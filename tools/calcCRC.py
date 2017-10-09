#!/usr/bin/env python
import os
import sys
import struct
from glob import iglob
#import sys
import binascii

def printf(format, *args):
   sys.stdout.write(format % args)

    #print filenames
#filenames = [f for f in iglob('./*/*.DAT', recursive=True) if os.path.isfile(f)]

#block starts with block number and A5 A5 A5
# might be they claculate CRC block wise
bl_start=[44,11568,11868,21472,21476,21484,21500,21528,21556,21608,21780,25880]

f=open("../SHOW0011/SCENE000.DAT",'rb')
data = f.read()

# not clear where AH starts with CRC calculation
for i in range (0,52,4):
# not clear how binascii.crc32 realy works

    crcval = binascii.crc32(data[i:25880]) & 0xffffffff
    print('crc{:d} = {:#010x}'.format(i,crcval))

print "file  = 0x" + binascii.hexlify(data[0x651C:0x6520])
   
f.closed

quit()
