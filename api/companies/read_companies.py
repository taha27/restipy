from api import app
from api import database
from flask import jsonify

# Decorator for the view function to return information for all companies
@app.route('/companies', methods=['GET'])
def read_companies():
    """
    Read all companies' details
    """
    # Build a dictionary with all company specific kv pairs
    db = database()
    companies_dict = {key: value for key, value in db.items()}

    # Read from DB and return
    return jsonify(companies=companies_dict)
