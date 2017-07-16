"""
Create and configure a Flask server
"""
import os
import sys
from pymongo import MongoClient
from flask import Flask

# Check if the MongoDB Connection URI string is set as an environment variable
DB_URI = os.environ.get('RESTIPY_DB_URI')
if DB_URI is None:
    sys.exit('The "RESTIPY_DB_URI" environment variable could not be found.'\
             ' Please set it using the following standard URI connection scheme:\n'\
             'mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]]'\
             '[/[database][?options]]')
    # Comment out the sys.exit(...) above and uncomment the line
    # below to connect on default mongod host and port
    # DB_URI = 'mongodb://localhost:27017/'


# Create an instance of a
app = Flask(__name__)

def database():
    """
    Returns a datastore of company information
    """
    client = MongoClient(DB_URI)
    db = client.restipy
    companies = db.companies
    return companies

# Routes
from api.companies import create_company
from api.companies import read_company
from api.companies import read_companies
