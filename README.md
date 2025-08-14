# Data Quality Checks Assignment

## Problem Description

In this assignment, you will implement a series of data quality checks on a dataset. You will write functions to verify the completeness, uniqueness, and validity of the data, and produce a report of any data quality issues found. This is a critical skill for ensuring the reliability of data used in analysis and decision-making.

## Learning Objectives

By completing this assignment, you will learn:
- How to check for null or missing values in a dataset
- How to verify the uniqueness of key columns
- How to validate data against a set of accepted values
- How to check for data consistency between columns
- How to create a data quality report

## Setup Instructions

1.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Make sure you have the following packages installed:
    -   pandas (>=1.3.0)

## Instructions

1.  Open the `assignment.py` file.
2.  You will find a function definition: `run_data_quality_checks(df)`.
3.  The function takes a pandas DataFrame as input.
4.  Your tasks are to implement the following data quality checks:
    *   **Task 1**: Check for null values in the `email` column.
    *   **Task 2**: Check for duplicate values in the `user_id` column.
    *   **Task 3**: Check if all values in the `status` column are within a predefined set of accepted values ('active', 'inactive', 'pending').
    *   **Task 4**: Check for consistency between the `start_date` and `end_date` columns (i.e., `end_date` should not be before `start_date`).
5.  The function should return a dictionary summarizing the results of the data quality checks.

## Hints

*   For Task 1, use `df['email'].isnull().sum()`.
*   For Task 2, use `df['user_id'].duplicated().sum()`.
*   For Task 3, use the `.isin()` method to check against the set of accepted values.
*   For Task 4, you can directly compare the two date columns.

## Testing Your Solution

Run the test file to verify your implementation:

```bash
python test.py
```

The tests will check:

-   That the function returns a dictionary with the correct keys
-   That each data quality check correctly identifies issues in the test data

## Expected Output

The function should return a dictionary with the following keys and values:

-   `null_email_check`: The number of null values in the `email` column.
-   `duplicate_user_id_check`: The number of duplicate user IDs.
-   `invalid_status_check`: A list of invalid status values found.
-   `inconsistent_date_check`: The number of rows with inconsistent start and end dates.

## Sample Data Format

The input DataFrame will have the following columns:

-   `user_id` (integer)
-   `email` (string)
-   `status` (string)
-   `start_date` (datetime)
-   `end_date` (datetime)

## Troubleshooting

### Common Errors

-   `TypeError`: Ensure that your date columns are in the correct datetime format before comparing them.

## Further Exploration (Optional)

*   How would you create a more detailed data quality report, including the row numbers of the problematic data?
*   Explore using a data quality framework like Great Expectations to automate these checks.
*   Can you write a function to automatically fix some of the data quality issues found (e.g., removing duplicates)?

## Resources

-   [Data Quality: What it is and Why it's Important](https://www.talend.com/resources/what-is-data-quality/)
-   [An Introduction to Data Quality with Python](https://www.datacamp.com/community/tutorials/data-quality-python)
-   [Great Expectations Documentation](https://greatexpectations.io/docs/)
