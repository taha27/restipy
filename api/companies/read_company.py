from http import HTTPStatus
from api import app
from api import database
from flask import jsonify, abort

# Decorator for the view function to return a information for a specific company
@app.route('/companies/<string:company_id>', methods=['GET'])
def read_company(company_id):
    """
    Read one company's details
    """
    # Load info from database
    db = database()
    # Check if the company id specified is valid
    if company_id not in db:
        abort(HTTPStatus.NOT_FOUND)
    # Get the company specific information from the database
    company = db[company_id]

    # Return company as JSON
    return jsonify(company)
