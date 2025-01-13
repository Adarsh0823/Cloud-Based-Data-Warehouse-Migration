# Architecture Overview

## Pre-Migration Architecture
The on-premises architecture consisted of a PostgreSQL database hosted locally. Data was manually processed and stored in multiple systems, leading to challenges with data consistency, scalability, and accessibility.

## Post-Migration Architecture
The data was migrated to a cloud-based architecture using AWS services. The following components were utilized:
- **AWS RDS**: Hosted the PostgreSQL database in the cloud for better scalability and accessibility.
- **AWS S3**: Used for staging data during the ETL process.
- **Databricks**: Used to create the ETL pipelines for extracting, transforming, and loading data into AWS RDS.

## Diagram
![Architecture Diagram](architecture_diagram.png)

## Benefits of Cloud-Based Architecture
- **Scalability**: AWS RDS automatically scales the database based on load.
- **Accessibility**: Data is now accessible from anywhere, enhancing business operations.
- **Cost-Efficiency**: The cloud infrastructure provides better resource utilization, reducing operational costs.

