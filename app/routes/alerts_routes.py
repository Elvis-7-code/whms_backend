from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.models.alert import Alert

alert_bp = Blueprint('alert_bp', __name__)

@alert_bp.route('/alerts', methods=['GET'])
@jwt_required()
def get_alerts():
    alerts =Alert.query.filter_by(sent=False).all()
    return jsonify([{
        'id': a.id,
        'type': a.type,
        'message': a.message,
        'trigger_date': str(a.trigger_date),
        'sent': a.sent
        }
          for a in alerts
          ])