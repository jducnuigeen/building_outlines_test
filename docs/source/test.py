import os
import sys
import re
from os import path

schema_name_globvar = ''


def get_schema_name():
    # The path of this python script is:
    # home/jducnuigeen/dev/building_outlines_test/docs/source
    # the path of the sql file is:
    # home/jducnuigeen/dev/building_outlines_test/sql/
    schema_dict = {}
    sql_file_path = "./sql_not_final_location/01-create_buildings_schema.sql"
    with open(sql_file_path) as f:
        for line in f:
            # CREATE SCHEMA IF NOT EXISTS buildings;
            schemaname = re.search(r"(?:CREATE SCHEMA IF NOT EXISTS)\s(.*)(;)", line)
            # COMMENT ON SCHEMA buildings IS 'This schema holds all of the tables for buildings';
            schema_com_srch = re.search(r"(?:COMMENT ON SCHEMA)\s(.*)(?:IS)\s(')(.*)(')(;)", line)

            table_lg = re.search(r"(?:CREATE TABLE IF NOT EXISTS)\s(.*)(\()", line)
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
        #print schema_dict
        schema_list = [schema_dict]
        print schema_list
        return schema_list

    f.close()

schema_list = get_schema_name()
