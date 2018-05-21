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
import re
from tabulate import tabulate
from os import path
import glob2
sys.path.insert(0, os.path.abspath('../../sql'))
site_url = "http://building-outlines-test.readthedocs.io/en/latest/"


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
    'sphinx.ext.autosectionlabel'
]

# 'sphinx.ext.autosectionlabel'
# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'NZ Buildings Data Dictionary'
author = u'Land Information NZ'

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
#exclude_patterns = []

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
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'sticky_navigation': True

}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'NZ Buildings Data Dictionary'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'NZ Buildings Data Dictionary'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'logo.png'

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
# html_extra_path = ['../../sql']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%B %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {'**': ['about.html'] }

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
html_show_copyright = False

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
htmlhelp_basename = 'NZ_Buildings'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
#latex_documents = [
#    (master_doc, 'BuildingOutlines.tex', u'Building Outlines Data Documentation',
#     u'LINZ', 'manual'),
#]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

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
    (master_doc, 'buildings_data_dictionary', u'buildings_data_dictionary',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'buildings_data_dictionary', u'NZ Buildings Data Dictionary',
     author, 'LINZ', 'Documentation for the NZ Buildings Dataset',
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
# The path of the SQL file is in the root repo folder




def get_schema(sql_file_path):
    
    schema = {}  # This only hold the schema name and schema comment
    schema_count = 0
    with open(sql_file_path) as full_file:
        file_content = full_file.read()
    full_file.close()

    with open(sql_file_path) as f:
        for line in f:
            schema_search = re.search(r"CREATE SCHEMA IF NOT EXISTS\s(.*);", line)
            schema_comment_search = re.search(r"COMMENT ON SCHEMA .*?\sIS\s(.+?)\;", file_content, re.DOTALL)

            if schema_search is not None:
                schema_count += 1
                if schema_count > 1:
                    raise ValueError("More than one schema is defined in this SQL file: {}".format(sql_file_path))
                else:
                    schema_name = schema_search.group(1)
                    schema["name"] = schema_name

            if schema_comment_search is not None:
                schema_comment = schema_comment_search.group(1)
                schema_comment_clean = schema_comment.replace("\r\n", "").replace("'", "")
                schema['comment'] = schema_comment_clean

    f.close()
    return schema



##############################################################################

# function to build a list of dictionaries (schema_tabulate_list), with each dictionary (table_dict_tabulate) containing all
# of the information for one table in the schema. Each of these dictionaries contains a key
# to hold a list (this_table_columns) of lists of the columns for each table.
def get_tables(schema_out, sql_file_path):

    schema_list = []
    schema_tabulate_list = []
    table_dict_tabulate = {}

    # We open and save a copy of the SQL file into a variable, in order to search for components
    # which may have multiple rows (ie table comments or column comments). 
    with open(sql_file_path) as full_file:
        file_content = full_file.read()
    full_file.close()

    # reading by line by line is done so that no tables are missed
    with open(sql_file_path) as f:
        for line in f:

            table_name_search = re.search(r"CREATE TABLE IF NOT EXISTS \w+\.([^\(\s]*)", line)

            if table_name_search is not None:
                # Now perform all actions to find table name, table comment, table columns, and table comments
                # and when done add all these content to table_dict, and then finally to schema_tabulate_list

                table_dict_tabulate = {} # This dict hold all the information for one table
                table_name = table_name_search.group(1)
                table_dict_tabulate["table_nam"] = table_name
                table_str = schema_out["name"] + "." + table_name
                table_comment_str = "(?<=COMMENT ON TABLE " + table_str + " IS)([^\;]*)"
                table_comment_search = re.search(table_comment_str, file_content, re.DOTALL)
                this_table_columns = [] # this holds several lists, each list is is one column of info

                if table_comment_search is not None:
                    table_comment_result = table_comment_search.group(1)
                    # remove line terminators and quote marks from multiline comment
                    table_comment_result_clean = table_comment_result.replace("\r\n", "").replace("'", "")
                    table_dict_tabulate["table_comment"] = table_comment_result_clean
                    # get the columns for this table
                    this_table_columns = get_columns(table_str, file_content, this_table_columns)
                    headers = ["Column Name", "Data Type", "Length", "Precision", "Scale", "Allows Nulls", "Description"]
                    tabulate_columns = tabulate(this_table_columns, tablefmt="rst", headers = headers)
                    tabulate_split = [x.split(",")for x in tabulate_columns.split('\n')]
                    table_dict_tabulate["table_columns"] = tabulate_split

                elif table_comment_search is None:
                    # get the columms for this table
                    this_table_columns = get_columns(table_str, file_content, this_table_columns)
                    table_dict_tabulate["table_comment"] = " "
                    headers = ["Column Name", "Data Type", "Length", "Precision", "Scale", "Allows Nulls", "Description"]
                    tabulate_columns = tabulate(this_table_columns, tablefmt="rst", headers = headers)
                    tabulate_split = [x.split(",")for x in tabulate_columns.split("\n")]
                    table_dict_tabulate["table_columns"] = tabulate_split

                schema_tabulate_list.append(table_dict_tabulate)


    f.close()
    return schema_tabulate_list



# Get column comments which might contain multilines
# If a column is a foreign key to another table, create hyperlinks to that RTD table
def get_column_comments(column_str, file_content):
    column_comment_str = r"COMMENT ON COLUMN " + column_str + r"\sIS([^\;]*)"
    column_comment_search = re.search(column_comment_str, file_content)
    schema_check = column_str.split('.')[0]

    if column_comment_search is not None:
        column_comment = column_comment_search.group(1)
        column_comment_result_clean = column_comment.replace("\r\n", "").replace("'", "").replace("\n", "")
        column_comment_result_strip = column_comment_result_clean.strip()
        column_comment_result_clean_lower = column_comment_result_clean.lower().strip()
        if "foreign key to the" in column_comment_result_clean_lower:
            foreign_search = re.search(r"(.*)(foreign key to the\s)(.*\..*)\stable(.*)", column_comment_result_strip, re.IGNORECASE)
            if foreign_search is not None:
                schema_and_table = foreign_search.group(3)
                schema_and_table_strip = schema_and_table.strip()
                front_comment = foreign_search.group(1)
                end_comment = foreign_search.group(4)
                foreign_key_comment = foreign_search.group(2)
                schema_named, table_named = schema_and_table.split(".")
                hyphens = table_named.replace("_", "-")
                if schema_check == "buildings" or schema_check == "buildings_common" or schema_check == "buildings_bulk_load":
                    #template_url = "`{schema_table} <https://building-outlines-test.readthedocs.io/en/latest/internal_data.html#table-{table_name_hyphens}>`_"
                    template_url = "`{schema_table} <{site_url}internal_data.html#table-{table_name_hyphens}>`_"
                    foreign_link = template_url.format(schema_table=schema_and_table_strip, site_url= site_url, table_name_hyphens=hyphens)
                    column_comment_result_strip = front_comment + foreign_key_comment + foreign_link + " table" + end_comment
                if schema_check == "buildings_lds":
                    template_url = "`{schema_table} <https://building-outlines-test.readthedocs.io/en/latest/published_data.html#table-{table_name_hyphens}>`_"
                    foreign_link = template_url.format(schema_table=schema_and_table_strip, table_name_hyphens=hyphens)
                    column_comment_result_strip = front_comment + foreign_key_comment + foreign_link + " table" + end_comment

    if column_comment_search is None:
        column_comment_result_strip = " "
    return column_comment_result_strip


# Get the columns for one table, which are listed across multiple lines 
def get_columns(table_str, file_content, this_table_columns):

    search_str = r"CREATE TABLE IF NOT EXISTS " + table_str + r"\s\(([^\;]*)\)\;"
    column_search = re.search(search_str, file_content)
    columns = column_search.group(1)
    columns_strip = [x.strip() for x in columns.split("    ,")]


    for column_details in columns_strip:
        pri_key_serial_search = re.search(r"(.*)\sserial PRIMARY KEY", column_details)
        pri_key_search = re.search(r"(.*)\sinteger PRIMARY KEY", column_details)
        pri_key_integer_not_null_search = re.search(r"(.*)\sinteger(?=.*?(NOT NULL))(?=.*?(PRIMARY KEY))", column_details)
        character_varying_search = re.search(r"(.*)\scharacter varying\((.*?)\)(?! NOT NULL)", column_details)  #does not contain "NOT NULL"
        character_varying_not_null_search = re.search(r"(.*)\scharacter varying\((.*?)\)\sNOT NULL", column_details)  #does contain "NOT NULL"
        timestamp_search = re.search(r"(.*)\stimestamptz(?! NOT NULL)", column_details)  #does not contain "NOT NULL"
        timestamp_not_null_search = re.search(r"^(.*)\stimestamptz\sNOT NULL.*", column_details)  #does contain "NOT NULL"
        integer_search = re.search(r"^(.*)\sinteger(?!.*NOT NULL)", column_details)  #does not contain "NOT NULL"
        integer_not_null_search = re.search(r"^(.*)\sinteger\sNOT NULL.*", column_details)  #does contain "NOT NULL"
        numeric_search = re.search(r"(.*)\snumeric\((.*)\,(.*)\)(?! NOT NULL)", column_details)
        numeric_not_null_search = re.search(r"(.*)\snumeric\((.*)\,(.*)\).*NOT NULL", column_details)
        shape = re.search(r"(shape).*geometry", column_details)
        text_not_null_search = re.search(r"(.*)\stext NOT NULL", column_details)
        text_search = re.search(r"(.*)\stext", column_details)
        date_search = re.search(r"(.*)\sdate(?!.*NOT NULL)", column_details)  # does not contain NOT NULL
        date_not_null_search = re.search(r"(.*)\sdate\sNOT NULL", column_details)  # contains NOT NULL
        decimal_search = re.search(r"(.*)\sdecimal\((\d{1,2})\,\s(\d{1,2})\)(?! NOT NULL)", column_details)
        decimal_not_null_search = re.search(r"(.*)\sdecimal\((\d{1,2})\,\s(\d{1,2}).*NOT NULL", column_details)

        if pri_key_serial_search is not None:
            this_column = []
            pri_key = pri_key_serial_search.group(1)
            pri_key2 = pri_key.strip()
            pri_key_str = " **" + pri_key2 + "** "
            column_str = table_str + "." + pri_key2
            this_column.append(pri_key_str)  #column Name
            this_column.append("integer")  #Data Type
            this_column.append("32")  # Length
            this_column.append(" ")  #Precision
            this_column.append(" ")  # Scale
            this_column.append("No") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out)  # Description
            this_table_columns.append(this_column)

        elif pri_key_search is not None:
            this_column = []
            pri_key = pri_key_search.group(1)
            pri_key2 = pri_key.strip()
            pri_key_str = " **" + pri_key2 + "** "
            column_str = table_str + "." + pri_key2
            this_column.append(pri_key_str)  #column Name
            this_column.append("integer")  #Data Type
            this_column.append("32")  # Length
            this_column.append(" ")  #Precision
            this_column.append(" ")  # Scale
            this_column.append("No") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out)  # Description
            this_table_columns.append(this_column)

        elif pri_key_integer_not_null_search is not None:
            this_column = []
            pri_key = pri_key_integer_not_null_search.group(1)
            pri_key2 = pri_key.strip()
            pri_key_str = " **" + pri_key2 + "** "
            column_str = table_str + "." + pri_key2
            this_column.append(pri_key_str)  #column Name
            this_column.append("integer")  #Data Type
            this_column.append("32")  # Length
            this_column.append(" ")  #Precision
            this_column.append(" ")  # Scale
            this_column.append("No") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out)  # Description
            this_table_columns.append(this_column)

        elif character_varying_search is not None:
            this_column = []
            var_column = character_varying_search.group(1)
            length = character_varying_search.group(2)
            column_str = table_str + "." + var_column
            this_column.append(var_column) #column Name
            this_column.append("varchar") #Data Type
            this_column.append(length) #Length
            this_column.append(" ") #Precision
            this_column.append(" ") #scale
            this_column.append("Yes") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif character_varying_not_null_search is not None:
            this_column = []
            var_column = character_varying_not_null_search.group(1)
            length = character_varying_not_null_search.group(2)
            column_str = table_str + "." + var_column
            this_column.append(var_column) #column Name
            this_column.append("varchar") #Data Type
            this_column.append(length) #Length
            this_column.append(" ") #Precision
            this_column.append(" ") #scale
            this_column.append("No") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif timestamp_search is not None:
            this_column = []
            timecolumn1 = timestamp_search.group(1)
            column_str = table_str + "." + timecolumn1
            this_column.append(timecolumn1) #column Name
            this_column.append("date") #Data Type
            this_column.append(" ") #Length
            this_column.append(" ") #Precision
            this_column.append(" ") #scale
            this_column.append("Yes") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif timestamp_not_null_search is not None:
            this_column = []
            timecolumn2 = timestamp_not_null_search.group(1)
            column_str = table_str + "." + timecolumn2
            this_column.append(timecolumn2) #column Name
            this_column.append("date") #Data Type
            this_column.append(" ") #Length
            this_column.append(" ") #Precision
            this_column.append(" ") #scale
            this_column.append("No") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif integer_search is not None:
            this_column = []
            integer_column_name = integer_search.group(1)
            column_str = table_str + "." + integer_column_name
            this_column.append(integer_column_name) #column Name
            this_column.append("integer") #Data Type
            this_column.append("32") #Length
            this_column.append(" ") #Precision
            this_column.append(" ") #scale
            this_column.append("Yes") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif integer_not_null_search is not None:
            this_column = []
            integer_column_name = integer_not_null_search.group(1)
            column_str = table_str + "." + integer_column_name
            this_column.append(integer_column_name) #column Name
            this_column.append("integer") #Data Type
            this_column.append("32") #Length
            this_column.append(" ") #Precision
            this_column.append(" ") #scale
            this_column.append("No") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif numeric_search is not None:
            this_column = []
            numeric_column_name = numeric_search.group(1)
            numeric_precision = numeric_search.group(2)
            numeric_scale = numeric_search.group(3)
            column_str = table_str + "." + numeric_column_name
            this_column.append(numeric_column_name) #column Name
            this_column.append("numeric") #Data Type
            this_column.append(" ") #Length
            this_column.append(str(numeric_precision)) #Precision
            this_column.append(str(numeric_scale)) #scale
            this_column.append("Yes") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif numeric_not_null_search is not None:
            this_column = []
            numeric_column_name = numeric_not_null_search.group(1)
            numeric_precision = numeric_not_null_search.group(2)
            numeric_scale = numeric_not_null_search.group(3)
            column_str = table_str + "." + numeric_column_name
            this_column.append(numeric_column_name) #column Name
            this_column.append("numeric") #Data Type
            this_column.append("32") #Length
            this_column.append(str(numeric_precision)) #Precision
            this_column.append(str(numeric_scale)) #scale
            this_column.append("No") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif shape is not None:
            this_column = []
            shape_column_name = shape.group(1)
            column_str = table_str + "." + shape_column_name
            this_column.append(shape_column_name) #column Name
            this_column.append("geometry") #Data Type
            this_column.append(" ") #Length
            this_column.append(" ") #Precision
            this_column.append(" ") #scale
            this_column.append("No") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif text_not_null_search is not None:
            this_column = []
            text_not_null_column_name = text_not_null_search.group(1)
            column_str = table_str + "." + text_not_null_column_name
            this_column.append(text_not_null_column_name) #column Name
            this_column.append("text") #Data Type
            this_column.append(" ") #Length
            this_column.append(" ") #Precision
            this_column.append(" ") #scale
            this_column.append("No") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif text_search is not None:
            this_column = []
            text_column_name = text_search.group(1)
            column_str = table_str + "." + text_column_name
            this_column.append(text_column_name) #column Name
            this_column.append("text") #Data Type
            this_column.append(" ") #Length
            this_column.append(" ") #Precision
            this_column.append(" ") #scale
            this_column.append("Yes") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif date_search is not None:
            this_column = []
            date_column_name = date_search.group(1)
            column_str = table_str + "." + date_column_name
            this_column.append(date_column_name) #column Name
            this_column.append("date") #Data Type
            this_column.append("4") #Length
            this_column.append(" ") #Precision
            this_column.append(" ") #scale
            this_column.append("Yes") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif date_not_null_search is not None:
            this_column = []
            date_not_null_column_name = date_not_null_search.group(1)
            column_str = table_str + "." + date_not_null_column_name
            this_column.append(date_not_null_column_name) #column Name
            this_column.append("date") #Data Type
            this_column.append("4") #Length
            this_column.append(" ") #Precision
            this_column.append(" ") #scale
            this_column.append("No") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif decimal_search is not None:
            this_column = []
            decimal_column_name = decimal_search.group(1)
            numeric_precision = decimal_search.group(2)
            numeric_scale = decimal_search.group(3)
            column_str = table_str + "." + decimal_column_name
            this_column.append(decimal_column_name) #column Name
            this_column.append("decimal") #Data Type
            this_column.append(" ") #Length
            this_column.append(str(numeric_precision)) #Precision
            this_column.append(str(numeric_scale)) #scale
            this_column.append("Yes") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif decimal_not_null_search is not None:
            this_column = []
            decimal_not_null_column_name = decimal_not_null_search.group(1)
            numeric_precision = decimal_not_null_search.group(2)
            numeric_scale = decimal_not_null_search.group(3)
            column_str = table_str + "." + decimal_not_null_column_name
            this_column.append(decimal_not_null_column_name) #column Name
            this_column.append("decimal") #Data Type
            this_column.append(" ") #Length
            this_column.append(str(numeric_precision)) #Precision
            this_column.append(str(numeric_scale)) #scale
            this_column.append("No") # Allows Nulls
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)


    return this_table_columns

def get_filenames():

    # read the path and file names of all of the SQL schema files in the /SQL folder
    # including subfolders
    filenames = glob2.glob("../../sql/**/*")
    for name in filenames:
        if "schema" not in name:
            filenames.remove(name)
    return filenames


def setup_html_context(files_to_read):

    # Generate a dict containing HTML_context items needed by Sphinx build process.
    # One schema_gen and one schema_tab for each schema.
    context = {}

    for f in files_to_read:
        sql_file_path = f
        schema_name_search = re.search(r".*\-(.*)\_schema.*", sql_file_path)
        name_key = schema_name_search.group(1)
        context_key = "schema_gen_" + name_key
        schema_out = get_schema(sql_file_path)
        context[context_key] = schema_out
        context_table_key = "schema_tab_" + name_key
        schema_tabulate_list_out = get_tables(schema_out, sql_file_path)
        context[context_table_key] = schema_tabulate_list_out

    return context


files_to_read = get_filenames()

context_out = setup_html_context(files_to_read)




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

html_context = context_out
