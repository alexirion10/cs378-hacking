import sys
from subprocess import call

sys.stdout = open('output.txt', 'w')
call(["ls", "-l"])