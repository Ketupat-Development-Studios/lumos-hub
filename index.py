import websocket
import time
import json
import _thread as thread
from device import Device


def on_message(ws, message):
    try:
        json_object = json.loads(message)
    except ValueError:
        print(f"received: message")
        return
    if "action" in json_object:
        action_result = Device.handle_action(message)
        ws.send(json.dumps(action_result))
    else:
        # some other thing = unexpected!
        print(json_object)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("socket closed")


def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello, I am client")
        time.sleep(1)
        # ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:5000",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
