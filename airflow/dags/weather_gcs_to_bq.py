from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime

default_args = {
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="weather_gcs_to_bq",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=["weather", "gcs", "bq"],
) as dag:

    load_weather_data = GCSToBigQueryOperator(
        task_id="load_gcs_to_bq",
        bucket="weather-analytics-bucket",  # ← your GCS bucket
        source_objects=["raw/weather_data.csv"],
        destination_project_dataset_table="weather-analytics-455508.weather_analytics.weather_data",
        source_format="CSV",
        skip_leading_rows=1,
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
    )
