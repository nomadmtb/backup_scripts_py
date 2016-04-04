#
#        _   ,--()            Make sure you back it up!
#       ( )-'-.------|>
#        "     `--[]          github.com/nomadmtb/backup_scripts_py
#

# Kyle Luce
# 4/3/2016
# backup.py
# DESC: This is the module that will contain all of the backup logic.
#------------------------------------------------------------------------------

# Import ./settings.py and shutil
import settings
from os import path
import shutil

def app_notify(status, message):
    stat = "OKAY" if status else "WARN"
    text = "{0}\t>>>\t{1}".format(stat, message)
    print(text)

def app_panic(message):
    text = "ERROR\t>>>\t{0}".format(message)
    print(text)

class Backup:

    def __init__(self):
        self.__BACKUP_ITEM = settings.BACKUP_ITEM
        self.__BACKUP_DEST = settings.BACKUP_DEST

    def __welcome(self):
        app_notify(True, "Starting the backup.")

    def __validate_dest(self):
        path_results = []
        is_bad_path = False

        for dest in self.__BACKUP_DEST:

            if path.exists(dest[0]):
                path_results.append( (dest[0], True) )
            else:
                path_results.append( (dest[0], False) )
                is_bad_path = True

        if is_bad_path:

            for status in path_results:
                msg_text = "BAD PATH" if status[1] else "VALID PATH"
                app_notify(False, "{0}, {1}".format(msg_text, status[0]))

            return False
        else:
            return True

    def start(self):

        self.__welcome()

        if not self.__validate_dest():
            app_panic("Bad dest path detected. Exiting.")

if __name__ == '__main__':

    my_backup = Backup()
    my_backup.start()
