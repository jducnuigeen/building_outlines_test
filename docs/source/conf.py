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

# Script to parse database sql files into one dictionary and one list 
# The path of this conf.py script is:
# ../docs/source
# The path of the SQL file has been altered from likely final folder path

sql_file_path = "./sql_not_final_location/02-buildings_schema.sql"
#sql_file_path = "./sql_not_final_location/02-create_buildings_stage_schema.sql"

def get_schema():
    
    schema = {}  # This only hold the schema name and schema comment
    schema_count = 0
    with open(sql_file_path) as full_file:
        file_content = full_file.read()
    full_file.close()

    with open(sql_file_path) as f:
        for line in f:
            schema_search = re.search(r"(?:CREATE SCHEMA IF NOT EXISTS)\s(.*)(;)", line)
            #schema_comment_search = re.search(r"(?:COMMENT ON SCHEMA)\s(.*)(?:IS)\s(')(.*)(')(;)", line)
            schema_comment_search = re.search(r"(?:COMMENT ON SCHEMA .*?)\s(?:IS)\s(.+?)(?=\;)", file_content, re.DOTALL)

            if schema_count > 1:
                raise ValueError("More than one schema is defined in this SQL file: {}".format(sql_file_path))
            if schema_search is not None:
                schema_name = schema_search.group(1)
                schema = {"schema_name": schema_name}
                schema_count += 1
            if schema_comment_search is not None:
                schema_comment = schema_comment_search.group(1)
                schema_comment_clean = schema_comment.replace('\r\n', '').replace("'", "")
                schema['schema_com'] = schema_comment_clean

    f.close()
    return schema, schema_name
    


##############################################################################

# function to build a list of dictionaries (schema_list), with each dictionary (table_dict) containing all
# of the information for one table in the schema. Each of these dictionaries contains a key
# to hold a list (this_table_columns) of lists of the columns for each table.
def get_tables(schema_name):
    
    schema_list = []
    table_dict = {}
    
    # We open and save a copy of the SQL file into a variable, in order to search for components
    # which may have multiple rows (ie table comments or column comments). 
    with open(sql_file_path) as full_file:
        file_content = full_file.read()
    full_file.close()

    # reading by line by line is done so that no tables are missed
    with open(sql_file_path) as f:
        for line in f:

            table_name_srch = re.search(r"(?<=CREATE TABLE IF NOT EXISTS )(\w+)(?:\.)([^\(\s]*)", line)

            if table_name_srch is not None:
                # Now perform all actions to find table name, table comment, table columns, and table comments
                # and when done add all these content to table_dict, and then finally to schema_list

                table_dict = {}  # This dict hold all the information for one table
                table_name = table_name_srch.group(2)
                table_dict["table_nam"] = table_name
                table_str = schema_name + "." + table_name
                table_com_str = "(?<=COMMENT ON TABLE " + table_str + " IS)([^\;]*)"
                table_com_srch = re.search(table_com_str, file_content, re.DOTALL)
                this_table_columns = [] # this holds several lists, each list is is one column of info

                if table_com_srch is not None:
                    table_com_result = table_com_srch.group(0)
                    # remove line terminators and quote marks from multiline comment
                    table_com_result_clean = table_com_result.replace('\r\n', '').replace("'", "")
                    table_dict["table_comment"] = table_com_result_clean
                    # get the columns for this table
                    this_table_columns = get_columns(table_str, file_content, this_table_columns)
                    table_dict["table_columns"] = this_table_columns

                elif table_com_srch is None:
                    table_com_result = ''
                    table_dict["table_comment"] = ""
                    # get the columms for this table
                    this_table_columns = get_columns(table_str, file_content, this_table_columns)
                    table_dict["table_columns"] = this_table_columns

                schema_list.append(table_dict)

    print "Final schema_list is: ", schema_list
    f.close()
    return schema_list



