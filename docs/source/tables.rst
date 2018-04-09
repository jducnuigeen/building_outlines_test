Tables
==========


Tables:
{% for item in schema_tab  %}
	Table Name: {% filter upper %} {{ item["table_nam"] }} {% endfilter %}
	Description: {{ item["table_comment"] }}
	{{ item["table_columns"] }}
	| {% if item["table_columns"] %}
	|	
					Column Name
					Data Type
					Length
					Precision
					Scale
					Description
		{% for columns in item["table_columns"] %}
			
				 | {{ column }}
				 |
		{% endfor%}

		
	{% endif %}

{% endfor %}