# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'fourier-optics'
copyright = '2023, Tony Allen'
author = 'Tony Allen'

# The full version, including alpha/beta/rc tags
release = '0.1'
import os
import sys
import sphinx_rtd_theme
from sphinx_gallery.sorting import FileNameSortKey
sys.path.insert(0, os.path.abspath('..'))


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinxcontrib.bibtex",
    "sphinx.ext.mathjax",
    "sphinx_gallery.gen_gallery",
]

# Allows to link to external modules
intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable/", None),
    'python': ('http://docs.python.org/3', None),
}

# sphinx-gallery configuration, allows for demo code in documentation
sphinx_gallery_conf = {
    # path to your example scripts
    'examples_dirs': ['../../demos'],
    # path to where to save gallery generated output
    'gallery_dirs': ['auto_demos'],
    # specify that examples should be ordered according to filename
    'within_subsection_order': FileNameSortKey,
    # # directory where function granular galleries are stored
    # 'backreferences_dir': 'gen_modules/backreferences',
    # Modules for which function level galleries are created.  In
    # this case sphinx_gallery and numpy in a tuple of strings.
    'doc_module': ('optics'),
    # only parse and add files beginning with 'demo', default='plot_'
    'filename_pattern': '/demo',
    # Remove download button
    'download_all_examples': False,
}

# bibliography file path
bibtex_bibfiles = ["references.bib"]

autosummary_generate = True
autoclass_content = "both"
add_function_parentheses = True

# Sort members by type
autodoc_member_order = "bysource"
autodoc_default_options = {
    "member-order": "bysource",
    "inherited-members": True,
    "show-inheritance": True,
}
autodoc_docstring_signature = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for Napoleon -----------------------------------------------------

napoleon_google_docstring = True
#napoleon_numpy_docstring = True
#napoleon_include_private_with_doc = False
#napoleon_include_special_with_doc = False
#napoleon_use_admonition_for_examples = False
#napoleon_use_admonition_for_notes = False
#napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
#napoleon_use_param = False
napoleon_use_rtype = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# #html_theme = 'sphinx_material'
# html_theme = "faculty-sphinx-theme"
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]