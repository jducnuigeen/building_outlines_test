Documentation on SQL script setup for proper Read The Docs parsing
==================================================================

Purpose
-------------

This document describes the requirements for properly formatting the SQL build scripts for this dataset to allow the automated parsing of these scripts by Read The Docs system and correctly generating the tables for the Building Outlines Data Dictionary.

File Structure
------------------

* The SQL scripts which build schema must be contained in a /sql folder in the root repository. 
* Two files are also needed in the root directory: requirements-docs.txt and setup.py.
* All other files needed for the automated Read The Docs system should be located in the /docs/source/ folders.
* The _static folder is where logos, custom css and images are stored.
* The SQL scripts which build schema must also have a name with the format "<name>_schema.sql"
* The /sql folder can contain subfolders with additional schema sql build files

.. code-block:: python

   /building_outlines/sql
   /building_outlines/requirements-docs.txt
   /building_outlines/setup.py
   /building_outlines/docs/source/
   /building_outlines/docs/source/_static



Files required
------------------

* Within the /building_outlines/docs/source/ folder, there must be an .rst file for each schema being parsed, with a name format of "<schema name>_schema.rst". 
* On the first line of each schema .rst file, there should be a line as shown here to give the file a name for referencing:

.. code-block:: python

   .. _buildings_schema:

* An index.rst file must exist with the names of the above mentioned schema .rst files listed in the toctree without the .rst extension:

.. code-block:: python

   .. toctree::
      :maxdepth: 3
      :numbered:

      introduction
      data_model
      buildings_schema
      buildings_common_schema
      buildings_bulk_load_schema
      buildings_lds_schema

* any .rst files named in the toctree above must exist in the /docs/source/ folder (ie introduction, data_model, etc)
* a conf.py file containing setup and parsing scripts must be located in the /docs/source/ folder.

Structure requirements of SQL schema build files:

1. The SQL scripts which build schema must have a name with the format "<name>_schema.sql"

1. Tables must be written with the following structure, and lines must end with an opening "(" bracket, and schema name and schema table name separated by a period:

.. code-block:: python

   CREATE TABLE IF NOT EXISTS buildings.lifecycle_stage (

2. Each table's columns must be listed in the lines immediately following the CREATE TABLE IF NOT EXISTS line, and within "()" brackets and ending with a semi-colon:

.. code-block:: rst

   CREATE TABLE IF NOT EXISTS buildings.use (
      use_id serial PRIMARY KEY
    , value character varying(40) NOT NULL
   );

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

