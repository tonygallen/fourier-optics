r"""Free-space propagator classes.
"""

import numpy as np
from typing import Optional, Sequence
from optics.typing import Array


class Propagator:
    r"""Free space wave propagator

    Propagates a planar source field, :math:`U(x, y, 0)` a distance :math:`z`,
    computed via the exact transfer function given by (Eq. 5-4, :cite:`goodmanIntroductionFourierOptics`)

    .. math ::
        U(x, y, z) = \mathcal{F}^{-1} \left( \mathcal{F}(U(x,y,0)) \times
        e^{j 2 \pi z / \lambda \sqrt{1 - (\lambda f_x)^2 - (\lambda f_x)^2}} \right) \;,

    where the :math:`\mathcal{F}` is the Fourier transform, implemented by :func:`numpy.fft.fftn`.
    """
    def __init__(
            self,
            input_shape: Sequence[int],
            dx: Sequence[float],
            wavelength: float,
            z: float,
    ):
        r"""
        Args:
            input_shape: Shape of input array.
            dx: Sampling interval at source plane, :math:`(\Delta x, \Delta y)`.
            wavelength: Illumination wavelength, :math:`\lambda`.
            z: Propagation distance, :math:`z`.
        """
        self.input_shape = input_shape
        self.dx = dx
        self.wavelength = wavelength
        self.z = z

        # only works with 2D images
        assert len(input_shape) == len(dx) == 2

        # define frequencies
        fx = np.fft.fftfreq(input_shape[0], dx[0])
        fy = np.fft.fftfreq(input_shape[1], dx[1])
        fxy2 = fx[None, :] ** 2 + fy[:, None] ** 2
        fxy2 = np.fft.fftshift(fxy2)
        self.fxy2 = fxy2

        self.transfer_function = np.exp(1j * 2 * np.pi * z / wavelength * np.emath.sqrt(1 - fxy2 * wavelength ** 2))

    def __call__(self, x: Array):
        return ifft(fft(x) * self.transfer_function)


class FresnelPropagator(Propagator):
    r"""Free space Fresnel wave propagator

    Propagates a planar source field, :math:`U(x, y, 0)` a distance :math:`z`,
    computed via the Fresnel transfer function given by (Eq. 5-3, :cite:`goodmanIntroductionFourierOptics`)

    .. math ::
         U(x, y, z) = \mathcal{F}^{-1} \left( \mathcal{F} (U(x,y,0)) \times \,
           e^{j2\pi z / \lambda} \times e^{-j\pi \lambda z (f_x^2 + f_y^2)} \right) \;,

    where the :math:`\mathcal{F}` is the Fourier transform, implemented by :func:`numpy.fft.fftn`.
    """
    def __init__(
            self,
            input_shape: Sequence[int],
            dx: Sequence[float],
            wavelength: float,
            z: float,
    ):
        r"""
        Args:
            input_shape: Shape of input array.
            dx: Sampling interval at source plane, :math:`(\Delta x, \Delta y)`.
            wavelength: Illumination wavelength, :math:`\lambda`.
            z: Propagation distance, :math:`z`.
        """
        super().__init__(
            input_shape=input_shape,
            dx=dx,
            wavelength=wavelength,
            z=z,
        )

        self.transfer_function = np.exp(1j * 2 * np.pi * z / wavelength) * np.exp(-1j * np.pi * wavelength * z *
                                                                                  self.fxy2)


class FraunhoferPropagator:
    pass


def fft(
        x: Array,
        output_shape: Optional[Sequence[int]] = None,
        axes: Optional[Sequence[int]] = None,
        norm: Optional[str] = 'ortho',
) -> Array:
    """
    Compute the N-dimensional discrete Fourier Transform

    Args:
        x: Input array
        output_shape: Shape of output array. Defaults to input shape.
        axes: Axes over which to compute the FFT. Defaults to all axes.
        norm: Method of normalizing FFT. Either "backward", "ortho", "forward".
            Defaults to "ortho".
    Returns:
        out: Output array

    """
    out = np.fft.fftshift(
        x=np.fft.fftn(
            a=np.fft.ifftshift(x=x, axes=axes,),
            s=output_shape,
            axes=axes,
            norm=norm
        ),
        axes=axes
    )
    return out


def ifft(
        x: Array,
        output_shape: Optional[Sequence[int]] = None,
        axes: Optional[Sequence[int]] = None,
        norm: Optional[str] = 'ortho',
) -> Array:
    """
    Compute the N-dimensional inverse discrete Fourier transform

    Args:
        x: Input array
        output_shape: Shape of output array. Defaults to input shape.
        axes: Axes over which to compute the FFT. Defaults to all axes.
        norm: Method of normalizing FFT. Either "backward", "ortho", "forward".
            Defaults to "ortho".
    Returns:
        out: Output array
    """

    out = np.fft.fftshift(
        x=np.fft.ifftn(
            a=np.fft.ifftshift(x=x, axes=axes,),
            s=output_shape,
            axes=axes,
            norm=norm
        ),
        axes=axes
    )
    return out
