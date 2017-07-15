"""
Create and configure a Flask server
"""
from pymongo import MongoClient
from flask import Flask

app = Flask(__name__)

# Fake company database
def database_dummy():
    """
    Represents and returns a datastore of company information
    """
    return {
        "exponential": {
            "name": "Exponential.io",
            "city": "Palo Alto"
        },
        "ibm": {
            "name": "International Business Machines",
            "city": "New York"
        }
    }

def database():
    """
    Represents and returns a datastore of company information
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client.restipy
    companies = db.companies
    return companies

# Routes
from api.companies import read_company
from api.companies import read_companies
