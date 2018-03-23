Database Schema
======================

.. toctree::
   :maxdepth: 2


{% block body %}
{% for schema_item in outputschema %}
	<li>**Schema Name: {{ schema_item["name"] }}**</li>
	<li>**Schema Comment: {{ schema_item["schemacomment"] }}**</li>
{% endfor %}
{% endblock %}


{% for table in something %}
{{ table["name"] }}
{{ table["description"] }}
{% endfor %}


