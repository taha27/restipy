"""
Create and configure a Flask server
"""
from flask import Flask

app = Flask(__name__)

# Fake company database
def database():
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

# Routes
from api.companies import read_company
from api.companies import read_companies
