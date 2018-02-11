from http import HTTPStatus
from api import app, database
from flask import abort, jsonify, make_response

@app.route('/companies/<string:company_id>', methods=['DELETE'])
def delete_company(company_id):
    """
    Deletes the company document associated with the specified company id
    """
    # Get the companies collection from the database
    company_collection = database()

    # Delete the company document
    deleted_company_document = company_collection.find_one_and_delete({'_id': company_id})

    # Throw the appropriate error if the company id isn't found
    if not deleted_company_document:
        not_found_msg = f"Company with id '{company_id}' does not exist in the database."
        abort(make_response(jsonify(message=not_found_msg), HTTPStatus.NOT_FOUND))

    # Return the deleted company document as JSON
    return jsonify(deleted_company_document), HTTPStatus.OK
