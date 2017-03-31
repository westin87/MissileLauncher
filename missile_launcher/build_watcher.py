import signal
from time import sleep

from missile_launcher.coordinator import give_me_coords
from missile_launcher.mail_reader import MailReader, get_name_from_mail
from missile_launcher.missile_launcher import MissileLauncher


class BuildWatcher:
    def __init__(self):
        self._mail_reader = MailReader()
        self._missile_launcher = MissileLauncher()
        self._should_run = False

    def start(self):
        print("Checking the mail!")
        self._should_run = True

        while self._should_run:
            new_mail = self._mail_reader.get_new_mail()
            if new_mail:
                developer_name = get_name_from_mail(new_mail)
                coords = give_me_coords(developer_name)

                if coords:
                    self._missile_launcher.reset()
                    self._missile_launcher.up(coords[0])
                    self._missile_launcher.right(coords[1])
                    self._missile_launcher.fire()

            sleep(10)

    def stop(self, *args, **kwargs):
        self._should_run = False


def start_build_watcher():
    watcher = BuildWatcher()
    signal.signal(signal.SIGINT, watcher.stop)
    watcher.start()


if __name__ == '__main__':
    start_build_watcher()