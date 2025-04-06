# ========== Airflow ==========
airflow-init:
	cd docker/airflow && docker compose up airflow-init

airflow-up:
	cd docker/airflow && docker compose up -d

airflow-down:
	cd docker/airflow && docker compose down

# ========== Data Ingestion ==========
upload-gcs:
	python data_ingestion/upload_to_gcs.py

# ========== dbt ==========
dbt-build:
	cd dbt/weather_dbt && dbt build

dbt-test:
	cd dbt/weather_dbt && dbt test

dbt-debug:
	cd dbt/weather_dbt && dbt debug

# ========== Local Setup ==========
install-requirements:
	pip install -r requirements.txt

# ========== Clean ==========
clean:
	find . -name __pycache__ -exec rm -rf {} +

# ========== Full Pipeline ==========
all: airflow-init airflow-up upload-gcs dbt-build
