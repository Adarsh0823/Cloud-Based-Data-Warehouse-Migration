import psycopg2

# Function to generate a post-migration report
def generate_report():
    conn = psycopg2.connect(
        host="your-database-host",
        database="your-database-name",
        user="your-username",
        password="your-password"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM your_table")
    row_count = cursor.fetchone()[0]
    
    with open("post_migration_report.txt", "w") as file:
        file.write(f"Post-migration report\n")
        file.write(f"Row count: {row_count}\n")
        file.write(f"Status: Migration successful\n")

    cursor.close()
    conn.close()
    print("Post-migration report generated.")

if __name__ == "__main__":
    generate_report()
