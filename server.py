from flask import Flask
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send("Hello, I am server")
        print(f"received {message}")
        # ws.send()


@app.route('/')
def hello():
    return 'Lumos Hub Interface'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    print('serving on 5000')
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()