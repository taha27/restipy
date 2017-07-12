from api import app
from api import database
from flask import jsonify

# Decorator
@app.route('/companies/<string:company_id>', methods=['GET'])
def read_company(company_id):
    """
    Read one company's details
    """

    # Read company from DB
    db = database()
    company = db[company_id]

    # Return company as JSON
    return jsonify(company)
