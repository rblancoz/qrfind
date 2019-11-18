"""
A sample Hello World server.
"""
import os
from flask import Flask
from functools import wraps
from flask import abort
from flask import Blueprint
from flask import jsonify, request

import functions
import base64
from flask.helpers import make_response, send_file
import io
# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "Hello World"
    return message


@app.route('/qrread')
def qrread():

    t = functions.decode_img("http://localhost:5000/qrtest")
    """Return a friendly HTTP greeting."""
    message = "Hello World"
    return message


@app.route('/qrtest')
def qrtest():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    img_path = dir_path + '/qrtest.jpg'
    f3 = open(img_path, "rb")
    img_base64 = f3.read()
    f3.close()

    byte_io = io.BytesIO()
    byte_io.write(img_base64)
    byte_io.seek(0)

    response = make_response(send_file(byte_io, mimetype='image/jpg'))
    response.headers['Content-Transfer-Encoding'] = 'base64'
    return response


@app.route("/barcode/read", methods=['POST'])
def barcode_img_base64():
    # print(request.data)
    data = request.get_json()
    try:
        img_base64 = data["img_b64"]
        code = functions.decode_img_base64(img_base64)
        code = "".join(map(chr, code))
        result = {
            "code": code,
        }
    except Exception as ex:

        result = {
            "code": "",
        }
        print(ex)

    result = {
        "code": code,
    }

    # html = json.dumps(result)
    # return Response(html, mimetype='application/json')
    return jsonify(dict(success=True, message="Ok", errors=[], data=result)), 200


if __name__ == '__main__':

    try:
        server_port = os.environ.get('PORT')
    except Exception as ex:
        server_port = 5000
        pass

    if server_port is None:
        print("error: PORT environment variable not set")
        exit(1)

    app.run(debug=False, port=server_port, host='0.0.0.0')
