Tables
==========


Tables:


{% for item in schema_tab  %}
	Table Name: {% filter upper %} {{ item["table_nam"] }} {% endfilter %}
	
	Description: {{ item["table_comment"] }}

	   {% for columns in item["table_columns"] %}
	      {% for column in columns %}
	      {{ column }}
	      {% endfor %}
	   {% endfor %}

		

{% endfor %}