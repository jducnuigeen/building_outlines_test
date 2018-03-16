Public Database Schema
===============

.. toctree::
   :maxdepth: 2


.. raw:: html


{<table>}

{% for tablename in outputschema %}
* {{ tablename['table'] }}
  {% for columnname in outputschema %}
    {{columnname['columns']}}

  {% endfor %}
{% endfor %}

Some text


