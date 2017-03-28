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

    def execute(self, action, argument):
        if isinstance(action, str):
            action = Action[action]

        if action in (Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT):
            milliseconds = argument
            self._move(action, milliseconds)
        elif action is Action.FIRE:
            number_of_shots = argument
            self._fire(number_of_shots)
        else:
            self._do(action)

    def _move(self, action, milliseconds):
        self._do(action)
        time.sleep(milliseconds / 1000)
        self._do(Action.STOP)

    def _fire(self, number_of_shots):
        time.sleep(0.5)
        for _ in range(number_of_shots):
            self._do(Action.FIRE)
            time.sleep(4.5)

    def _do(self, action):
        self.usb_device.send_command(action.value)