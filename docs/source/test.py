import sys
import os
import json
import re
from tabulate import tabulate
from os import path
import glob2
sys.path.insert(0, os.path.abspath('../../sql'))

def get_filenames():

    # read the path and file names of all of the SQL schema files in the /SQL folder
    filenames = glob2.glob("../../sql/**/*")
    for name in filenames:
        if "schema" not in name:
            filenames.remove(name)
    return filenames



files_to_read = get_filenames()



print files_to_read