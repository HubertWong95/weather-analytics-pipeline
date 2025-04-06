select
  location,
  round(avg(temperature_c), 2) as avg_temp_c,
  round(avg(humidity_pct), 2) as avg_humidity,
  round(avg(precipitation_mm), 2) as avg_precipitation,
  round(avg(wind_speed_kmh), 2) as avg_wind_speed
from {{ ref('stg_weather_data') }}
group by location
