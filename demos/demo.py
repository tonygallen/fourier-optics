"""
Fresnel Propagator demo
=======================
This demo will compute and display the Fresnel transform of a given aperture.
"""

import numpy as np
from matplotlib import pyplot as plt
from optics.propagators import FresnelPropagator
from typing import Sequence


# %%
# Build the aperture
# ------------------
# First we define a circle function.
def circle(shape: Sequence[int], radius: float):
    """Create a circle of a given radius centered in an array of a given shape."""
    for dim in shape:
        assert radius < dim

    x, y = np.meshgrid(np.arange(shape[0]), np.arange(shape[1]))
    r = np.abs((x - (shape[0] - 1) / 2) ** 2 + (y - (shape[1] - 1) / 2) ** 2) < radius ** 2
    return r.astype('int')


# %%
# Then we define some parameters and build the aperture.
input_shape = (300, 300)
dx = (1e-2, 1e-2)
z = 1e5
wavelength = 1e-6

aperture = circle(shape=input_shape, radius=50)
aperture = aperture - circle(shape=input_shape, radius=10)
diag_idx = np.diag_indices(300)
aperture[diag_idx[0], diag_idx[1]] = 0
aperture[np.flip(diag_idx[0]), diag_idx[1]] = 0

plt.imshow(aperture)
plt.title('Aperture')
plt.show()

# %%
# Call the Fresnel Propagator
# ---------------------------
fresnel_propagator = FresnelPropagator(
    input_shape=input_shape,
    dx=dx,
    z=z,
    wavelength=wavelength,
)

y = fresnel_propagator(aperture)

# %%
# Plot the field at distance :math:`z`
# -------------------------------------------------

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(abs(y) ** 2)
ax1.set_title("Intensity")
ax2.imshow(np.angle(y))
ax2.set_title("Phase")

plt.show()