import logging
from flask import request, Flask, render_template
from routes import api


app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route("/")
def index():
    logs = ""
    if 'logs' in request.args:
        logs = request.args['logs']
    return render_template('index.html', logs=logs)

if __name__ == "__main__":
    app.register_blueprint(api, url_prefix="/api")
    app.run(host="0.0.0.0", port=8080)
