"""
Create and configure a Flask server
"""
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient('localhost', 27017)
    companies_db = client.companies_database
    return companies_db

# Fake company database
# def database():
#     """
#     Represents and returns a datastore of company information
#     """
#     return {
#         "exponential": {
#             "name": "Exponential.io",
#             "city": "Palo Alto"
#         },
#         "ibm": {
#             "name": "International Business Machines",
#             "city": "New York"
#         }
#     }

def database():
    """
    Get database info from mongodb test database
    """
    db = get_db()

    sample_company_data = {
        "exponential": {
            "name": "Exponential.io",
            "city": "Palo Alto"
        },
        "ibm": {
            "name": "International Business Machines",
            "city": "New York"
        }
    }

    for key, value in sample_company_data.items():
        db.companies.insert({key: value})

    # return db.test.find

# Routes stored in CRUD pattern
from api.companies import create_company
from api.companies import read_company
from api.companies import read_companies
