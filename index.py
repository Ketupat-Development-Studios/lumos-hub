import websocket
import time
import _thread as thread


def on_message(ws, message):
    print(f"received: message")


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
