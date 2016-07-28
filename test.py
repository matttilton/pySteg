"""test file for pySteg"""
from time import time
from pySteg import Decode
from pySteg import Encode

StringToEncode = "test string"


def testEncode():
    encode = Encode("master.png", "testFileName.png", "../", "../")
    encode.Encode(encode.textToBinary(StringToEncode))


def testDecode():
    decode = Decode("master.png", "testFileName.png", "../", "../")
    ResultString = decode.binaryToText(decode.Decode())
    if ResultString == StringToEncode:
        print("Success!")
    else:
        print("Fail!")

startTime = time()
testEncode()
testDecode()
endTime = time()
print("Data encoded and checked in: " + str(endTime - startTime) + " seconds")
