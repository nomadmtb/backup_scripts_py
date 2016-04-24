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
import multiprocessing as multi
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

# This function will get mapped when the user wantes to copy files using
# the multiprocess option when the backup initiates. Parameters for this
# will be a tuple holding the one backup_item and the other a list of
# destinations.

def copy_mp(data):
    item = data[0]

    for dest in data[1]:
        if dest.is_valid and item.is_valid:
            app_notify(True, "Copying {0}".format(item.path))
            if item.is_directory():
                shutil.copytree(item.path, "{0}/{1}".format(
                    dest.new_path, item.alias))
            else:
                shutil.copy2(item.path, "{0}/{1}".format(
                    dest.new_path, item.alias))

# Backup class that will contain our backup items and destinations
class Backup:

    def __init__(self):
        self.__backup_items = []
        self.__backup_destinations = []
        self.__mp_copy = False
        self.__cpu_count = multi.cpu_count() * 2

        # Load our mp_copy from settings
        self.__mp_copy = settings.MP_COPY

        # Load our backup items from settings
        for item in settings.BACKUP_ITEM:
            new_item = Backupitem(item[0], item[1], item[2])
            self.__backup_items.append(new_item)

        # Load our backup destinations from settings
        for dest in settings.BACKUP_DEST:
            new_dest = Backupdestination(dest[0], dest[1])
            self.__backup_destinations.append(new_dest)

    # Display a simple welcome message with some SETTINGS data
    def __welcome(self):
        app_notify(True, "backup.py - Make sure you back it up!")
        app_notify(True, "----------------------------------------")

        app_notify(True, "Loaded {0} sources and {1} destination(s) from SETTINGS".format(
            len(self.__backup_items),
            len(self.__backup_destinations)
        ))

        app_notify(True, "{0} the multiprocessing attribute from SETTINGS".format(
            "Using" if self.__mp_copy else "Not using"
        ))

        app_notify(True, "Using {0} worker processes to copy".format(
            self.__cpu_count if self.__mp_copy else 1
        ))

        app_notify(True, "----------------------------------------")
        app_notify(True, "Backing up the files...")

    # Display the goodbye messages when complete.
    def __goodbye(self):
        app_notify(True, "----------------------------------------")
        app_notify(True, "Backup completed. Goodbye.")


    # Loop through the items and destinations and call the appropriate shutil
    # method based on the item type. Append the item alias with the new_path
    # to get the full new_path for the copy2/copytree method.
    def __initiate_backup(self):
        if not self.__mp_copy:
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
        else:
            built_items = []
            for item in self.__backup_items:
                built_items.append( (item, self.__backup_destinations,) )

            copy_pool = multi.Pool(self.__cpu_count)
            copy_pool.map(copy_mp, built_items )
            copy_pool.close()
            copy_pool.join()


    # Execution starts here for the backup.
    def start(self):
        self.__welcome()
        self.__initiate_backup()
        self.__goodbye()


# Main function starts here
if __name__ == '__main__':

    my_backup = Backup()
    my_backup.start()
