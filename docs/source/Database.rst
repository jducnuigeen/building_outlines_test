Database Schema
======================

.. toctree::
   :maxdepth: 2



{% for schema in outputschema %}
**Schema Name: {{ schema[1]["name"] }}**
**Schema Comment: {{ schema[0]["schemacomment"] }}**
{% endfor %}


{% for table in something %}
{{ table["name"] }}
{{ table["description"] }}
{% endfor %}


