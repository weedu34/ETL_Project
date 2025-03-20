# GCP_ETL
## Overview
This project implements a complete Extract, Transform, Load (ETL) pipeline on Google Cloud Platform. It generates synthetic employee data, processes it through various GCP services, and presents it for analysis in Google Looker.

## Architecture
The pipeline consists of the following components:
1. **Data Generation**: Python script to create synthetic employee data
2. **Storage**: Google Cloud Storage for raw data
3. **Transformation**: Cloud Data Fusion for data transformation
4. **Data Warehouse**: BigQuery for storage and querying
5. **Visualization**: Google Looker for data analysis and visualization

## Setup

### Environment Setup

```bash
# Create and activate virtual environment 
conda create -n gcp python=3.8 
conda activate gcp 

# Install required packages 
pip install -r requirements.txt 

# Authenticate with Google Cloud 
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

### Data Generation
The `fake_data_generation.py` script creates synthetic employee data in CSV format using the Faker library.

```bash
# Generate fake employee data and upload to GCS
python fake_data_generation.py