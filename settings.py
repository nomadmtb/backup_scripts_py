# Kyle Luce
# 4/3/2016
# settings.py
# DESC: In this module please define the following configuration settings. This
# will allow the user to customize what they back up etc.
#------------------------------------------------------------------------------

# BACKUP_ITEM
# DESC: Use this List to define Tuples of items that you would like to backup.
# Please note that you need to specify if it is a directory or a regular file
# with the second position in each Tuple.
#-------------------------
# BACKUP_ITEM = [
#     ('/Users/kyle/Documents/git','dir'),
#     ('/Users/kyle/.ssh','dir'),
#     ('/Users/kgluce/.bash_profile', 'file')
#     ...
# ]
BACKUP_ITEM = [
    ('/Users/kgluce/.ssh', 'dir'),
    ('/Users/kgluce/Documents/git','dir'),
    ('/Users/kgluce/Documents/programming','dir'),
    ('/Users/kgluce/Documents/personal','dir'),
    ('/Users/kgluce/.bash_profile','file'),
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
    ('/Volumes/USB/macbookair_backups', '%Y-%m-%d_%H:%M:%S'),
    ('/Volumes/USB/macbookair_backups_2', '%Y-%m-%d_%H:%M:%S')
]
