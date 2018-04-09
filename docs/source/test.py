import os
import sys
import re
from os import path
from itertools import takewhile
from tabulate import tabulate
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

# function to build a list of dictionaries (schema_list), with each dictionary (table_dict) containing all
# of the information for one table in the schema. Each of these dictionaries contains a key
# to hold a list (this_table_columns) of lists of the columns for each table.
def get_tables(schema_out):
    
    schema_list = []
    schema_tabulate_list = []
    table_dict = {}
    table_dict_tab = {}
    
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
                # and when done add all these content to table_dict, and then finally to schema_list

                table_dict = {}  # This dict hold all the information for one table
                table_dict_tab = {}
                table_name = table_name_search.group(1)
                table_dict["table_nam"] = table_name
                table_dict_tab["table_nam"] = table_name
                table_str = schema_out["name"] + "." + table_name
                table_comment_str = "(?<=COMMENT ON TABLE " + table_str + " IS)([^\;]*)"
                table_comment_search = re.search(table_comment_str, file_content, re.DOTALL)
                this_table_columns = [] # this holds several lists, each list is is one column of info

                if table_comment_search is not None:
                    table_comment_result = table_comment_search.group(1)
                    # remove line terminators and quote marks from multiline comment
                    table_comment_result_clean = table_comment_result.replace("\r\n", "").replace("'", "")
                    table_dict["table_comment"] = table_comment_result_clean
                    table_dict_tab["table_comment"] = table_comment_result_clean
                    # get the columns for this table
                    this_table_columns = get_columns(table_str, file_content, this_table_columns)
                    table_dict["table_columns"] = this_table_columns
                    # temporary
                    headers = ["Column Name", "Data Type", "Length", "Precision", "Scale", "Description"]
                    tabulate_col = tabulate(this_table_columns,tablefmt='rst', headers = headers)
                    table_dict_tab["table_columns"] = tabulate_col

                elif table_comment_search is None:
                    table_dict["table_comment"] = ""
                    # get the columms for this table
                    this_table_columns = get_columns(table_str, file_content, this_table_columns)
                    table_dict["table_columns"] = this_table_columns
                    # temporary
                    table_dict_tab["table_comment"] = ""
                    headers = ["Column Name", "Data Type", "Length", "Precision", "Scale", "Description"]
                    tabulate_col = tabulate(this_table_columns,tablefmt='rst', headers = headers)
                    table_dict_tab["table_columns"] = tabulate_col

                schema_list.append(table_dict)
                # temporary
                schema_tabulate_list.append(table_dict_tab)
                print schema_tabulate_list


    f.close()
    return schema_list, schema_tabulate_list



# Get column comments which might contain multilines
def get_column_comments(column_str, file_content):
    column_comment_str = r"COMMENT ON COLUMN " + column_str + r"\sIS([^\;]*)"
    column_comment_search = re.search(column_comment_str, file_content)

    if column_comment_search is not None:
        column_comment = column_comment_search.group(1)
        column_comment_result_clean = column_comment.replace("\r\n", "").replace("'", "")

    if column_comment_search is None:
        column_comment_result_clean = ""
    return column_comment_result_clean


# Get the columns for one table, which are listed across multiple lines
def get_columns(table_str, file_content, this_table_columns):

    search_str = r"CREATE TABLE IF NOT EXISTS " + table_str + r"\s\(([^\;]*)\)\;"
    column_search = re.search(search_str, file_content)
    columns = column_search.group(0)
    columns_strip = [x.strip() for x in columns.split(',')]

    for column_details in columns_strip:
        pri_key_search = re.search(r"(.*)serial PRIMARY KEY", column_details)
        character_varying_search = re.search(r"(.*)\scharacter varying\((.*?)\)", column_details)
        timestamp_search = re.search(r"(.*)\stimestamptz", column_details)
        integer_search = re.search(r"^(.*)\sinteger", column_details)
        shape = re.search(r"(shape).*geometry", column_details)

        if pri_key_search is not None:
            this_column = []
            pri_key = pri_key_search.group(1)
            column_str = table_str + "." + pri_key
            this_column.append(pri_key) #column Name
            this_column.append("integer")  #Data Type
            this_column.append("") # Length
            this_column.append("32") #Precision
            this_column.append("0") #Scale
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif character_varying_search is not None:
            this_column = []
            var_column = character_varying_search.group(1)
            length = character_varying_search.group(2)
            column_str = table_str + "." + var_column
            this_column.append(var_column) #column Name
            this_column.append("varchar") #Data Type
            this_column.append(length) #Length
            this_column.append("") #Precision
            this_column.append("") #scale
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif timestamp_search is not None:
            this_column = []
            timecolumn1 = timestamp_search.group(1)
            column_str = table_str + "." + timecolumn1
            this_column.append(timecolumn1) #column Name
            this_column.append("date") #Data Type
            this_column.append("") #Length
            this_column.append("") #Precision
            this_column.append("") #scale
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif integer_search is not None:
            this_column = []
            integer_column_name = integer_search.group(1)
            column_str = table_str + "." + integer_column_name
            this_column.append(integer_column_name) #column Name
            this_column.append("integer") #Data Type
            this_column.append("") #Length
            this_column.append("32") #Precision
            this_column.append("0") #scale
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        elif shape is not None:
            this_column = []
            shape_column_name = shape.group(1)
            column_str = table_str + "." + shape_column_name
            this_column.append(shape_column_name) #column Name
            this_column.append("geometry") #Data Type
            this_column.append("") #Length
            this_column.append("") #Precision
            this_column.append("") #scale
            column_comment_out = get_column_comments(column_str, file_content)
            this_column.append(column_comment_out) #Description
            this_table_columns.append(this_column)

        # temporary



    return this_table_columns

schema_out = get_schema()

schema_list_out, schema_tabulate_list_out = get_tables(schema_out)

print "schema_tabulate_list_out: ", schema_tabulate_list_out