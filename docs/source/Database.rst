Database Schema
======================

.. toctree::
   :maxdepth: 2


{% block body %}
{% for schema_item in outputschema %}
**Schema Name: {{ schema_item["name"] }}**
**Schema Comment: {{ schema_item["schemacomment"] }}**
{% endfor %}
{% endblock %}


{% for table in something %}
{{ table["name"] }}
{{ table["description"] }}
{% endfor %}


