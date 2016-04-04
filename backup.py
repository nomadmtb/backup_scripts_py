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

import settings
from backupitem import Backupitem
from backupdestination import Backupdestination
import shutil

# Some boiler-plate functions to standardize output for the program
# app_notify >>> use as an FYI
# app_panic >>> use when you need to get the heck out
def app_notify(status, message):
    stat = "OKAY" if status else "WARN"
    text = "{0} > {1}".format(stat, message)
    print(text)

def app_panic(message):
    text = "ERROR > {0}".format(message)
    print(text)
    exit(1)

# Backup class that will contain our backup items and destinations
class Backup:

    def __init__(self):
        self.__backup_items = []
        self.__backup_destinations = []

        # Load our backup items from settings
        for item in settings.BACKUP_ITEM:
            new_item = Backupitem(item[0], item[1], item[2])
            self.__backup_items.append(new_item)

        # Load our backup destinations from settings
        for dest in settings.BACKUP_DEST:
            new_dest = Backupdestination(dest[0], dest[1])
            self.__backup_destinations.append(new_dest)

    # Display a simple welcome message
    def __welcome(self):
        app_notify(True, "Backing up the files...")


    # Loop through the items and destinations and call the appropriate shutil
    # method based on the item type. Append the item alias with the new_path
    # to get the full new_path for the copy2/copytree method.
    def __initiate_backup(self):
        for item in self.__backup_items:
            for dest in self.__backup_destinations:
                if dest.is_valid and item.is_valid:
                    app_notify(True, "Copying {0}".format(item.path))
                    if item.is_directory():
                        shutil.copytree(item.path, "{0}/{1}".format(
                            dest.new_path, item.alias))
                    else:
                        shutil.copy2(item.path, "{0}/{1}".format(
                            dest.new_path, item.alias))

    # Exection starts here for the backup.
    def start(self):
        self.__welcome()
        self.__initiate_backup()


# Main function starts here
if __name__ == '__main__':

    my_backup = Backup()
    my_backup.start()
