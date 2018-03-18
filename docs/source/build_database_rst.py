import re
import sys
schema_globvar = ''
tables = {}

def main(args):

	with open('01-create_building_schema.sql') as f:
		for line in f:
			schemaname = re.search(r"(?:CREATE SCHEMA IF NOT EXISTS)\s(.*)(;)", line)
			# table = re.search(r"(?:CREATE TABLE IF NOT EXISTS)\s()", line)
			table_lg = re.search(r"(?:CREATE TABLE IF NOT EXISTS)\s(.*)(\()", line)
			if schemaname:
				schema = schemaname.group(1)
				schema_globvar = schema
				print "Schema Name: ", schema
			if table_lg:
				print 'Table match found: ', table_lg.group(1)
				table_str = table_lg.group(1)
				schema, table = table_str.split(".")
				print 'Table name is: ', table
				


			else:
				print 'No match'
	f.close()

if __name__ == '__main__':
	args = sys.argv[1:]
	main(args)