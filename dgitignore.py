#!/usr/bin/python3
import os
import sys
from sys import exit

def main():
	if len(sys.argv) > 1 :
		print("creating " + sys.argv[1])
		os.system("echo \"$(curl https://raw.githubusercontent.com/github/gitignore/master/" + sys.argv[1] + ".gitignore)\" > .gitignore")
	else:
		sayhelp()
def sayhelp():
	pass
	
if __name__ == "__main__":
	main()
