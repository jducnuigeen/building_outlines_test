Documentation on SQL script setup for proper Read The Docs parsing
==================================================================

Purpose
-------------

This document describes the requirements for properly formatting the SQL build scripts for this dataset to allow the automated parsing of these scripts by Read The Docs system and correctly generating the tables for the Building Outlines Data Dictionary.

File Structure
------------------

The SQL build scripts:
The SQL scripts which build schema must be contained in a folder in the root repository:
-- highlight:: SQL
   /building_outlines/sql


Assumptions:
1. The line "create Tables" are not listed more than once for any one table

2. once created tables are listed their columns are not listed anywhere else other than immediately after the line "Create table"

3. Schema and table and column comments can be more than one line in the sql file, and must take the form of:
"COMMENT ON COLUMN schema.table.column IS 'comment contents';
If they are more than one line, they must have matching single quotes containing the text on each line.

4. Every schema, table, and column must have a comment.

5. SQL schema files must have the name of the schema followed by "_schema"

6. Avoid using commas in any comments

7. Numeric data types must have a space after the comma before the scale value

8. For table field comments which are foreign keys, they can either be written like 
	"Foreign key to the schema.table table", or
	"Unique identifier for the schema.tablename table and foreign key to the schema.table table."
	The important part for the parsing script is the "foreign key to the " followed by "table", and the schema/table part must be separated by a period.

9. The in order for the parsing linking to work, the names of the schema must be known in advance, and rst pages setup in advance according
to the names of the schema. This must be hard coded into the index file, and appropriate links to pages setup. Therefore, the linking in item 8 above requires
you to know the URL of the path to the appropriate schema pages in advance.

10. 

