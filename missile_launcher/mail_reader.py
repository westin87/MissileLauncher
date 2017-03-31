import imaplib

from pathlib import Path


class MailReader:
    def __init__(self):
        self._mail_server = imaplib.IMAP4_SSL('imap.gmail.com')

        try:
            self._mail_server.login("missilelaunchertc@gmail.com", "5mxTktjFu4pk")
        except imaplib.IMAP4.error:
            print("Login failed")

    def get_new_mail(self):
        """Returns the latest mail if there are any new mails since last check."""
        current_number_of_mails = self._get_number_of_mails_in_inbox()

        if self._there_are_any_new_mails(current_number_of_mails):
            return self._get_mail_number(current_number_of_mails)
        else:
            return None

    def _get_number_of_mails_in_inbox(self):
        _, data_tupple = self._mail_server.select("INBOX")
        number_of_mails = data_tupple[0]
        return number_of_mails

    @staticmethod
    def _there_are_any_new_mails(new_number_of_mails):
        new_number_of_mails = int(new_number_of_mails)
        mail_count_file = Path("/tmp/mails")

        with mail_count_file.open('r+') as file_object:
            old_number_of_mails = file_object.read()
            if old_number_of_mails == "":
                old_number_of_mails = "0"

            old_number_of_mails = int(old_number_of_mails)

            file_object.write(str(new_number_of_mails))

        return old_number_of_mails != new_number_of_mails

    def _get_mail_number(self, index):
        # Don't ask about the indexing :)
        mail_content = self._mail_server.fetch(index, '(RFC822)')[1][0][1].decode()
        return mail_content
