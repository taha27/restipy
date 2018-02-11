from http import HTTPStatus
from api import app, database
from flask import jsonify, abort, make_response

# Decorator for the view function to return a information for a specific company
@app.route('/companies/<string:company_id>', methods=['GET'])
def read_company(company_id):
    """
    Read one company's details
    """
    # Get the companies collection from the database
    company_collection = database()

    # Get the document for the company with the specified id
    company = company_collection.find_one({'_id': company_id}, {'_id': 0})

    # Throw the appropriate error if the company id was not found
    if not company:
        not_found_msg = f"Company with id '{company_id}' does not exist in the database."
        abort(make_response(jsonify(message=not_found_msg), HTTPStatus.NOT_FOUND))

    # Return company as JSON
    return jsonify(company)
