from flask import jsonify

def success(message, data=None, status=200):

    response = {
        "status": "ok",
        "message": message
    }

    if data:
        response.update(data)

    return jsonify(response), status


def error(message, status=400):

    return jsonify({
        "status": "error",
        "message": message
    }), status