Database Schema
======================

.. toctree::
   :maxdepth: 2


Schema:
{% for schema in outputschema %}
{{schema[outputschema]}}
{% endfor %}


{% for table in something %}
{{ table["name"] }}
{{ table["description"] }}
{% endfor %}


