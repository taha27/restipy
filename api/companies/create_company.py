import sys
from http import HTTPStatus
from api import app, database
from flask import jsonify, request, abort

def check_and_insert(company):
    """
    Inserts the supplied company record if it doesnt already exists
    """
    # Get the companies collection from the database
    company_collection = database()

    # Check if a company document already exists with the id provided and throw HTTP error if so
    company_in_db = company_collection.find_one({'_id': company['_id']}, {'_id': 0})
    if company_in_db:
        print(f"Company with id '{company['_id']}' already exists in the database.")
        abort(HTTPStatus.CONFLICT)

    # Insert the posted company json body as a document in the database
    company_collection.insert_one(company)

@app.route('/companies', methods=['POST'])
def create_company():
    """
    Creates a new company
    """
    # Get the posted data
    companies_json = request.get_json()

    # Check if the json only contains a single company document
    if '_id' in companies_json:
        check_and_insert(companies_json)
    # Iterate and insert each company document if there are multiple documents
    else:
        for company in companies_json:
            check_and_insert(company)

    # Return the created company as JSON
    return jsonify(companies_json), 201
