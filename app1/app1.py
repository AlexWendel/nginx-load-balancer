from flask import request, Flask
import json


app1 = Flask(__name__)


@app1.route("/")
def hello_world():
    return """<html><head><title>Gawr Gura</title></head><body><h1>Gawr Gura</h1><img src="https://dotesports.com/wp-content/uploads/2023/02/02001438/Gawr-Gura-Return-to-Streaming.png?w=1200"></body></html>"""


if __name__ == "__main__":
    app1.run(debug=True, host="0.0.0.0")
