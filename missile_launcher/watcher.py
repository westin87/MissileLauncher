import signal
from time import sleep

from missile_launcher.mail_reader import MailReader
from missile_launcher.missile_launcher import MissileLauncher


class MailWatcher:
    def __init__(self):
        self._mail_reader = MailReader()
        self._missile_launcher = MissileLauncher()
        self._should_run = False

    def start(self):
        self._should_run = True

        while self._should_run:
            new_mail = self._mail_reader.get_new_mail()
            if new_mail:
                self._missile_launcher.fire()

            sleep(10)

    def stop(self):
        self._should_run = False


def start_watcher():
    watcher = MailWatcher()
    signal.signal(signal.SIGINT, watcher.stop)
    watcher.start()


if __name__ == '__main__':
    start_watcher()