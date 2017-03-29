import time
from enum import Enum

from missile_launcher.usb_device import USBDevice

class Action(Enum):
    UP = 0x02
    DOWN = 0x01
    LEFT = 0x04
    RIGHT = 0x08
    FIRE = 0x10
    STOP = 0x20
    RESET = 0x50

class MissileLauncher:
    def __init__(self):
        self.usb_device = USBDevice()

    def up(self, milliseconds):
        self._move(Action.UP, milliseconds)

    def down(self, milliseconds):
        self._move(Action.DOWN, milliseconds)

    def left(self, milliseconds):
        self._move(Action.LEFT, milliseconds)

    def right(self, milliseconds):
        self._move(Action.RIGHT, milliseconds)

    def fire(self, number_of_shots=1):
        self._fire(number_of_shots)

    def stop(self):
        self._do(Action.STOP)

    def reset(self):
        self._do(Action.DOWN, 2000)
        self._do(Action.LEFT, 8000)

    def execute(self, action, argument):
        if isinstance(action, str):
            action = Action[action.capitalize()]

        if action in (Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT):
            milliseconds = argument or 100
            self._move(action, milliseconds)
        elif action is Action.FIRE:
            number_of_shots = argument or 1
            self._fire(number_of_shots)
        elif action is Action.RESET:
            self.reset()
        else:
            self._do(action)

    def _move(self, action, milliseconds):
        milliseconds = _clip(milliseconds, 0, 10000)
        self._do(action)
        time.sleep(milliseconds / 1000)
        self._do(Action.STOP)

    def _fire(self, number_of_shots):
        number_of_shots = _clip(number_of_shots, 1, 4)
        time.sleep(0.5)
        for _ in range(number_of_shots):
            self._do(Action.FIRE)
            time.sleep(4)

    def _do(self, action):
        self.usb_device.send_command(action.value)


def _clip(value, min, max):
    if value < min:
        value = min
    elif value > max:
        value = max

    return value