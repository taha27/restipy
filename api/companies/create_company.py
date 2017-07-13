from api import app, database
from flask import jsonify, request

@app.route('/companies', methods=['POST'])
def create_company():
    """
    Creates a new company
    """

    # Get the posted data
    company = request.get_json()

    # Insert new company into the DB
    db = database()
    db.update(company)

    # Return the created company as JSON
    return jsonify(company), 201
