# Kyle Luce
# 4/3/2016
# backupitem.py
# DESC: This class will represent an item that the backup program needs to
# backup. They can either be files or directories.
#------------------------------------------------------------------------------

from os import path

class Backupitem:

    def __validate(self):
        item_result = False

        if self.type == "dir":
            item_result = path.exists(self.path)
        elif self.type == "file":
            item_result = path.isfile(self.path)

        return item_result

    def __init__(self, path, type):
        self.type = type
        self.path = path
        self.is_valid = self.__validate()
