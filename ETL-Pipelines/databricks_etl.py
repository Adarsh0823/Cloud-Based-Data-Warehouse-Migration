import boto3
import psycopg2
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder.appName('DataWarehouseMigration').getOrCreate()

# AWS S3 Client
s3 = boto3.client('s3')

# PostgreSQL Connection Setup
def create_pg_connection():
    conn = psycopg2.connect(
        host="your-database-host",
        database="your-database-name",
        user="your-username",
        password="your-password"
    )
    return conn

# Extract Data from PostgreSQL
def extract_data():
    conn = create_pg_connection()
    query = "SELECT * FROM your_table"
    df = pd.read_sql(query, conn)
    return df

# Transform Data (basic example)
def transform_data(df):
    spark_df = spark.createDataFrame(df)
    transformed_df = spark_df.withColumn('new_column', col('existing_column') * 2)
    return transformed_df

# Load Data into AWS RDS (PostgreSQL)
def load_data(df):
    conn = create_pg_connection()
    cursor = conn.cursor()
    for row in df.collect():
        cursor.execute("INSERT INTO your_table (column1, column2) VALUES (%s, %s)", (row['column1'], row['column2']))
    conn.commit()
    cursor.close()
    conn.close()

# Main ETL Pipeline
def run_etl():
    # Step 1: Extract data
    data = extract_data()

    # Step 2: Transform data
    transformed_data = transform_data(data)

    # Step 3: Load data to AWS RDS
    load_data(transformed_data)

if __name__ == "__main__":
    run_etl()
