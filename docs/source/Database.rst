Database Schema
======================

.. toctree::
   :maxdepth: 2


Schema:
{% for schema in outputschema %}
{{ schema["name"] }}
{{ schema["description"]}}
{% endfor %}


{% for table in something %}
{{ table["name"] }}
{{ table["description"] }}
{% endfor %}


