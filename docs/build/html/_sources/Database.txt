Database Schema
======================

.. toctree::
   :maxdepth: 2






{% for tablename in outputschema %}
* Table: {{ tablename['table'] }}
    {% for key in outputschema['primary_key']: %}
      {{ primarykey['primary_key'] }}
    {% endfor %}
{% endfor %}

Some text


