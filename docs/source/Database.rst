Database Schema
===============

.. toctree::
   :maxdepth: 2





+-----------------------------------+
|{% for tablename in outputschema %} |
|    {{ tablename['table'] }}        |
|{% endfor %}                        |
+-----------------------------------+


