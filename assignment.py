import pandas as pd

def run_data_quality_checks(df):
  """
  Runs a series of data quality checks on the input DataFrame.

  This function performs checks for:
  1. Null values
  2. Duplicate values
  3. Invalid values
  4. Inconsistent data

  Args:
    df: A pandas DataFrame to check.

  Returns:
    A dictionary summarizing the data quality issues found.
  """
  dq_report = {}

  # Task 1: Check for null emails
  # Your code here

  # Task 2: Check for duplicate user IDs
  # Your code here

  # Task 3: Check for invalid status values
  # Your code here

  # Task 4: Check for inconsistent dates
  # Your code here

  return dq_report
