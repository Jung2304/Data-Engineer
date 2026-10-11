{%- set apples = ["Gala", "Fuji", "Honeycrisp", "Granny Smith", "Red Delicious"] -%}

{% for a in apples %}
  {% if a != "Gala" %}
    {{ a }}
  {% else %}
    I hate {{ a }}
  {% endif %}
{% endfor %}