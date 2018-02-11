import unittest
import json
from http import HTTPStatus
from test_lib.testutils import BaseTestCase


class TestCreateCompany(BaseTestCase):
    def test_create_company_1(self):
        """
        Tests creation of a single company document in the database
        """
        company_data = {
            "_id": "sbucks",
            "headquarters": "Seattle",
            "name": "Starbucks Inc.",
        }

        resp = self.app.post('/companies', data=json.dumps(company_data),
                             content_type='application/json')
        self.assertEqual(resp.status_code, HTTPStatus.CREATED)

        # cleanup
        del_resp = self.app.delete(f'/companies/{company_data["_id"]}')
        self.assertEqual(del_resp.status_code, HTTPStatus.OK)

    def test_create_company_2(self):
        """
        Tests creation of a duplicate company document in the database
        """
        company_data = {
            "_id": "sbucks",
            "headquarters": "Seattle",
            "name": "Starbucks Inc.",
        }

        resp = self.app.post('/companies', data=json.dumps(company_data),
                             content_type='application/json')
        self.assertEqual(resp.status_code, HTTPStatus.CREATED)

        resp = self.app.post('/companies', data=json.dumps(company_data),
                             content_type='application/json')
        self.assertEqual(resp.status_code, HTTPStatus.CONFLICT)

        # cleanup
        del_resp = self.app.delete(f'/companies/{company_data["_id"]}')
        self.assertEqual(del_resp.status_code, HTTPStatus.OK)

    def test_create_company_3(self):
        """
        Tests creation of a multiple company documents in the database
        """
        companies_data = [
            {
                "_id": "sbucks",
                "headquarters": "Seattle",
                "name": "Starbucks Inc.",
            },
            {
                "_id": "salesforce",
                "headquarters": "Toronto",
                "name": "Salesforce Inc.",
            },
        ]

        resp = self.app.post('/companies', data=json.dumps(companies_data),
                             content_type='application/json')
        self.assertEqual(resp.status_code, HTTPStatus.CREATED)

        # cleanup
        for company in companies_data:
            del_resp = self.app.delete(f'/companies/{company["_id"]}')
            self.assertEqual(del_resp.status_code, HTTPStatus.OK)
