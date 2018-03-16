Public Database Schema
======================

.. toctree::
   :maxdepth: 2






{% for tablename in outputschema %}
* Table: {{ tablename['table'] }}
    {% for primarykey in outputschema: %}
      {{ primarykey['primary_key'] }}
      {% endfor %}
{% endfor %}

Some text


