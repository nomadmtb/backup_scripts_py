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
import shutil

class Backup:

    def __init__(self):
        self.__BACKUP_ITEM = settings.BACKUP_ITEM
        self.__BACKUP_DEST = settings.BACKUP_DEST

    def start(self):
        pass

if __name__ == '__main__':

    my_backup = Backup()
    my_backup.start()
