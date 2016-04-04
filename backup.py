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

        for status in path_results:
            msg_text = "BAD DEST" if not status[1] else "VALID DEST"
            app_notify(status[1], "{0}, {1}".format(msg_text, status[0]))

        return not is_bad_path


    def __validate_item(self):
        item_results = []
        is_bad_item = False

        for item in self.__BACKUP_ITEM:

            if item[1] == "dir":
                if path.exists(item[0]):
                    item_results.append( (item[0], item[1], True) )
                else:
                    item_results.append( (item[0], item[1], False) )
                    is_bad_item = True

            elif item[1] == "file":
                if path.isfile(item[0]):
                    item_results.append( (item[0], item[1], True) )
                else:
                    item_results.append( (item[0], item[1], False) )
                    is_bad_item = True

        for status in item_results:
            msg_text = "BAD ITEM" if not status[2] else "VALID ITEM"
            app_notify(status[2], "{0}/{1}, {2}".format(msg_text, status[1], status[0]))

        return not is_bad_item

    def start(self):
        self.__welcome()

        if not self.__validate_dest():
            app_panic("Bad dest path detected. Exiting.")

        if not self.__validate_item():
            app_panic("Bad source item detected. Exiting.")

if __name__ == '__main__':

    my_backup = Backup()
    my_backup.start()
