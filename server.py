import logging
from flask import Flask, render_template
from routes import api
from service.battery import get_battery_info
from service.cache import get_movement

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route("/")
def index():
    logs = get_movement()
    battery_info = get_battery_info()
    return render_template('index.html', logs=logs, battery_info=battery_info)

if __name__ == "__main__":
    app.register_blueprint(api, url_prefix="/api")
    app.run(host="0.0.0.0", port=8080)
