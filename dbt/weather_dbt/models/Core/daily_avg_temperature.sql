select
  date(date_time) as day,
  round(avg(temperature_c), 2) as avg_temp_c
from {{ ref('stg_weather_data') }}
group by day
order by day
