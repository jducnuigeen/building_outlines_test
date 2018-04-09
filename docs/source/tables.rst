Tables
==========


Tables:
{% for item in outputschema  %}
	Table Name: {% filter upper %} {{ item["table_nam"] }} {% endfilter %}<br/></b>
	Description: {{ item["table_comment"] }}
	{% if item["table_columns"] %}
		
					Column Name
					Data Type
					Length
					Precision
					Scale
					Description
		{% for columns in item["table_columns"] %}
			{% for column in columns %}
			
				 {{ column }}
				 
			{% endfor %}
		{% endfor%}

		
	{% endif %}

{% endfor %}