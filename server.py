'''
THIS IS A WEBSOCKETS SERVER FOR TESTING WEBSOCKET CLIENTS
'''

from flask import Flask
from flask_socketio import SocketIO, send, emit

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'supersecret'
SOCKETIO = SocketIO(APP)


@SOCKETIO.on('action')
def handle_result_action(json):
    print('received json: ' + str(json))


@SOCKETIO.on('connect')
def test_connect():
    emit('message', {'data': "Hi, I'm server"})
    emit('action', {'data': "pls turn xx switch to yy position"})
    print('Client connected')


@SOCKETIO.on('disconnect', namespace='/chat')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    # default port is 5000
    SOCKETIO.run(APP, debug=True)
