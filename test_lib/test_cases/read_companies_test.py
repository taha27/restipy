import unittest
from ..testutils import BaseTestCase

class TestReadCompanies(BaseTestCase):
    """
    Test Cases class for the read_companies endpoint
    """
    def test_read_companies_1(self):
        """
        Tests if a company id is in the response
        """
        resp = self.app.get('/companies')
        self.assertTrue(b'ibm' in resp.data)

    def test_read_companies_2(self):
        """
        Tests if a company id is not in the response
        """
        resp = self.app.get('/companies')
        self.assertFalse(b'google' in resp.data)

if __name__ == '__main__':
    unittest.main()
