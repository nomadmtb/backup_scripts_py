#
#        _   ,--()            Make sure you back it up!
#       ( )-'-.------|>
#        "     `--[]          github.com/nomadmtb/backup_scripts_py
#

# Kyle Luce
# 4/3/2016
# backupdestination.py
# DESC: This class will represent backup destinations.
#------------------------------------------------------------------------------

from os import path
from os import makedirs
from datetime import datetime

class Backupdestination:

    # This method will sanitize the format string that is supplied in the
    # settings module.  Entry point for more cleansing if needed.
    @staticmethod
    def __sanitize_format(format):
        format = format.replace(" ", "_")
        return format


    # _validate_path will determine if the destination root directory exists or
    # not.  Adding the logic here so we don't have to check elsewhere.
    def __validate_path(self):

        return path.exists(self.path)


    # Function will return the new destination path with the destination root
    # directory attached with the format string being taken into account.
    def __generate_new_path(self):

        cur_date = datetime.now()
        date_str = cur_date.strftime(self.format_str)

        return "{0}/{1}".format(self.path, date_str)

    # In our init we are checking for a sanitized format, validating the path,
    # and generating a new_path based on the format string.
    def __init__(self, path, format_str):
        self.path = path
        self.format_str = self.__sanitize_format(format_str)
        self.is_valid = self.__validate_path()
        self.new_path = self.__generate_new_path()
