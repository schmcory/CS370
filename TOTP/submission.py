# Author: Cory Schmidt
# Date: 12/12/2019
# Description: This program generates 30-second one-time passwords and QR codes that can be used with Google Authenticator. 
# Sources: 
#         generateORCode: https://www.geeksforgeeks.org/python-generate-qr-code-using-pyqrcode-module/
#         import png: https://stackoverflow.com/questions/31142919/how-to-install-the-png-module-in-python
#         Key URI format: https://github.com/google/google-authenticator/wiki/Key-Uri-Format
#         Base 64 library: https://docs.python.org/2/library/base64.html
#         Struct pack: https://docs.python.org/2/library/struct.html
#         Hmac: https://docs.python.org/2/library/hmac.html
#         Time: https://docs.python.org/2/library/time.html
# Libaries: 
#           pip3 install pyqrcode
#           pip3 install pypng
#To run: python3 submission.py --generate-qr OR --get-otp

#import libraries
import sys 
import png
import pyqrcode
from pyqrcode import QRCode
import hmac
import base64
import struct
import hashlib
import time

# Function generates a QR code
def generateQR(s):
    img = pyqrcode.create(s)        # Generate QR code 
    img.show()                      # Show QR code
    
# Function generates an OTP
def getOTP(secret, time):
    key = base64.b32decode(secret)                                     # decodes a string
    msg = struct.pack(">Q", time)                                      # holds string of unsigned long long int 
    h = hmac.new(key, msg, hashlib.sha1).digest()                      # holds new hmac oject 
    o = h[-1] & 0x0F                                                   # offsets hmac
    c = (struct.unpack(">I", h[o:o+4]) [0] & 0x7FFFFFFF) % 1000000     # unpack string
    return c

def main():
    # hardcoded key value
    my_key = "JBSWY3DPEHPK3PXP"
    
    # label follows format in github documentation
    label = "otpauth://totp/OSU:schmcory@oregonstate.edu?secret=" + my_key + "&issuer=OSU"
    
    # holds the time is seconds, every 30 seconds 
    current_time = int(time.time()) // 30
    
    # handle user input 
    if len(sys.argv) == 2:
        if sys.argv[1] == "--generate-qr":          
            generateQR(label)
        elif sys.argv[1] == "--get-otp":
            print(getOTP(my_key, current_time))  
        else:
            print("Invalid command")
    else:
        print("Usage: submission.py --generate-qr OR --get-otp")
    
main() 
    
    




