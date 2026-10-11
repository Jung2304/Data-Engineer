{%- set inc_flag = 1 -%}
{%- set last_load_key = 3 -%}

{% set cols_list = ["sales_id", "date_sk", "gross_amount"] %}

SELECT

  {% for i in cols_list %}
    {{ i }}{% if not loop.last %}, {% endif %}
  {% endfor %}

FROM
  {{ ref("bronze_sales") }}

{% if inc_flag == 1 %}
  WHERE date_sk > {{ last_load_key }}
{% endif %}