# Get column comments which might contain multilines
def get_column_comments(column_str, file_content):
    col_com_str = r"(?:COMMENT ON COLUMN " + column_str + r")(?:\s)(?:IS)([^\;]*)"
    col_com_srch = re.search(col_com_str, file_content)

    if col_com_srch is not None:
        col_com = col_com_srch.group(1)
        col_com_result_clean = col_com.replace('\r\n', '').replace("'", "")

    if col_com_srch is None:
        col_com_result_clean = ""
    return col_com_result_clean


# Get the columns for one table, which are listed across multiple lines
def get_columns(table_str, file_content, this_table_columns):

    srch_str = r"(?<=CREATE TABLE IF NOT EXISTS " + table_str + r"\s\()[^\;]*(?=\)\;)"
    column_srch = re.search(srch_str, file_content)
    columns = column_srch.group(0)
    columns_strip = [x.strip() for x in columns.split(',')]

    for column_details in columns_strip:
        pri_key_srch = re.search(r"(.*)(?:serial PRIMARY KEY)", column_details)
        char_var_srch = re.search(r"(.*)(?:\s)(?:character varying)\((.*?)\)", column_details)
        timestamp1 = re.search(r"(.*)(?:\s)(?:timestamptz)", column_details)
        integer = re.search(r"^(.*)(?:\s)(?=integer)", column_details)
        shape = re.search(r"(shape)(?:.*)(?:geometry)", column_details)

        if pri_key_srch is not None:
            this_column = []
            pri_key = pri_key_srch.group(1)
            column_str = table_str + "." + pri_key
            this_column.append(pri_key) #column Name
            this_column.append("integer")  #Data Type
            this_column.append("") # Length
            this_column.append("32") #Precision
            this_column.append("0") #Scale
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif char_var_srch is not None:
            this_column = []
            var_column = char_var_srch.group(1)
            length = char_var_srch.group(2)
            column_str = table_str + "." + var_column
            this_column.append(var_column) #column Name
            this_column.append("varchar") #Data Type
            this_column.append(length) #Length
            this_column.append("") #Precision
            this_column.append("") #scale
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif timestamp1 is not None:
            this_column = []
            timecolumn1 = timestamp1.group(1)
            column_str = table_str + "." + timecolumn1
            this_column.append(timecolumn1) #column Name
            this_column.append("date") #Data Type
            this_column.append("") #Length
            this_column.append("") #Precision
            this_column.append("") #scale
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif integer is not None:
            this_column = []
            integercol = integer.group(1)
            column_str = table_str + "." + integercol
            this_column.append(integercol) #column Name
            this_column.append("integer") #Data Type
            this_column.append("") #Length
            this_column.append("32") #Precision
            this_column.append("0") #scale
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif shape is not None:
            this_column = []
            shapecol = shape.group(1)
            column_str = table_str + "." + shapecol
            this_column.append(shapecol) #column Name
            this_column.append("geometry") #Data Type
            this_column.append("") #Length
            this_column.append("") #Precision
            this_column.append("") #scale
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

    return this_table_columns

schema_out, schema_name = get_schema()

schema_list_out = get_tables(schema_name)



# This is required to allow Sphinx to read data dynamically
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
    'schema_gen': schema_out
}

# This is test data in case troubleshooting is required
        # schema_general = {"schema_name": "buildings", "schema_com": "holds schema comment"}
        # schema_list = [
        # {"table_nam": "lifecycle stage", "table_comment": "Lifecycle stage comments", "table_columns": [
        #             ["lifecycle_stage_id", "integer", "", "32", "0", "", "Lookup table that holds all of the lifecycle stages for a building."],
        #             ["value", "varchar", "40", "", "", "", "The stage of a buildings lifecycle."]
        #                     ]
        #      },
        # {"table_nam": "use", "table_comment": "Lookup table that holds all of the uses for a building. These uses are the same as those used in the Topo50 map series.", "table_columns": [
        #             ["use_id", "integer", "", "32", "0", "", "Unique identifier for the use."],
        #             ["value", "varchar", "40", "", "", "", "The building use, maintained for the Topo50 map series."]
        #                     ]
        # }
        #             ]
