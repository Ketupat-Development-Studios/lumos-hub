import json
from flask import Flask
from flask_sockets import Sockets
from constants import ActionTypes

app = Flask(__name__)
sockets = Sockets(app)


def send_sample_action(ws):
    action = {
        "id": 1,
        "type": "action",
        "device_id": 101,
        "action": ActionTypes.ON
    }
    ws.send(json.dumps(action))


@sockets.route('/')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send("Hello, I am server")
        send_sample_action(ws)
        print(f"received {message}")
        # ws.send()


@app.route('/')
def hello():
    # serve GUI here
    return 'Lumos Hub Interface'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    print('serving on 5000')
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
