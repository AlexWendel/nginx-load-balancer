from flask import request, Flask
import json

app2 = Flask(__name__)


@app2.route("/")
def hello_world():
    return """<html><head><title>Amelia Watson</title></head><body><h1>Amelia Watson</h1><img src="https://yt3.googleusercontent.com/RZ4Fp3L6_zyq6YA7s5WnH8-22iezMLwdJhtkBgs_EAb06mvMCnF59JKMNu9YPCqb7nhaeXMdPvY=s900-c-k-c0x00ffffff-no-rj"></body></html>"""


if __name__ == "__main__":
    app2.run(debug=True, host="0.0.0.0")
