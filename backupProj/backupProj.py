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
import string
import random

build = 'v0.1a6'
now = datetime.datetime.now()

class BackupItem:
    def __init__(self, version, source, isSrcRemote, target, isTgtRemote, lastBackup):
        self.version = version
        self.source = source
        self.isSrcRemote = isSrcRemote
        self.target = target
        self.isTgtRemote = isTgtRemote
        self.lastBackup = lastBackup

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

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

def init():
    global now
    locSrcPath = ''
    locTgtPath = ''
    locisSrcRemote = False
    locisTgtRemote = False


    prefs = input('Is there a prefs.txt file to import? y/N: ')
    if prefs == 'y' or prefs == 'Y':
            #import, read file.
        print('')
    elif prefs == 'n' or prefs == 'N':

        whereSource = input('Is source on a local disk? y/N: ')

        if whereSource == 'y' or whereSource == 'Y':

            locisSrcRemote = False
            locSrcPath = input('Enter the full filepath to the source enclosing folder: ')
            whereTarget = input('Is target on a local disk? y/N: ')

            if whereTarget == 'y' or whereTarget == 'Y':

                locTgtPath = input('Enter the full filepath to the target folder: ')
                id_gen_hold = id_generator()
                namer = str(id_gen_hold)
                id_gen_hold = BackupItem(1, locSrcPath, locisSrcRemote, locTgtPath, locisTgtRemote, now.isoformat())

                with open('prefs.txt', 'a') as f:
                    f.write('\n' + namer + ','+ str(id_gen_hold.version) + ',' + id_gen_hold.source + ',' + str(id_gen_hold.isSrcRemote) + ',' + id_gen_hold.target + ',' + str(id_gen_hold.isTgtRemote) + ',' + id_gen_hold.lastBackup)

            elif whereTarget == 'n' or whereTarget == 'N':
                print('Remote target backup functionality has not yet been implemented... sorry.')

        elif whereSource == 'n' or whereSource == 'N':

            locisSrcRemote = True
            locSrcPath = input('Enter full SSH address to source enclosing folder: ')


            locTgtPath
                print('Remote source backup functionality has not yet been implemented... sorry.')




def getSrcStatus():
    if os.path.exists(source) and os.path.isdir(source):
        print(os.listdir(source))
    else:
        print('source either does not exist or is not a folder.')

def backup(isLoc):
    return 0

def main():
    startUp()
    init()
    getSrcStatus()
if __name__ == "__main__":
    print(main())
