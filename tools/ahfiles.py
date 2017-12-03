#!/usr/bin/env python
import os
import sys
import struct
import binascii
from array import array
import argparse
import csv

def calcCheckSum (scenearray):
    "retuns the CheckSum of a Scene filedata array"
    lut = [0x00000000,0x77073096,0xEE0E612C,0x990951BA,0x076DC419,0x706AF48F,0xE963A535,0x9E6495A3,0x0EDB8832,0x79DCB8A4,0xE0D5E91E,0x97D2D988,0x09B64C2B,0x7EB17CBD,0xE7B82D07,0x90BF1D91,0x1DB71064,0x6AB020F2,0xF3B97148,0x84BE41DE,0x1ADAD47D,0x6DDDE4EB,0xF4D4B551,0x83D385C7,0x136C9856,0x646BA8C0,0xFD62F97A,0x8A65C9EC,0x14015C4F,0x63066CD9,0xFA0F3D63,0x8D080DF5,0x3B6E20C8,0x4C69105E,0xD56041E4,0xA2677172,0x3C03E4D1,0x4B04D447,0xD20D85FD,0xA50AB56B,0x35B5A8FA,0x42B2986C,0xDBBBC9D6,0xACBCF940,0x32D86CE3,0x45DF5C75,0xDCD60DCF,0xABD13D59,0x26D930AC,0x51DE003A,0xC8D75180,0xBFD06116,0x21B4F4B5,0x56B3C423,0xCFBA9599,0xB8BDA50F,0x2802B89E,0x5F058808,0xC60CD9B2,0xB10BE924,0x2F6F7C87,0x58684C11,0xC1611DAB,0xB6662D3D,0x76DC4190,0x01DB7106,0x98D220BC,0xEFD5102A,0x71B18589,0x06B6B51F,0x9FBFE4A5,0xE8B8D433,0x7807C9A2,0x0F00F934,0x9609A88E,0xE10E9818,0x7F6A0DBB,0x086D3D2D,0x91646C97,0xE6635C01,0x6B6B51F4,0x1C6C6162,0x856530D8,0xF262004E,0x6C0695ED,0x1B01A57B,0x8208F4C1,0xF50FC457,0x65B0D9C6,0x12B7E950,0x8BBEB8EA,0xFCB9887C,0x62DD1DDF,0x15DA2D49,0x8CD37CF3,0xFBD44C65,0x4DB26158,0x3AB551CE,0xA3BC0074,0xD4BB30E2,0x4ADFA541,0x3DD895D7,0xA4D1C46D,0xD3D6F4FB,0x4369E96A,0x346ED9FC,0xAD678846,0xDA60B8D0,0x44042D73,0x33031DE5,0xAA0A4C5F,0xDD0D7CC9,0x5005713C,0x270241AA,0xBE0B1010,0xC90C2086,0x5768B525,0x206F85B3,0xB966D409,0xCE61E49F,0x5EDEF90E,0x29D9C998,0xB0D09822,0xC7D7A8B4,0x59B33D17,0x2EB40D81,0xB7BD5C3B,0xC0BA6CAD,0xEDB88320,0x9ABFB3B6,0x03B6E20C,0x74B1D29A,0xEAD54739,0x9DD277AF,0x04DB2615,0x73DC1683,0xE3630B12,0x94643B84,0x0D6D6A3E,0x7A6A5AA8,0xE40ECF0B,0x9309FF9D,0x0A00AE27,0x7D079EB1,0xF00F9344,0x8708A3D2,0x1E01F268,0x6906C2FE,0xF762575D,0x806567CB,0x196C3671,0x6E6B06E7,0xFED41B76,0x89D32BE0,0x10DA7A5A,0x67DD4ACC,0xF9B9DF6F,0x8EBEEFF9,0x17B7BE43,0x60B08ED5,0xD6D6A3E8,0xA1D1937E,0x38D8C2C4,0x4FDFF252,0xD1BB67F1,0xA6BC5767,0x3FB506DD,0x48B2364B,0xD80D2BDA,0xAF0A1B4C,0x36034AF6,0x41047A60,0xDF60EFC3,0xA867DF55,0x316E8EEF,0x4669BE79,0xCB61B38C,0xBC66831A,0x256FD2A0,0x5268E236,0xCC0C7795,0xBB0B4703,0x220216B9,0x5505262F,0xC5BA3BBE,0xB2BD0B28,0x2BB45A92,0x5CB36A04,0xC2D7FFA7,0xB5D0CF31,0x2CD99E8B,0x5BDEAE1D,0x9B64C2B0,0xEC63F226,0x756AA39C,0x026D930A,0x9C0906A9,0xEB0E363F,0x72076785,0x05005713,0x95BF4A82,0xE2B87A14,0x7BB12BAE,0x0CB61B38,0x92D28E9B,0xE5D5BE0D,0x7CDCEFB7,0x0BDBDF21,0x86D3D2D4,0xF1D4E242,0x68DDB3F8,0x1FDA836E,0x81BE16CD,0xF6B9265B,0x6FB077E1,0x18B74777,0x88085AE6,0xFF0F6A70,0x66063BCA,0x11010B5C,0x8F659EFF,0xF862AE69,0x616BFFD3,0x166CCF45,0xA00AE278,0xD70DD2EE,0x4E048354,0x3903B3C2,0xA7672661,0xD06016F7,0x4969474D,0x3E6E77DB,0xAED16A4A,0xD9D65ADC,0x40DF0B66,0x37D83BF0,0xA9BCAE53,0xDEBB9EC5,0x47B2CF7F,0x30B5FFE9,0xBDBDF21C,0xCABAC28A,0x53B39330,0x24B4A3A6,0xBAD03605,0xCDD70693,0x54DE5729,0x23D967BF,0xB3667A2E,0xC4614AB8,0x5D681B02,0x2A6F2B94,0xB40BBE37,0xC30C8EA1,0x5A05DF1B,0x2D02EF8D]
    checksum = 0x0
    idx = 0x0
    for i in range (0xC, 0x651C):
        idx = ~(scenearray[i] ^ checksum) & 0xFF  
        checksum = lut[idx] ^ 0xFF000000
    
    return checksum

