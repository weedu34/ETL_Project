import random
import pandas as pd
from faker import Faker
from google.cloud import storage
import os
import string
import csv

# Set Google Cloud credentials
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:/MS_MT/Project/GCP_ETL/prefab-kit-453822-q4-d57d426fc02e.json"

# Create Faker instance
fake = Faker()
Faker.seed(42)  # Ensures reproducibility

num_employees = 100
# Define password characters
password_characters = string.ascii_letters + string.digits + 'm'

# Generate employee data and save it to a CSV file
with open('employee_data.csv', mode='w', newline='') as file:
    fieldnames = ['first_name', 'last_name', 'job_title', 'department', 'email', 'address', 'phone_number', 'salary', 'password']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for _ in range(num_employees):
        writer.writerow({
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "job_title": random.choice(["HR Manager", "Civil Engineer", "Marketing Manager", "Sales Manager", "Finance Manager", "IT Manager"]),
            "department": random.choice(["HR", "Engineering", "Marketing", "Sales", "Finance", "IT"]),  # Generate department-like data using the job() method
            "email": fake.email(),
            "address": fake.city(),
            "phone_number": fake.phone_number(),
            "salary": fake.random_number(digits=5),  # Generate a random 5-digit salary
            "password": ''.join(random.choice(password_characters) for _ in range(8))  # Generate an 8-character password with 'm'
        })

# Upload the CSV file to a GCS bucket
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f'File {source_file_name} uploaded to {destination_blob_name} in {bucket_name}.')

# GCS bucket details
bucket_name = "bkt-testemployee-data"
source_file_name = 'employee_data.csv'
destination_blob_name = 'employee_data.csv'

upload_to_gcs(bucket_name, source_file_name, destination_blob_name)

print("✅ Fake employee data generated and uploaded to GCS.")
