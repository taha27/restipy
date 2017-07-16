from api import app
from api import database
from flask import jsonify
import pymongo

# Decorator for the view function to return information for all companies
@app.route('/companies', methods=['GET'])
def read_companies():
    """
    Read all companies' details
    """
    # Get the companies collection
    company_collection = database()

    # Get all companies' documents and assemble a list of company dictionaries
    companies_cursor = company_collection.find({})

    companies_list = [
        {
            key: value for key, value in company.items()
        }
        for company in companies_cursor
    ]

    # Read from DB and return
    return jsonify(companies=companies_list)
