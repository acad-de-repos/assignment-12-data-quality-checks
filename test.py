import unittest
import pandas as pd
import numpy as np
from assignment import run_data_quality_checks

class TestDataQualityChecks(unittest.TestCase):
    def setUp(self):
        """Set up a DataFrame with data quality issues for testing"""
        data = {
            'user_id': [1, 2, 3, 1, 4],
            'email': ['a@a.com', 'b@b.com', np.nan, 'a@a.com', 'd@d.com'],
            'status': ['active', 'inactive', 'pending', 'active', 'invalid'],
            'start_date': pd.to_datetime(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-01', '2022-01-05']),
            'end_date': pd.to_datetime(['2023-01-01', '2021-01-02', '2023-01-03', '2023-01-01', '2023-01-05'])
        }
        self.df = pd.DataFrame(data)

    def test_run_data_quality_checks(self):
        """Test the data quality checks function"""
        dq_report = run_data_quality_checks(self.df)

        self.assertEqual(dq_report['null_email_check'], 1)
        self.assertEqual(dq_report['duplicate_user_id_check'], 1)
        self.assertEqual(dq_report['invalid_status_check'], ['invalid'])
        self.assertEqual(dq_report['inconsistent_date_check'], 1)

if __name__ == '__main__':
    unittest.main()
