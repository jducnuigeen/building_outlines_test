Public Database Schema
===============

.. toctree::
   :maxdepth: 2


.. raw:: html


{<table>}

{% for tablename in outputschema %}
* {{ tablename['table'] }}
{% endfor %}

Some text


