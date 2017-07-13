import unittest
# import json
from api.lib.testutils import BaseTestCase

class TestReadCompany(BaseTestCase):
    def test_read_company(self):
        resp = self.app.get('/companies/ibm')
        assert b'New York' in resp.data

        # response_dict = json.loads(resp.data.decode('utf-8'))
        # assert 'Palo Alto' == response_dict['city']


if __name__ == '__main__':
    unittest.main()
