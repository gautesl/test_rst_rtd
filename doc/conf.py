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
import sys
from pathlib import Path
# sys.path.insert(0, os.path.abspath('.'))
TEST_BASE = Path(__file__).resolve().parents[1]

# Add the '_extensions' directory to sys.path, to enable finding Sphinx
# extensions within.
sys.path.insert(0, str(TEST_BASE / "doc" / "_extensions"))


# -- Project information -----------------------------------------------------

project = 'Test RST on RTD'
copyright = '2022, Gaute Svanes Lunde'
author = 'Gaute Svanes Lunde'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "external_content"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_book_theme"
html_logo = "_static/images/logo.png"
html_favicon = "_static/images/favicon.ico"
html_static_path = ["_static"]
html_theme_options = {
    "logo_only": True,
    "github_url": "https://github.com/gautesl/test_rst_rtd",
    "repository_url": "https://github.com/gautesl/test_rst_rtd",
    "use_edit_page_button": True,
    "repository_branch": "master",
    "path_to_docs": "doc",
}

# -- Options for zephyr.external_content ----------------------------------

external_content_contents = [
    (TEST_BASE / "doc", "[!_]*"),
    (TEST_BASE / "doc", "_static/images"),
    (TEST_BASE, "src/**/*.rst"),
]

def setup(app):
    app.srcdir = str((Path("_build") / "src").resolve())