#created by Alex Hapgood
#Started 02/2018
import boto3
import os
import platform
import datetime
import textwrap
import string
import random

build = 'v0.2a1'
now = datetime.datetime.now()

class payload:
    def __init__(self, version, source, lastBackup):
        self.version = version
        self.source = source
        self.lastBackup = lastBackup

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

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

#    prefs = input('Is there a prefs.txt file to import for an existing backup? y/N: ')
#    if prefs == 'y' or prefs == 'Y':
#        f = open('prefs.txt', 'r')
#        f1 = f.readlines()
#        for x in f1:
#            print(x)
#

            payloadPath = input('Enter the full filepath to the source enclosing folder or single file: ')
            id_gen_hold = id_generator()
            namer = str(id_gen_hold)

            id_gen_hold = BackupItem(payloadPath, now.isoformat())

                with open('prefs.txt', 'a') as f:
                    f.write('\n' + namer + ','+ str(id_gen_hold.version) + ',' + id_gen_hold.source + ',' + str(id_gen_hold.isSrcRemote) + ',' + id_gen_hold.target + ',' + str(id_gen_hold.isTgtRemote) + ',' + id_gen_hold.lastBackup)
                    f.close()
            elif whereTarget == 'n' or whereTarget == 'N':
                print('Remote target backup functionality has not yet been implemented... sorry.')

        elif whereSource == 'n' or whereSource == 'N':

            #if locisSrcRemote = True
                #locSrcPath = input('Enter full SSH address to source enclosing folder: ')

            #locTgtPath
            print('Remote source backup functionality has not yet been implemented... sorry.')

    else:
        print('input not recognized...')
        return -1


def payloadLocation():
    if os.path.exists(source) and os.path.isdir(source):
        print(os.listdir(source))
    else:
        print('source either does not exist or is not a folder.')

def main():
    startUp()
    init()
    getSrcStatus()

if __name__ == "__main__":
    print(main())
