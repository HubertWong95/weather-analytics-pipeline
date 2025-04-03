from google.cloud import storage
import os

def upload_to_gcs(bucket_name, source_file_path, destination_blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path)
    print(f"File {source_file_path} uploaded to {destination_blob_name}.")

if __name__ == "__main__":
    bucket_name = "weather-analytics-bucket"
    local_file = "data_ingestion/raw/weather_data.csv"
    gcs_file = "raw/weather_data.csv"

    upload_to_gcs(bucket_name, local_file, gcs_file)
