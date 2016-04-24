#
#        _   ,--()            Make sure you back it up!
#       ( )-'-.------|>
#        "     `--[]          github.com/nomadmtb/backup_scripts_py
#

# Kyle Luce
# 4/3/2016
# settings.py
# DESC: In this module please define the following configuration settings. This
# will allow the user to customize what they back up etc.
#------------------------------------------------------------------------------

# BACKUP_ITEM
# DESC: Use this List to define Tuples of items that you would like to backup.
# Please note that you need to specify if it is a directory or a regular file
# with the second position in each Tuple.  The last argument is the alias when
# the item is copied.
#-------------------------
# BACKUP_ITEM = [
#     ('/Users/kyle/Documents/git','dir', 'git_bak'),
#     ('/Users/kyle/.ssh','dir', 'ssh_bak'),
#     ('/Users/kgluce/.bash_profile', 'file', 'bash_profile.bak')
#     ...
# ]
BACKUP_ITEM = [
    ('/Users/kgluce/.ssh', 'dir', 'SSH_DATA'),
    ('/Users/kgluce/Documents/git','dir', 'GIT_DATA'),
    ('/Users/kgluce/Documents/personal','dir', 'PERSONAL_DATA'),
    ('/Users/kgluce/Documents/csuchico','dir', 'CSUCHICO_DATA'),
    ('/Users/kgluce/.bash_profile','file', 'BASH_PROFILE'),
]

# BACKUP_DEST
# DESC: Use this List to define Tuples where you want to copy the above files or
# directories too.  Each Tuple with also have a datetime format string for the
# destination path for the next backup.  Please note that you can have more than
# one destination in the destination specifications.
#-------------------------
# BACKUP_DEST = [
#     ('/Volumes/sandisk_backup_1/backups', '%Y-%m-%d_%H:%M:%S'),
#     ('/Volumes/sandisk_backup_2/backups', '%Y-%m-%d_%H:%M'),
#     ...
# ]
BACKUP_DEST = [
    ('/Volumes/USB/macbookair_backups', '%Y-%m-%d_%H_%M_%S'),
]

# MP_COPY
# DESC: Set this item accordingly when the user has a large amount of
# BACKUP_ITEMS.  This will create a pool of worker processes that will each copy
# a BACKUP_ITEM to the required BACKUP_DEST.  This may improve performace if
# the user has a large number of BACKUP_ITEMS that are significant in size.
#-------------------------
# MP_COPY = True
# OR
# MP_COPY = False
#
MP_COPY = True
