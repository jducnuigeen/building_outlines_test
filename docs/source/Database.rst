Database Schema
======================

.. toctree::
   :maxdepth: 2



{% for schema_item in outputschema %}
**Schema Name: {{ schema_item["name"] }}**
{% endfor %}

{% for schema_item in outputschema %}
**Schema Comment: {{ schema_item["schemacomment"] }}**
{% endfor %}



{% for table in something %}
{{ table["name"] }}
{{ table["description"] }}
{% endfor %}


