from http import HTTPStatus
from api import app, database
from flask import jsonify, request, abort, make_response
from pymongo.collection import ReturnDocument

@app.route('/companies/<string:company_id>', methods=['PUT', 'PATCH'])
def update_company(company_id):
    """
    Updates the document of an existing company; only updates fields specified in json body
    """
    # Get the posted data
    company_json = request.get_json()

    # Get the companies collection from the database
    company_collection = database()

    # Update the company document in the database
    updated_company_document = company_collection.find_one_and_update(
        {'_id': company_id},
        {'$set': company_json},
        return_document=ReturnDocument.AFTER
    )

    # Throw the appropriate error if the company id isn't found
    if not updated_company_document:
        not_found_msg = f"Company with id '{company_id}' does not exist in the database."
        abort(make_response(jsonify(message=not_found_msg), HTTPStatus.NOT_FOUND))

    # Return the updated company as JSON
    return jsonify(updated_company_document), HTTPStatus.OK
