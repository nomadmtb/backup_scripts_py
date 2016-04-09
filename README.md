<pre>
_   ,--()            Make sure you back it up!
( )-'-.------|>
"     `--[]          github.com/nomadmtb/backup_scripts_py
</pre>


# Backup Scripts - Python
Python implementation of my backup scripts for my personal computer.
Original bash version can be found [HERE](https://github.com/nomadmtb/backup_scripts)

*Please feel free to fork/modify it for your own use.*

## PLEASE NOTE
Before using the back-up scripts, you need to configure them via the settings.md file. This file will contain two lists of tuples (BACKUP_ITEM, BACKUP_DEST). There you can set what files/directories get backedup along with the destination(s).

[settings.py](https://github.com/nomadmtb/backup_scripts_py/blob/master/settings.py)
```python
# This is the stuff that we are backing up...
BACKUP_ITEM = [
   ('/Users/kgluce/.ssh', 'dir', 'SSH_DATA'),
   ('/Users/kgluce/Documents/git','dir', 'GIT_DATA'),
   ('/Users/kgluce/Documents/personal','dir', 'PERSONAL_DATA'),
   ('/Users/kgluce/Documents/csuchico','dir', 'CSUCHICO_DATA'),
   ('/Users/kgluce/.bash_profile','file', 'BASH_PROFILE'),
]

# This is where we are putting it...
BACKUP_DEST = [
   ('/Volumes/USB/macbookair_backups', '%Y-%m-%d_%H_%M_%S'),
]
```

## How do I run this damn thing?
To run the backup after you configure the settings.py, just run the backup.py file.
<pre>
(backup_env)Kyles-Air$ python backup.py
</pre>
