

Tables
==========


Tables:

{% for item in schema_tab  %}

	Table Name: {% filter upper %} {{ item.table_nam }} {% endfilter %}
	
	Description: {{ item.table_comment }}

	{% for table in item.table_columns %}

	{{ table }}

	{% endfor %}
	      
		

{% endfor %}