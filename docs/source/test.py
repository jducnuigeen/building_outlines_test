import sys
import os
import json
import re
from tabulate import tabulate
from os import path
import glob
sys.path.insert(0, os.path.abspath('../../sql'))


def get_filenames():

    # read the path and file names of all of the SQL schema files in the /SQL folder
    filenames = []
    filenames_sorted = []
    filenames = glob.glob("../../sql/*.sql")
    str = "schema"
    for name in filenames:
        if str not in name:
            filenames.remove(name)

    filenames_sorted = sorted(filenames)
    return filenames_sorted



filenames_out = get_filenames()
print filenames_out