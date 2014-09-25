import re
import sys
from os import listdir, makedirs
from os.path import isfile, join

#MYPATH = "output/fshare2/IntentResults"
PATTERN = ".*(com/google|android/support/v4).*\n"

MYPATH = sys.argv[1]

def filter(folder, file):
    f = open(join(folder,file), "r+b")
    f_content = f.read()
    f_content = re.sub(PATTERN, r'', f_content)
    f.seek(0)
    f.truncate()
    f.write(f_content)
    f.close()

def listAllFiles(folder):
    for item in listdir(folder):
        if isfile(join(folder, item)):
            filter(folder, item)
        else:
            listAllFiles(join(folder, item))

listAllFiles(MYPATH)