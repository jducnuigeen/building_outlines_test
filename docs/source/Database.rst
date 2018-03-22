Database Schema
======================

.. toctree::
   :maxdepth: 2



{% for schema in outputschema %}
Schema Name:{{ schema["name"] }}
Description{{ schema["description"]}}
{% endfor %}

{% for schema in outputschema %}
Description{{ schema["description"]}}
{% endfor %}


{% for table in something %}
{{ table["name"] }}
{{ table["description"] }}
{% endfor %}


