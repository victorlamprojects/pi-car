from flask import current_app as app, make_response, Blueprint
from service.battery import get_battery_info

battery = Blueprint("battery", __name__)

@battery.route('/info')
def battery_info():
    headers = {
        'content-type': 'application/json'
    }
    response = None
    try:
        response = make_response(
            get_battery_info(),
            200,
        )

    except Exception as e:
        app.logger.error(str(e))
        response = make_response(
            {
                "data": str(e)
            },
            500,
        )
    response.headers = headers

    return response
