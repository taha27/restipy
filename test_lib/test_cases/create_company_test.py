import unittest
from http import HTTPStatus
from test_lib.testutils import BaseTestCase

class TestCreateCompany(BaseTestCase):
    def test_create_company_1(self):
        """
        Tests creation of a single company document in the database
        """
        resp = self.app.post('/companies')
        self.assertEqual(resp.status_code, HTTPStatus.CREATED)

    def test_create_company_2(self):
        """
        Tests creation of a duplicate company document in the database
        """
        resp = self.app.post('/companies')
        self.assertEqual(resp.status_code, HTTPStatus.CONFLICT)

    def test_create_company_3(self):
        """
        Tests creation of a multiple company documents in the database
        """
        resp = self.app.post('/companies')
        self.assertEqual(resp.status_code, HTTPStatus.CREATED)
