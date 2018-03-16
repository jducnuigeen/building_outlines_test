Public Database Schema
======================

.. toctree::
   :maxdepth: 2





{%import json %}

{% for tablename in outputschema %}
* {{ tablename['table'] }}
    {% for primarykey in outputschema: %}
      {{primarykey['primary_key']}}
      {% endfor %}
{% endfor %}

Some text


