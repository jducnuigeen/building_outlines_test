Tables
==========


Tables:


{% for item in outputschema  %}
	Table Name: {% filter upper %} {{ item["table_nam"] }} {% endfilter %}
	
	Description: {{ item["table_comment"] }}

.. list-table:: Title
   :widths: 30 30 30 30 30 50
   :header-rows: 1

   {% for columns in item["table_columns"] %}
      {% for column in columns %}
      {{ column }}
      {% endfor %}
   {% endfor %}

		

{% endfor %}