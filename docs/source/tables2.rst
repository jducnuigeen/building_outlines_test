Tables
==========


Tables:

    ===== ============= ==================================== 
    Name  Favorite Food Favorite Subject                     
    ===== ============= ==================================== 
    Joe   Hamburgrs     I like things with really long names 
    ----- ------------- ------------------------------------ 
    Jill  Salads        American Idol                        
    ----- ------------- ------------------------------------ 
    Sally Tofu          Math                                 
    ===== ============= ====================================

{% for item in outputschema  %}
	Table Name: {% filter upper %} {{ item["table_nam"] }} {% endfilter %}
	
	Description: {{ item["table_comment"] }}

	
	{{ item["table_columns"] }}
	      
		

{% endfor %}