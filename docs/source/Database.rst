Database Schema
======================

.. toctree::
   :maxdepth: 2



{% for schema in outputschema %}
**Schema Name: {{ schema["name"] }}**
{% endfor %}

{% for schemacomment in outputschema %}
**Schema Comment: {{ schemacomment["schemacomment"] }}**
{% endfor %}


{% for table in something %}
{{ table["name"] }}
{{ table["description"] }}
{% endfor %}


