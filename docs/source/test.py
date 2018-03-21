import os
import sys
import re
from os import path

schema_name_globvar = ''
tables = []

def get_schema_name():
    script_file_path = path.dirname(__file__)
    print script_file_path
    # The path of this python script is:
    # home/jducnuigeen/dev/building_outlines_test/docs/source
    # the path of the sql file is:
    # home/jducnuigeen/dev/building_outlines_test/sql/
    sql_file_path = path.abspath(path.join(script_file_path, "..", "..", "../building_outlines_test/sql/01-create_buildings_schema.sql"))
    with open(sql_file_path) as f:
        for line in f:
            schemaname = re.search(r"(?:CREATE SCHEMA IF NOT EXISTS)\s(.*)(;)", line)
            # table = re.search(r"(?:CREATE TABLE IF NOT EXISTS)\s()", line)
            table_lg = re.search(r"(?:CREATE TABLE IF NOT EXISTS)\s(.*)(\()", line)
            if schemaname:
                schema = schemaname.group(1)
                schema_name_globvar = schema
                print "Schema Name: ", schema
    f.close()

get_schema_name()