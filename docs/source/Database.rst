Database Schema
======================

.. toctree::
   :maxdepth: 2






{% for tablename in outputschema: %}
* Table: {{ tablename['table'] }}
    {% for columns in tablename['columns]: %}
      {% col = column.get('name') %} 
      Columns: {{ col }}
    {% endfor %}








{% endfor %}

Some text


