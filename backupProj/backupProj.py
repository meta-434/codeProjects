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
import textwrap

payload = ['/home/usr/alex/folder1','/home/usr/alex/folder2']
source = 'thisisatest'
lastBackup = '0000y/00m/00d 00h:00m.00s'

def startUp():
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

def getUserPref():
    global source
    whereSource = ''
    whereSource = input('Is source on a local disk? y/N: ')
    if whereSource == 'y' or whereSource == 'Y':
        source = input('Enter the full filepath to the source enclosing folder: ')
    elif whereSource == 'n' or whereSource == 'N':
        source = input('Enter full SSH address to source enclosing folder: ')
    else:
        print('only y/Y or n/N please.')

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
    getSrcStatus()
if __name__ == "__main__":
    print(main())
