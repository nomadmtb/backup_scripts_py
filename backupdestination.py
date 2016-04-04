# Kyle Luce
# 4/3/2016
# backupdestination.py
# DESC: This class will represent backup destinations.
#------------------------------------------------------------------------------

from os import path

class Backupdestination:

    def __validate(self):

        return path.exists(self.path)

    def __init__(self, path, format_str):
        self.path = path
        self.format_str = format_str
        self.is_valid = self.__validate()
