import unittest
from api.lib.testutils import BaseTestCase

class TestReadCompanies(BaseTestCase):
    def test_read_companies(self):
        resp = self.app.get('/companies')
        assert b'ibm' in resp.data

if __name__ == '__main__':
    unittest.main()
