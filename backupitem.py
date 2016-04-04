#
#        _   ,--()            Make sure you back it up!
#       ( )-'-.------|>
#        "     `--[]          github.com/nomadmtb/backup_scripts_py
#

# Kyle Luce
# 4/3/2016
# backupitem.py
# DESC: This class will represent an item that the backup program needs to
# backup. They can either be files or directories.
#------------------------------------------------------------------------------

from os import path

class Backupitem:

    # _validate will return true/false depending on if the item that is being
    # requested for backup exists or not. Want to track so we don't try to copy
    # files that don't exist. Just a quick spot check and putting logic here.
    @staticmethod
    def __validate(item_type, item_path):
        item_result = False

        if item_type == "dir":
            item_result = path.exists(item_path)
        elif item_type == "file":
            item_result = path.isfile(item_path)

        return item_result


    # Little wrapper function to check and see if the item is a directory or not
    def is_directory(self):

        if self.type == "dir":
            return True
        else:
            return False


    # On init we are validating on whether the file/directory exists or not.
    # >>> _validate
    def __init__(self, path, type, alias):
        self.type = type
        self.path = path
        self.alias = alias
        self.is_valid = self.__validate(self.type, self.path)
