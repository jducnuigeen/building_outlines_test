import os
import sys
import re
from os import path
from itertools import takewhile

schema_name_globvar = ''


def get_schema_name():
    # The path of this python script is:
    # home/jducnuigeen/dev/building_outlines_test/docs/source
    # the path of the sql file is:
    # home/jducnuigeen/dev/building_outlines_test/sql/
    schema_general = {}
    schema_list = []
    table_dict = {}
    sql_file_path = "./sql_not_final_location/02-buildings_schema.sql"
    with open(sql_file_path) as full_file:
        file_content = full_file.read()
    full_file.close()

    with open(sql_file_path) as f:
        for line in f:
            print "The line being processed is: ", line
            # CREATE SCHEMA IF NOT EXISTS buildings;
            schemaname = re.search(r"(?:CREATE SCHEMA IF NOT EXISTS)\s(.*)(;)", line)
            # COMMENT ON SCHEMA buildings IS 'This schema holds all of the tables for buildings';
            schema_com_srch = re.search(r"(?:COMMENT ON SCHEMA)\s(.*)(?:IS)\s(')(.*)(')(;)", line)

            #table_name_srch = re.search(r"(CREATE TABLE IF NOT EXISTS)(?:\s)(?:.*)(?:\.)(.*)(?:\s)(?:\()", line)
            table_name_srch = re.search(r"(?<=CREATE TABLE IF NOT EXISTS )(\w+)(?:\.)([^\(\s]*)", line)


            if schemaname is not None:
                schema = schemaname.group(1)
                schema_name_globvar = schema
                print "Processing schemaname"
                print "Schema Name: ", schema
                schema_general = {}
                schema_general = {"schema_name": schema_name_globvar}
                print "schema_general: ", schema_general
            elif schema_com_srch is not None:
                schema_comment = schema_com_srch.group(3)
                schema_general['schema_com'] = schema_comment
                print "Processing schema com srch"
                print "Schema general: " , schema_general
            elif table_name_srch is not None:
                # Now perform all actions to find table name, table comment, table columns, and table comments
                # and when done add all these content to table_dict, and then finally to schema_list

                table_dict = {}  # This dict hold all the information for one table
                #create_table_line = table_name_srch.group(1)
                table_name = table_name_srch.group(2)
                print "Table Name: ", table_name

                table_dict["table_nam"]= table_name
                print "table_dict is now: ", table_dict
                table_str = schema_name_globvar + "." + table_name
                print "table_str is: ", table_str
                table_com_str = "(?<=COMMENT ON TABLE " + table_str + " IS)([^\;]*)"
                #table_com_str = "(?<=COMMENT ON TABLE buildings.use IS)[^\;]*"
                #table_com_str = "(COMMENT ON TABLE buildings.lifecycle_stage IS)"

                print "table_com_str: ", table_com_str
                table_com_srch = re.search(table_com_str, file_content, re.DOTALL)
                print "table_com_srch: ", table_com_srch
                this_table_columns = [] # this holds several lists, each list is is one column of info
                if table_com_srch is not None:
                    print "table_com_srch: ", table_com_srch
                    table_com_result = ''
                    table_com_result = table_com_srch.group(0)
                    #print "table_com_result: ", repr(table_com_result)
                    table_com_result_clean = table_com_result.replace('\r\n', '').replace("'", "")
                    #print "Cleaned: ", table_com_result_clean
                    table_dict["table_comment"] = table_com_result_clean
                    #print table_dict
                    #schema_list.append(table_dict)
                    print "table_dict is now: ", table_dict

                    # get this tables' columns
                    print "Currently this_table_columns is: ", this_table_columns
                    this_table_columns = get_columns(table_str, file_content, this_table_columns)
                    table_dict["table_columns"] = this_table_columns
                    print "table_dict is now after adding columns: ", table_dict

                elif table_com_srch is None:
                    print "table_com_srch: ", table_com_srch
                    print "table_com_srch: No table comment found"
                    table_com_result = ''
                    table_dict["table_comment"] = ""
                    print "table_dict is now: ", table_dict
                    # get the columms for this table
                    this_table_columns = get_columns(table_str, file_content, this_table_columns)
                    table_dict["table_columns"] = this_table_columns
                    print "table_dict is now after adding columns: ", table_dict
                schema_list.append(table_dict)
                print "After adding a new table, schema_list is now:", schema_list

    print "Final schema_list is: ", schema_list
    return schema_general, schema_list

    f.close()


