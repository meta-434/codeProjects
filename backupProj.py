#Program should:
#1. ask me where my backups are if they exist
#1b. If they don't exist, where to start putting them
#1c. This includes local directories, network locations, and remote internet locations
#2. ask me the desired backup frequency
#3. ask me if I want my backups compressed
#4. ask what threshold of disk usage requires oldest backup deletion OR
#4b. if backups should be placed somewhere else after disk is filled
import os
import platform
import datetime
import textwrap

build = 'r0.1.4a'
now = datetime.datetime.now()

lastBackup = '0000y/00m/00d 00h:00m.00s'

class BackupItem:

    def __init__(self, name, source, target, lastBackup, isRemote):
        self.version = version
        self.source = source
        self.target = target
        self.lastBackup = lastBackup
        self.isRemote = isRemote

def startUp():
    global build

    print('#' * 80)
    print('#     '' _             ______ _     _                       ______  __       ''    #\n'
          '#     ''| |      /\   / _____) |   | |                     / __   |/  |      ''    #\n'
          '#     ''| | _   /  \ | /     | |___| |_   _ ____      ____| | //| /_/ | ____ ''    #\n'
          '#     ''| || \ / /\ \| |     |  ___  | | | |  _ \    / ___) |// | | | |/ _  |''    #\n'
          '#     ''| |_) ) |__| | \_____| |   | | |_| | | | |  | |   |  /__| | | ( ( | |''    #\n'
          '#     ''|____/|______|\______)_|   |_|\____| ||_/   |_|    \_____(_)|_|\_||_|''    #\n'
          '#     ''                                   |_|                               ''    #\n'
          '#     ''                                                                     ''    #')
    print('#                                  By Alex H.                                ''  #')
    print('#' * 80)

    print('\nSystem platform is ++%s++ running release ++%s++.\n' % (platform.system(), platform.release()))
    print('current build is %s' % build)

def getUserPref():
    locSource = ''
    locisRemote = False
    locTarget = ''

    prefs = input('Is there a prefs.txt file to import? y/N: ')

    if prefs == 'y' or prefs == 'Y':
        locPrefsLoc = 

    whereSource = input('Is source on a local disk? y/N: ')
    if whereSource == 'y' or whereSource == 'Y':

        locisRemote = True
        locSource = input('Enter the full filepath to the source enclosing folder: ')

    elif whereSource == 'n' or whereSource == 'N':

        locisRemote = False
        locSource = input('Enter full SSH address to source enclosing folder: ')

    else:
        print('only y/Y or n/N please.')

    locTarget = input('Where should the folder be backed up to?: ')
    locName = input('What shoudl the backup be called?')

    locName = BackupItem(1, locSource, locTarget, now.isoformat(), locisRemote)


def getSrcStatus():
    global source
    if os.path.exists(source) and os.path.isdir(source):
        print(os.listdir(source))
    else:
        print('source either does not exist or is not a folder.')

def remoteConnection():
    return 0

def backup():
    return 0

def main():
    startUp()
    getUserPref()
    #getSrcStatus()
if __name__ == "__main__":
    print(main())
