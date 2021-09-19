#!/usr/bin/python3
import os
import sys
from sys import exit

def main():
	if len(sys.argv) > 1 :
		print("creating " + sys.argv[1])
		
		if os.path.exists(os.path.expanduser('~') + "/.cache/dgitignore/") == False:
			os.system("""
			
			mkdir -p ~/.cache
			git clone https://github.com/github/gitignore ~/.cache/dgitignore/
			
			""")
		
		os.system("echo \"$(cat ~/.cache/dgitignore/" + sys.argv[1] + ".gitignore)\" > .gitignore")
	else:
		sayhelp()
def sayhelp():
	pass
	
if __name__ == "__main__":
	main()
