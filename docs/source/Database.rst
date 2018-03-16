Public Database Schema
======================

.. toctree::
   :maxdepth: 2





{<table>}

{% for tablename in outputschema %}
* {{ tablename['table'] }}
	{% for columnname in outputschema %}
	  {{columnname['name']}}
	{% endfor %}
{% endfor %}

Some text


