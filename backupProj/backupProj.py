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
    def __init__(self, id, source, time):
        self.source = source
        self.id = id
        self.time = date

    def writeToPrefs(self):
        self.id = id_generator()
        self.now = str(now)

        with open('prefs.txt', 'a') as f:
            f.write('\n' + self.id  + ' | ' + self.source + ' | ' + self.now)
            f.close()

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

    #!!!existPrefs = bool(input)
    payloadPath = input('Enter the full filepath to the source enclosing folder or single file: ')







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
