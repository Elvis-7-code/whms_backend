from flask import Blueprint, jsonify

feed_bp = Blueprint("feed", __name__)

@feed_bp.route("/feeds", methods=["GET"])
def get_feeds():
    return jsonify({"message": "Feed routes working"})
