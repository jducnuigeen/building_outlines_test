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
    schema_dict = {}
    table_list = []
    sql_file_path = "./sql_not_final_location/01-create_buildings_schema.sql"
    with open(sql_file_path) as full_file:
        file_content = full_file.read()
    full_file.close()

    with open(sql_file_path) as f:
        for line in f:
            # CREATE SCHEMA IF NOT EXISTS buildings;
            schemaname = re.search(r"(?:CREATE SCHEMA IF NOT EXISTS)\s(.*)(;)", line)
            # COMMENT ON SCHEMA buildings IS 'This schema holds all of the tables for buildings';
            schema_com_srch = re.search(r"(?:COMMENT ON SCHEMA)\s(.*)(?:IS)\s(')(.*)(')(;)", line)

            table_name_srch = re.search(r"(CREATE TABLE IF NOT EXISTS)(?:\s)(?:.*)(?:\.)(.*)(?:\s)(?:\()", line)
            print "table_name_search: ", table_name_srch

            if schemaname:
                schema = schemaname.group(1)
                schema_name_globvar = schema
                print "Processing schemaname"
                print "Schema Name: ", schema
                schema_dict = {}
                schema_dict = {"name": schema_name_globvar}
                print schema_dict
            elif schema_com_srch is not None:
                schema_comment = schema_com_srch.group(3)
                schema_dict['schemacomment'] = schema_comment
                print "Processing schema com srch"
                print schema_dict
            elif table_name_srch is not None:
                this_column_table = []
                create_table_line = table_name_srch.group(1)
                table_name = table_name_srch.group(2)
                print "Table Name: ", table_name

                table_list.append(table_name)
                print "table_list now: ", table_list
                #search = r"(?:CREATE TABLE IF NOT EXISTS)(?:\s)(?:.*)(?:\.)(?:"+(table_name)+r")(?:\s)(?:\()"
                #print search
                srch_str = r"(?<=" + table_name + r"\s\()[^\;]*(?=\)\;)"
                column_srch = re.search(srch_str, file_content)
                #column_srch = re.search(r"(?<=capture_method\s\()[^\;]*(?=\;)", file_content)
                columns = column_srch.group(0)
                print "columns: ", columns
                columns_strip = [x.strip() for x in columns.split(',')]
                print "columns stripped: ", columns_strip
                for column_details in columns_strip:
                    pri_key_srch = re.search(r"(.*)(?:serial PRIMARY KEY)", column_details)
                    not_null_srch_1 = re.search(r"(.*)(?:integer NOT NULL)", column_details)
                    if pri_key_srch is not None:
                        pri_key = pri_key_srch.group(1)
                        this_column_table.append(pri_key) #Column Name
                        this_column_table.append("integer")  #Data Type
                        this_column_table.append("") # Length
                        this_column_table.append("32") #Precision
                        this_column_table.append("0")  #Scale
                    elif not_null_srch_1 is not None:
                        int_column = not_null_srch_1.group(1)
                        this_column_table.append(int_column) #column Name
                        this_column_table.append("integer") #Data Type
                        this_column_table.append("") #Length
                        this_column_table.append("32") #Precision
                        this_column_table.append("0") #scale
                
                table_list.append(this_column_table)
                print "table list:", table_list




                







        #print schema_dict
        schema_list = [schema_dict]
        print schema_list
        return schema_list

    f.close()

schema_list = get_schema_name()
