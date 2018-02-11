import unittest
# import json
from http import HTTPStatus
from test_lib.testutils import BaseTestCase

class TestReadCompany(BaseTestCase):
    """
    Test Cases class for the read_company endpoint
    """
    def test_read_company_present(self):
        """
        Tests if a company is in the database
        """
        resp = self.app.get('/companies/ibm')
        self.assertIn(b'International Business Machines', resp.data)

        # response_dict = json.loads(resp.data.decode('utf-8'))
        # assert 'Palo Alto' == response_dict['city']

    def test_read_company_missing(self):
        """
        Tests if a company is not in the database
        """
        resp = self.app.get('/companies/hooli')
        self.assertEqual(resp.status_code, HTTPStatus.NOT_FOUND)

if __name__ == '__main__':
    unittest.main()
