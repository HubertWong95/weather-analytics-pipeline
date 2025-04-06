# 🌤️ Weather Analytics Pipeline

End‑to‑end **batch** data‑engineering project that ingests, transforms, tests, and visualises a 1 million‑row synthetic weather dataset for 10 US cities.

> 🔗 **Live dashboard** (Looker Studio)  
> https://lookerstudio.google.com/reporting/33be14bf-9aff-422c-80d8-7fe0c071c9f9

---

## 🎯 Project Goals

1. Build a reproducible **batch pipeline** on GCP
2. Model the data with a proper **staging → core** dbt layer
3. Validate data quality with **dbt tests**
4. Surface insights in a **two‑tile dashboard** (categorical & time‑series)

---

## ⚙️ Tech Stack

| Layer          | Tool                                |
| -------------- | ----------------------------------- |
| Cloud          | **Google Cloud Platform**           |
| Data Lake      | **Google Cloud Storage (GCS)**      |
| Orchestration  | **Apache Airflow** (Docker Compose) |
| Warehouse      | **BigQuery**                        |
| Transformation | **dbt** (`dbt-bigquery`)            |
| Tests          | **dbt_utils** package               |
| BI             | **Looker Studio**                   |
| Code           | Python 3.8, Docker                  |

---

## 🔁 Pipeline Flow

CSV → GCS (raw) → Airflow DAG → BigQuery (weather_data) → dbt (staging → core models) → Looker Studio dashboard

---

## 🧪 Data Quality Tests

| Model                     | Column(s)                                                              | Tests                                      |
| ------------------------- | ---------------------------------------------------------------------- | ------------------------------------------ |
| `stg_weather_data`        | `location`, `date_time`                                                | `not_null`                                 |
|                           | `temperature_c`                                                        | `not_null`, `accepted_range (-50 → 60 °C)` |
| `avg_weather_by_location` | `location`                                                             | `not_null`, `unique`                       |
|                           | `avg_temp_c`, `avg_humidity`,<br>`avg_precipitation`, `avg_wind_speed` | `accepted_range` checks (realistic limits) |
| `daily_avg_temperature`   | `day`                                                                  | `not_null`, `unique`                       |
|                           | `avg_temp_c`                                                           | `accepted_range (-50 → 60 °C)`             |

All tests pass (`dbt build` ➜ **PASS 13 / FAIL 0**).

---

## 📊 Dashboard Tiles

| Tile           | Description                              | Source Table              |
| -------------- | ---------------------------------------- | ------------------------- |
| **Bar chart**  | _Average Temperature by City_            | `avg_weather_by_location` |
| **Line chart** | _Daily Average Temperature (All Cities)_ | `daily_avg_temperature`   |

Dashboard link at top of README.

---

## 🚀 Quick Start (Local)

```bash
# 0.  Clone repo & create .env with GCP creds if needed
git clone https://github.com/HubertWong95/weather-analytics-pipeline.git
cd weather-analytics-pipeline

# 1.  Build / start Airflow
make airflow-init
make airflow-up         # http://localhost:8080 (airflow/airflow)

# 2.  Upload data to GCS
make upload-gcs

# 3.  Trigger DAG in Airflow (weather_gcs_to_bq) or wait for schedule

# 4.  Run dbt models & tests
make dbt-build          # (= dbt build)

# 5.  Open Looker Studio and refresh tiles
```
