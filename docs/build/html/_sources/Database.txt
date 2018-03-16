Database Schema
======================

.. toctree::
   :maxdepth: 2






{% for tablename in outputschema %}
* Table: {{ tablename['table'] }}
    Columns: {{ tablename['columns'] }}
{% endfor %}

Some text


