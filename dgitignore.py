#!/usr/bin/python3
import os
import sys
from sys import exit

def main():
	if len(sys.argv) > 1 :
		
		if sys.argv[1] == "-l" or sys.argv[1] == "--list":
			saylist()
			exit()
		if sys.argv[1] == "-u" or sys.argv[1] == "--update":
			sayupdate()
			exit()
		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			sayhelp()
			exit()
		if sys.argv[1] == "-v" or sys.argv[1] == "--version":
			print("v0.1")
			exit()
		
		verifyifexist(sys.argv[1])
		print("Creating " + sys.argv[1])
		
		if os.path.exists(os.path.expanduser('~') + "/.cache/dgitignore/") == False:
			os.system("""
			
			mkdir -p ~/.cache
			git clone https://github.com/github/gitignore ~/.cache/dgitignore/
			
			""")
		
		#os.system("echo \"$(cat ~/.cache/dgitignore/" + sys.argv[1] + ".gitignore)\" > .gitignore")
	else:
		sayhelp()
def sayhelp():
	print("""Use:
    dgitignore <Name>
Other:
    -h or --help      help
    -v or --version   see version
    -l or --list      list available
    -u or --update    download news gitignores
    """)
def verifyifexist(gitignore):
	if os.path.exists(os.path.expanduser('~') + "/.cache/dgitignore/" + gitignore + ".gitignore"):
		print("gitignore detected")
	else:
		print("Error, " + gitignore + " gitignore not exists")
		exit()
def saylist():
	if os.path.exists(os.path.expanduser('~') + "/.cache/dgitignore/") == False:
		os.system("""
		
		mkdir -p ~/.cache
		git clone https://github.com/github/gitignore ~/.cache/dgitignore/
		
		""")
	
	files = os.listdir(os.path.expanduser('~') + "/.cache/dgitignore/")
	
	files = order(files)
	
	for i in range(len(files)):
		if ".gitignore" in files[i]:
			print(files[i][:-10])
		
	
def sayupdate():
	if os.path.exists(os.path.expanduser('~') + "/.cache/dgitignore/") == False:
		os.system("""
		
		mkdir -p ~/.cache
		git clone https://github.com/github/gitignore ~/.cache/dgitignore/
		
		""")
	else:
		os.system("""
		
		cd ~/.cache/dgitignore/
		git restore :
		git pull
		
		""")
	
def order(output):
	lenoutput = len(output)
	j = False
	i = True

	while i == True:
		i = 0
		for i in range(lenoutput):
			if i != 0:
				if output[i] < output[i-1]:
					j = True
					m = output[i-1]
					output[i-1] = output[i]
					output[i] = m
		if j == True:
			j = False
			i = True
		else:
			i = False
	
	return output

if __name__ == "__main__":
	main()
