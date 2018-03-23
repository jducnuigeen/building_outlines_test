Database Schema
======================

.. toctree::
   :maxdepth: 2



{% for schema in outputschema %}
	{% for key, value in schema.items() %}
		**Schema Name: Key: {{ name }}**
		**Schema Comment: Value: {{"schemacomment"}}**
	{% endfor %}
{% endfor %}



{% for table in something %}
{{ table["name"] }}
{{ table["description"] }}
{% endfor %}


