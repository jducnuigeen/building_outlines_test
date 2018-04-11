
.. _tables:
{% filter upper %}
**Schema: {{ schema_gen["name"] }}**
=======================================
{% endfilter %}
**Description: {{ schema_gen["comment"] }}**

Additional Notes about this Schema
------------------------------------
* This schema is designed for specific purposes

{{ schema_gen["name"] }} Schema Details
-----------------------------------------


{% for item in schema_tab  %}

	**Table Name:** {% filter upper %} **{{ item.table_nam }}** {% endfilter %}
	
	**Description: {{ item.table_comment }}**

		{% for table in item.table_columns %}{%  for column in table %}{{ column }}{% endfor %}
		{% endfor %}
	      
		

{% endfor %}