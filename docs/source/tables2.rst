Tables
==========


Tables:
==================  ===========  ========  ===========  =======  ===================================\n
Column Name         Data Type    Length    Precision    Scale    Description\n
==================  ===========  ========  ===========  =======  ===================================\n
lifecycle_stage_id  integer                32           0        _1\n
value               varchar      40                              The stage of a buildings lifecycle.\n
==================  ===========  ========  ===========  =======  ===================================\n

{% for item in outputschema  %}
	Table Name: {% filter upper %} {{ item["table_nam"] }} {% endfilter %}
	
	Description: {{ item["table_comment"] }}

	
	{{ item["table_columns"] }}
	      
		

{% endfor %}