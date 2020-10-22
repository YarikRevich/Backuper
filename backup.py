import os
import subprocess
import sys


DIRTOCPFROM = sys.argv[1]
DIRTOCPTO = sys.argv[2]

def copyfiles():
    pipe = subprocess.Popen(["ls"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    stdout, _ = pipe.communicate()
    _, path = DIRTOCPTO.split("/")
    os.mkdir(DIRTOCPTO) if path not in stdout.decode() else None
    _, dirs, files = [elems for elems in os.walk(DIRTOCPTO)][0]
    subprocess.call([f"rm -r {DIRTOCPTO}/*"], shell=True) if dirs or files else None
    subprocess.call([f"cp -r {DIRTOCPFROM} {DIRTOCPTO}"], shell=True)

if __name__ == "__main__":
    if "--help" in sys.argv:
        print("You have to put two params\n::The first one is from I should copy\::The second one is that place where it will be saved")
    else:
        copyfiles()
