# Cloud-Based Data Warehouse Migration

## Project Overview
This project focuses on migrating an on-premises database system to a cloud-based data warehouse using AWS services. The primary objective of this migration was to enhance scalability, improve accessibility, and streamline data processing. By leveraging AWS (RDS, S3) for storage and PostgreSQL for database management, we were able to modernize the infrastructure and improve operational efficiency. The migration was executed using ETL pipelines built in Databricks, ensuring seamless data transfer and integrity.

## Technologies Used
- **AWS**: RDS (Relational Database Service), S3 (Simple Storage Service)
- **PostgreSQL**: Database Management System for handling the data storage and queries.
- **Databricks**: A unified data analytics platform used to build ETL pipelines for transforming and loading data.
- **Python**: Scripting language used to handle data validation and migration processes.

## Features
- **ETL Pipelines**: Utilized Databricks to extract data from the on-premises database, transform it according to business logic, and load it into AWS RDS.
- **Data Validation**: Ensured the integrity and consistency of data post-migration through rigorous validation scripts.
- **Migration Documentation**: Detailed step-by-step plan and architecture documentation to support a smooth migration process.

## Setup Instructions
To get started with this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Cloud-Based-Data-Warehouse-Migration.git
## Install required dependencies for the ETL pipeline:

pip install -r ETL-Pipelines/requirements.txt

## Configure AWS credentials in config/aws_config.json:

{
  "aws_access_key_id": "your-access-key",
  "aws_secret_access_key": "your-secret-key",
  "region_name": "your-region"
}

## Configure PostgreSQL credentials in config/postgres_config.json:

{
  "host": "your-database-host",
  "port": "5432",
  "user": "your-username",
  "password": "your-password",
  "database": "your-database-name"
}

## Usage
To run the ETL pipeline, execute the following command:

python ETL-Pipelines/databricks_etl.py

For post-migration validation:

python Scripts/data_validation_script.py
