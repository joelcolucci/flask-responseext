from flask import Flask

from flask_responseext import Response as ResponseExt
from flask_responseext import status


app = Flask(__name__)


@app.route('/status')
def get_status():
    return ResponseExt().set_status(status.OK)


@app.route('/content')
def get_content():
    content = 'hello, world'
    return ResponseExt(content)


@app.route('/json')
def get_json():
    payload = {
        'hello': 'world'
    }

    return ResponseExt(payload).to_json()


@app.route('/headers')
def get_headers():
    headers = {
        'X-Test-Header': 'header value'
    }

    return ResponseExt().set_headers(headers)