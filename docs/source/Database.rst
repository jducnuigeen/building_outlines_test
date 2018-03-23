Database Schema
======================

.. toctree::
   :maxdepth: 2



{% for schema in outputschema %}
	{% for key, value in schema.items %}
		**Schema Name: Key: {{ key }}**
		**Schema Comment: Value: {{ value }}**
	{% endfor %}
{% endfor %}



{% for table in something %}
{{ table["name"] }}
{{ table["description"] }}
{% endfor %}


