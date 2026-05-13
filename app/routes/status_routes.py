from flask import Blueprint, jsonify

status_bp = Blueprint("status", __name__)

@status_bp.route("/v1/status", methods=["GET"])
def status():

    return jsonify({
        "status": "ok",
        "message": "Servidor disponível"
    }), 200