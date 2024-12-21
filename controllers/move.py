import os
os.environ["DISPLAY"] = ":0"

from flask import current_app as app, request, make_response, Blueprint

moves = Blueprint("moves", __name__)

@moves.route("/action", methods=["POST", "DELETE"])
def action():
    headers = {
            'mimetype': 'application/json'
            }
    response = None
    try:
        data = request.json
        action = data["action"]

        if request.method == "POST":
            msg = f"Pressing {action}"
            app.logger.info(msg)
            response = make_response(
                {
                    "data": msg
                },
                200,
            )
        else:
            msg = f"Released {action}"
            app.logger.info(msg)
            response = make_response(
                {
                    "data": msg
                },
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
