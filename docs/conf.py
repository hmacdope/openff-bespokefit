# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# Incase the project was not installed
import os
import sys

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "BespokeFit"
copyright = (
    "2020, Joshua Horton. Project structure based on the "
    "Computational Molecular Science Python Cookiecutter version 1.1"
)
author = "Joshua Horton"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = ""


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "myst_parser",
    "sphinxcontrib.autodoc_pydantic",
    "doctest_oxide",
    "sphinx_click",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "openff.toolkit": (
        "https://open-forcefield-toolkit.readthedocs.io/en/stable/",
        None,
    ),
    "openff.fragmenter": ("https://fragmenter.readthedocs.io/en/stable/", None),
    "openff.qcsubmit": ("https://openff-qcsubmit.readthedocs.io/en/stable/", None),
    "mdtraj": ("https://www.mdtraj.org/1.9.5/", None),
}

autosummary_generate = True
autosummary_imported_members = False
autosummary_ignore_module_all = False
autosummary_context = {
    # Modules to exclude from API docs
    "exclude_modules": [
        "openff.bespokefit.cli",
        "openff.bespokefit.tests",
    ]
}
autodoc_default_options = {
    "member-order": "bysource",
    "undoc-members": True,
    "members": True,
    "inherited-members": False,
    "show-inheritance": True,
}
autodoc_preserve_defaults = True
autodoc_inherit_docstrings = False
autodoc_typehints_format = "short"

autodoc_pydantic_model_member_order = "groupwise"
autodoc_pydantic_model_signature_prefix = "model"
autodoc_pydantic_model_show_validator_members = False
autodoc_pydantic_model_show_validator_summary = False
autodoc_pydantic_model_show_config_summary = False
autodoc_pydantic_model_show_config_member = False
autodoc_pydantic_model_show_json = False
autodoc_pydantic_settings_signature_prefix = "settings"
autodoc_pydantic_settings_show_validator_members = False
autodoc_pydantic_settings_show_validator_summary = False
autodoc_pydantic_settings_show_config_summary = False
autodoc_pydantic_settings_show_config_member = False
autodoc_pydantic_field_doc_policy = "both"
autodoc_pydantic_field_list_validators = False

napoleon_google_docstring = True
napoleon_use_param = False
napoleon_use_ivar = True

myst_enable_extensions = [
    "deflist",
    "smartquotes",
    "replacements",
    "dollarmath",
    "colon_fence",
]

# sphinx-notfound-page
# https://github.com/readthedocs/sphinx-notfound-page
# Renders a 404 page with absolute links
import importlib

if importlib.util.find_spec("notfound"):
    extensions.append("notfound.extension")

    notfound_context = {
        "title": "404: File Not Found",
        "body": """
    <h1>404: File Not Found</h1>
    <p>
        Sorry, we couldn't find that page. This often happens as a result of
        following an outdated link. Please check the latest stable version
        of the docs, unless you're sure you want an earlier version, and
        try using the search box or the navigation menu on the left.
    </p>
    <p>
    </p>
    """,
    }

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "default"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
extensions.append("openff_sphinx_theme")
html_theme = "openff_sphinx_theme"

LOCALTOC_ON_LEFT = ["globaltoc.html", "searchbox.html"]
LOCALTOC_ON_RIGHT = ["globaltoc.html", "localtoc.html", "searchbox.html"]
html_sidebars = {
    "*": LOCALTOC_ON_LEFT,
    "getting-started/**": LOCALTOC_ON_LEFT,
    "users/**": LOCALTOC_ON_LEFT,
    "ref/**": LOCALTOC_ON_RIGHT,
    "developers/**": LOCALTOC_ON_LEFT,
}

# Theme options are theme-specific and customize the look and feel of a
# theme further.
html_theme_options = {
    # Repository integration
    # Set the repo url for the link to appear
    "repo_url": "https://github.com/openforcefield/openff-bespokefit",
    # The name of the repo. If must be set if repo_url is set
    "repo_name": "openff-bespokefit",
    # Must be one of github, gitlab or bitbucket
    "repo_type": "github",
    # Colour for sidebar captions and other accents. One of
    # openff-blue, openff-toolkit-blue, openff-dataset-yellow,
    # openff-evaluator-orange, aquamarine, lilac, amaranth, grape,
    # violet, pink, pale-green, green, crimson, eggplant, turquoise,
    # or a tuple of three ints in the range [0, 255] corresponding to
    # a position in RGB space.
    "color_accent": "openff-evaluator-orange",
    "html_minify": False,
    "html_prettify": False,
    "css_minify": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "bespokefitdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "bespokefit.tex", "BespokeFit Documentation", "bespokefit", "manual"),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "bespokefit", "BespokeFit Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "bespokefit",
        "BespokeFit Documentation",
        author,
        "bespokefit",
        "Creating bespoke parameters for individual molecules.",
        "Miscellaneous",
    ),
]


# -- Extension configuration -------------------------------------------------
