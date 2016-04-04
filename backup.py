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
from backupitem import Backupitem
from backupdestination import Backupdestination
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
        self.__backup_items = []
        self.__backup_destinations = []

        for item in settings.BACKUP_ITEM:
            new_item = Backupitem(item[0], item[1])
            self.__backup_items.append(new_item)

        for dest in settings.BACKUP_DEST:
            new_dest = Backupdestination(dest[0], dest[1])
            self.__backup_destinations.append(new_dest)

    def __welcome(self):
        app_notify(True, "Starting the backup.")

    def start(self):
        self.__welcome()


if __name__ == '__main__':

    my_backup = Backup()
    my_backup.start()