def updateCheckSum (scenearray):
    "updates the checksum of of a scene data array"
    checksum = calcCheckSum (scenearray)
    a2 = binascii.unhexlify('%08x' % checksum) #format 8 digit with leading 0
    b2 = array('B',a2)
    b2.reverse()
    scenearray[0x651C:0x6520] = b2[0:4]
    return

def getCheckSum (scenearray):
    checksum = scenearray[0x651C:0x6520]
    return checksum

def setSceneName (scenearray, scenename):
    "set Scene Name into scenearray. does not check len of str"
    #0 terminated string vermutlich 10 oder 11 Zeichen, max 63
    a = array('B', scenename)
    alen = len(a)
    alen = alen & 0xF #limit string lenght
    scenearray[12:12+alen] = a[:alen]
    scenearray[12+alen+1]=0 #0 terminated string needed???
    return

def setSceneNum (scenearray, numstr):
    "set the scene number, should be unique in 1 show and fit to the filename"
    scenearray[3] = int (numstr)  
    return
def writeSceneFile (scenearray, numstr):
    "writes the scene to file"
    #ToDo check number, path
    scenearray[3] = int(numstr)
    updateCheckSum (scenearray)
    # py 3.6 os.makedirs(args.outpath, exist_ok=True)
    filename = os.path.join(args.showdir,"SCENE" + numstr +".DAT")
    with open(filename, 'w') as ofile:
        scenearray.tofile(ofile)

    return

def processMuteFile():
    "reads the file given at cmd line arg --mutefile and generates the scenefiles"
    #open template scenefile = microfone test
    with open(args.baseScene,'rb') as baseScene:
        sa = baseScene.read()
        scenearray = array('B', sa)
    if not os.path.exists(args.showdir):
        os.makedirs(args.showdir)

    # make a copy of the microphone test file
    setSceneName(scenearray,"MicTest")
    writeSceneFile(scenearray,"000")
    
    with open(args.mutefile, 'rb') as mutefile:
        mfreader = csv.reader(mutefile, delimiter=' ')
        #iterate thru mute file lines
        for row in mfreader:
            print ', '.join(row)
            setMuteList(scenearray, row)
            setSceneName(scenearray,"s"+row[0])
            filenr = format(int(row[0]), '03d') #first line is scenenumber
            writeSceneFile(scenearray,filenr)
    return

