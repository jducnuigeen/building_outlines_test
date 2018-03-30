# -*- coding: utf-8 -*-
#
# Building Outlines Test documentation build configuration file, created by
# sphinx-quickstart on Tue Mar 13 11:20:05 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import json
import re
from tabulate import tabulate
from os import path


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
#sys.path.insert(0, os.path.abspath('../buildings_outlines_test'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Building Outlines Test'
copyright = u'2018, Jan Ducnuigeen'
author = u'Jan Ducnuigeen'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.0.1'
# The full version, including alpha/beta/rc tags.
release = u'0.0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'page_width': 'auto',
    'sidebar_width': '200px',

}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'BuildingOutlinesTestdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'BuildingOutlinesTest.tex', u'Building Outlines Test Documentation',
     u'Jan Ducnuigeen', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'buildingoutlinestest', u'Building Outlines Test Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'BuildingOutlinesTest', u'Building Outlines Test Documentation',
     author, 'BuildingOutlinesTest', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Extensions and parsing SQL build scripts

# Test Data
#building_name_table = [
#                ["building_name_id", "character", "250", "noprec", "noscl", "An Id for a building name: 5","A hardware store" ],
#                ["building_id", "integer", "4", "noprec", "noscl", "3928", "A unique id for a building" ]
#                ]


schema_name_globvar = ''
tables = {}

def get_schema_name():
    # The path of this python script is:
    # home/jducnuigeen/dev/building_outlines_test/docs/source
    # the path of the sql file is:
    # home/jducnuigeen/dev/building_outlines_test/sql/
    schema_dict = {}
    schema_general = {}
    sql_file_path = "./sql_not_final_location/01-create_buildings_schema.sql"
    with open(sql_file_path) as f:
        # for line in f:
        #     # CREATE SCHEMA IF NOT EXISTS buildings;
        #     schemaname = re.search(r"(?:CREATE SCHEMA IF NOT EXISTS)\s(.*)(;)", line)
        #     # COMMENT ON SCHEMA buildings IS 'This schema holds all of the tables for buildings';
        #     schema_com_srch = re.search(r"(?:COMMENT ON SCHEMA)\s(.*)(?:IS)\s(')(.*)(')(;)", line)

        #     table_name_srch = re.search(r"(?:CREATE TABLE IF NOT EXISTS)(?:\s)(?:.*)(?:\.)(.*)(?:\s)(?:\()", line)


        #     if schemaname:
        #         schema = schemaname.group(1)
        #         schema_name_globvar = schema
        #         print "Processing schemaname"
        #         print "Schema Name: ", schema
        #         schema_dict = {}
        #         schema_dict = {"name": schema_name_globvar}
        #         print schema_dict
        #     elif schema_com_srch is not None:
        #         schema_comment = schema_com_srch.group(3)
        #         schema_dict['schemacomment'] = schema_comment
        #         print "Processing schema com srch"
        #         print schema_dict
        #     elif table_name_srch is not None:
        schema_general = {"schema_name": "buildings", "schema_com": "holds schema comment"}
        schema_list = [
        {"table_nam": "lifecycle_stage", "table_comment": "lifecycle_stage comment", "table_columns": [
                    ["lifecycle_stage_id", "integer", "", "32", "0", "", "Lookup table that holds all of the lifecycle stages for a building."],
                    ["value", "varchar", "40", "", "", "", "The stage of a buildings lifecycle."]
                            ]
             },
        {"table_nam": "use", "table_comment": "Lookup table that holds all of the uses for a building. These uses are the same as those used in the Topo50 map series.", "table_columns": [
                    ["use_id", "integer", "", "32", "0", "", "Unique identifier for the use."],
                    ["value", "varchar", "40", "", "", "", "The building use, maintained for the Topo50 map series."]
                            ]
        }
                    ]
        print "schema_dict", schema_dict
        print "schema_general", schema_general





    #schema_list = [schema_dict]
    #return schema_list
    return schema_general, schema_list
    f.close()


#schema_list_out = get_schema_name()
schema_general, schema_list_out = get_schema_name()


#rst_table = tabulate(building_name_table,tablefmt='rst', headers=["Column Name", "Data Type", "Length", "Width", "Precision", "Scale", "Example", "Description"])

#schema_name = [schema_name_globvar]



#test1 = {"name": "Test 1", "description": "Blah"}
#test2 = {"name": "Test 2", "description": "Blah de blah"}
#test3 = {"name": "Test 3", "description": "Blah bloo"}
#test4 = {"rst": rst_table}

#table_names = [test1, test2, test3]

#rst_out = [test4]

#json.dumps(rst_table)

# with open('dbschema.json', 'w') as outfile:
#    json.dump(rst_table, outfile)



def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    src = source[0]
    rendered = app.builder.templates.render_string(
        src, app.config.html_context
    )
    source[0] = rendered

def setup(app):
    app.connect("source-read", rstjinja)
    app.add_stylesheet('custom.css')

html_context = {
    'outputschema': schema_list_out,
    'schema_gen': schema_general
    #'something': table_names,
    #'rst': rst_out
}
