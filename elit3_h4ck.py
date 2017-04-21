import sys
from subprocess import call
import argparse


parser = argparse.ArgumentParser()
parser.parse_args()

sys.stdout = open('output.txt', 'w')
call(["ls", "-l"])