#!/usr/bin/env python
import os
import sys
import struct
from glob import iglob
#import sys
import binascii

def printf(format, *args):
   sys.stdout.write(format % args)

print("Hallo Ballo")


path ="./"
for (dirpath, dirnames, filenames) in os.walk(path):
    #print filenames
#filenames = [f for f in iglob('./*/*.DAT', recursive=True) if os.path.isfile(f)]

    for file in filenames:
        if file.endswith((".DAT")):
            f=open(os.path.join(dirpath,file),'rb')
            data = f.read()
            #print " ".join(hex(ord(n)) for n in data[0x6518:0x6520]) + "   " + file
            print binascii.hexlify(data[0x6518:0x651C]) + " " + binascii.hexlify(data[0x651C:0x6520]) + " " + dirpath + "/" + file
   
            f.closed

quit()