from flask import Flask, request
from flask_cors import *
import requests

app = Flask(__name__)
CORS(app, supports_credentials=False)


def request_parse(req_data):
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data


@app.route('/', methods=["GET", "POST"])
def hello_world():  # put application's code here
    if request.method == "GET":
        return 'wallheaven接口云'
    else:
        data = request_parse(request)
        url = data.get("url")
        resp = requests.get(url).json()
        data = resp["data"]
        path_list = []
        for item in data:
            path_list.append(item["path"])
            print(item["path"])

        # age = request.form.get("age")
        # print(age)
        return {
            "path_list": path_list
        }


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="9528")

