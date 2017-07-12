import unittest
import json
from api.lib.testutils import BaseTestCase

class TestReadCompany(BaseTestCase):
    def test_read_company(self):
        resp = self.app.get('/companies/exponential')

        # response_dict = json.loads(resp.data.decode('utf-8'))
        # assert 'Palo Alto' == response_dict['city']
        assert b'Palo Alto' in resp.data

if __name__ == '__main__':
    unittest.main()
