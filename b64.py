#!/usr/bin/env python

import base64
import argparse
import pyperclip


#Handle Command Line Parameters 
parser = argparse.ArgumentParser(description="Settings to for Encoder/Decoder")

#Parse Options
parser.add_argument("string", help="String to decode")
parser.add_argument("-e", "--encode", help="encode the string", action="store_true")
parser.add_argument("-c", "--copy", help="Copy the decoded string to the clipboard", action="store_true")

args = parser.parse_args()
thestring = ""

if args.encode == True:
    thestring = base64.b64encode(args.string)
else:
    thestring = base64.b64decode(args.string)

print ""
print thestring

if args.copy:
    pyperclip.copy(thestring)