def get_columns(table_str, file_content, this_table_columns):

    
    srch_str = r"(?<=CREATE TABLE IF NOT EXISTS " + table_str + r"\s\()[^\;]*(?=\)\;)"
    column_srch = re.search(srch_str, file_content)
    columns = column_srch.group(0)
    print "columns: ", columns
    columns_strip = [x.strip() for x in columns.split(',')]
    print "columns stripped: ", columns_strip
    for column_details in columns_strip:
        pri_key_srch = re.search(r"(.*)(?:serial PRIMARY KEY)", column_details)
        #not_null_srch_1 = re.search(r"^(.*)(?:\s)(?:integer NOT NULL)", column_details)
        char_var_srch = re.search(r"(.*)(?:\s)(?:character varying)\((.*?)\)", column_details)
        timestamp1 = re.search(r"(.*)(?:\s)(?:timestamptz)", column_details)
        integer = re.search(r"^(.*)(?:\s)(?=integer)", column_details)
        shape = re.search(r"(shape)(?:.*)(?:geometry)", column_details)

        if pri_key_srch is not None:
            this_column = []
            pri_key = pri_key_srch.group(1)
            this_column.append(pri_key) #column Name
            this_column.append("integer")  #Data Type
            this_column.append("") # Length
            this_column.append("32") #Precision
            this_column.append("0") #Scale
            this_column.append("") #Description
            this_table_columns.append(this_column)

        # if not_null_srch_1 is not None:
        #     this_column = []
        #     int_column = not_null_srch_1.group(1)
        #     this_column.append(int_column) #column Name
        #     this_column.append("integer") #Data Type
        #     this_column.append("") #Length
        #     this_column.append("32") #Precision
        #     this_column.append("0") #scale
        #     this_column.append("") #Description
        #     this_table_columns.append(this_column)

        if char_var_srch is not None:
            this_column = []
            var_column = char_var_srch.group(1)
            length = char_var_srch.group(2)
            this_column.append(var_column) #column Name
            this_column.append("varchar") #Data Type
            this_column.append(length) #Length
            this_column.append("") #Precision
            this_column.append("") #scale
            this_column.append("") #Description
            this_table_columns.append(this_column)

        if timestamp1 is not None:
            this_column = []
            timecolumn1 = timestamp1.group(1)
            this_column.append(timecolumn1) #column Name
            this_column.append("date") #Data Type
            this_column.append("") #Length
            this_column.append("") #Precision
            this_column.append("") #scale
            this_column.append("") #Description
            this_table_columns.append(this_column)

        if integer is not None:
            this_column = []
            integercol = integer.group(1)
            print "integer group 1:", integercol

            this_column.append(integercol) #column Name
            this_column.append("integer") #Data Type
            this_column.append("") #Length
            this_column.append("32") #Precision
            this_column.append("0") #scale
            this_column.append("") #Description
            this_table_columns.append(this_column)

        if shape is not None:
            this_column = []
            shapecol = shape.group(1)
            this_column.append(shapecol) #column Name
            this_column.append("") #Data Type
            this_column.append("") #Length
            this_column.append("") #Precision
            this_column.append("") #scale
            this_column.append("") #Description
            this_table_columns.append(this_column)

    return this_table_columns




schema_general, schema_list = get_schema_name()
print "schema_general is: ", schema_general
print "         "
print "schema_list is: ", schema_list