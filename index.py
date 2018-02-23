from socketIO_client import SocketIO, LoggingNamespace


def on_connect():
    print('connect')
    return


def on_disconnect():
    print('disconnect')
    return


def on_reconnect():
    print('reconnect')
    return


def on_message(*args):
    # generic message
    print('generic message', args)


def on_action(*args):
    # receive request to perform action (toggle switch, etc.)
    print('on_action', args)


with SocketIO('localhost', 5000, LoggingNamespace) as socketIO:
    # Connection Events
    socketIO.on('connect', on_connect)
    socketIO.on('disconnect', on_disconnect)
    socketIO.on('reconnect', on_reconnect)

    # Listen
    socketIO.on('action', on_action)
    socketIO.on('message', on_message)

    # Don't die
    socketIO.wait()

'''
socketIO = SocketIO('localhost', 5000, LoggingNamespace)

# Connection Events
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)

# Listen
socketIO.on('action', on_action)
socketIO.on('message', on_message)

# Don't die
socketIO.wait()
'''
