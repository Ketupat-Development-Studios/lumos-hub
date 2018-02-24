import json
from constants import ActionTypes


class Device:
    @staticmethod
    def handle_action(action):
        SAMPLE_NEW_STATE = {
            "type": "state",
            "data": {
                "device_id": 101,
                "value": ActionTypes.ON
            }
        }

        # if sending action to device fails, return an error
        SAMPLE_ERROR = {
            "type": "error",
            "data": {
                "code": 999, # come up with some error code
                "message": "Lost bluetooth connection with device",
                "device_id": 101,
                "action_id": 1
            }
        }

        if action == ActionTypes.ON:
            # turn device on
            return  # new state
        elif action == ActionTypes.OFF:
            # turn device off
            return  # new state
        elif action == ActionTypes.TOGGLE:
            # toggle device
            return  # new state
        else:
            raise BaseException(f"unexpected action: {json.dumps(action)}")
