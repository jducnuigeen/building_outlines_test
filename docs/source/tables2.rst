Tables
==========


Tables:
==================  ===========  ========  ===========  =======  ===================================

Column Name         Data Type    Length    Precision    Scale    Description

==================  ===========  ========  ===========  =======  ===================================
lifecycle_stage_id  integer                32           0        _1
value               varchar      40                              The stage of a buildings lifecycle.
==================  ===========  ========  ===========  =======  ===================================

{% for item in outputschema  %}
	Table Name: {% filter upper %} {{ item["table_nam"] }} {% endfilter %}
	
	Description: {{ item["table_comment"] }}

	
	{{ item["table_columns"] }}
	      
		

{% endfor %}