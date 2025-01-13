# Data Validation Report

## Objective
This document outlines the data validation process conducted after migrating the data from the on-premises database to AWS RDS. The goal was to ensure data integrity, consistency, and correctness.

## Validation Steps
1. **Row Count Validation**: Verified that the number of rows in the source and target databases matched after migration.
2. **Data Type and Format Checks**: Ensured that all fields had the correct data types and formats in the target database.
3. **Business Logic Validation**: Applied predefined business rules to check if the transformed data met the required standards.
4. **Cross-Referencing**: Compared sample records from the source and target databases to ensure no data corruption occurred.

## Results
- **Row Count**: Passed
- **Data Types**: Passed
- **Business Logic**: Passed
- **Cross-Referencing**: Passed

## Issues Found
- Minor discrepancies in null values, which were fixed by re-running the ETL pipeline with corrected transformations.

## Conclusion
The data migration was successful with all validations passing successfully. The migrated data was validated to be consistent and reliable.
