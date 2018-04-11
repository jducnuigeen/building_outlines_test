import sys
import os
import json
import re
from tabulate import tabulate
from os import path
import glob
sys.path.insert(0, os.path.abspath("../../sql"))

sql_file_path = "../../sql/02-buildings_schema.sql"

def read_sql():

    # read the path and file names of all of the SQL schema files in the /SQL folder
    filenames = glob.glob("../../sql/*")
    str = "schema"
    for name in filenames:
    	if str not in name:
    		filenames.remove(name)
    	



    return filenames

filenames_out = read_sql()
print filenames_out

#schema_out = get_schema()

#schema_list_out, schema_tabulate_list_out = get_tables(schema_out)

#print schema_tabulate_list_out