#old outdated
def setMuteList(scenearray, mutelist):
    "set all 24 mute as in the mutelist of 0 and 1"
    #ToDocheck data types, number of mute channels,
    for i in range(0,3):
        scenearray[0xb8 + i*0xC0] = int(mutelist[i+1]) #first col is scene number
    return

def insertSceneafter(numstr):
    "insert new scenefile and shifts the following up"
    #we work reverse, starting with the highest file number
    #increase the file number in name in internaly 
    #write the new file and decrease file number, until we have
    # increased the given numstr file
    # find the highest file number via sort?
    # gererischer Ansatz: erst mal File namen anpassen und dann 
    # interne file nummer und crc anpassen
    # problem: interen Scene Namen, wenn der durch nummeriert ist
    # automatisch erkennen und anpassen???
    

    filename = os.path.join(args.showdir,"SCENE" + numstr +".DAT")
    with open(filename, 'w') as ofile:
        scenearray.tofile(ofile)

    return

def processSceneNames():

    with open(args.scenenames, 'r') as scnamefile:
        sfreader = csv.reader(scnamefile, delimiter=',')
        #iterate thru mute file lines
        for row in sfreader:
            print ', '.join(row)
            try:
                numstr = format(int(row[0]), '03d')
                filename = os.path.join(args.showdir,"SCENE" + numstr +".DAT")
                with open(filename, 'r') as ifile:
                    sa = ifile.read()
                    scenearray = array('B', sa)
                    setSceneName(scenearray,row[1])
            
                writeSceneFile(scenearray, numstr)
            except:
                print "empty line"
                
            #writeSceneFile(scenearray,filenr)

    return
# defined command line options
# this also generates --help and error handling
CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--baseScene",  # name on the CLI - drop the `--` for positional/required parameters
  nargs=1,  # 1 input file
  default="../SHOW0011/SCENE000.DAT",  # default if nothing is provided
  help="Scene.DAT file as base for the operation",
)
CLI.add_argument(
 "--output", 
 nargs='?',  # 1 file
 help= " output file name",
)
CLI.add_argument(
 "--showdir",  
 #nargs=1,  # 1 dir name list of 1 element
 default="../SHOW0111",  # default if nothing is provided
 help="directory for the operation"
)
CLI.add_argument(
 "--scenename",
 nargs=1,  # a name
 help="scene name, for a single Scene File",
)
CLI.add_argument(
 "--scenenames",
 #nargs=1,  # a name
 help="file name, comma seperated, scene number, Scene Name",
)
CLI.add_argument(
 "--showname", 
 nargs=1,  # 1 name
 help="set the show name",
)
CLI.add_argument(
 "--wcrc", 
 action='store_true', #flag, default false
 help= "recalculate and write the CRC into .DAT files",
)
CLI.add_argument(
"--mutefile",
nargs='?',
const="./mutefile.csv",
help="mute file; comma seperated table; first col is scene number, followed by channels mute= 1, not mute = 0"
)

# parse the command line
args = CLI.parse_args()
# access CLI options
print("baseScene: %r" % args.baseScene)
print("output: %r" % args.output)
print("wcrc: %r" % args.wcrc)

#block starts with block number and A5 A5 A5
# might be they claculate CRC block wise
#bl_start=[44,11568,11868,21472,21476,21484,21500,21528,21556,21608,21780,25880]

if args.mutefile is not None:
     processMuteFile()
else:
# eventuell etwas besser Steuerung, damit Mutefile und Szene Names zusammen aber auch 
# getrennt bearbeitet werden koennen
    if args.scenenames is not None:
        processSceneNames()


#print('crc = {:#010x}'.format(checksum))
#a1 = getCheckSum(ba1)
#a1.reverse()
#print "file = 0x" + binascii.hexlify(a1)

quit()
