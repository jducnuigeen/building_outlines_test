Database Schema
======================

.. toctree::
   :maxdepth: 2



{% for schema in outputschema %}
**Schema Name: {{ schema[2]["name"] }}**
**Schema Comment: {{ schema[1]["schemacomment"] }}**
{% endfor %}


{% for table in something %}
{{ table["name"] }}
{{ table["description"] }}
{% endfor %}


