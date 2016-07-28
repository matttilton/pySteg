from pySteg import Decode
from pySteg import Encode
from time import time

print("pySteg interface v0.1")
print("A default value will be used for any blank argument \n")

running = True

while running:
    decoding = False
    encoding = False
    action = input("Enter 1 for encoding or 2 for decoding: ")
    if (action == "1"):
        encoding = True
        decoding = False
    elif (action == "2"):
        encoding = False
        decoding = True
    elif (action == "3"):
        running = False
    else:
        print("Unrecognized value")
    while encoding:
        sourcePath = input("Path for starting image: ")
        if (sourcePath == ""):
            sourcePath == "../"
        sourceName = input("Name of starting image: ")
        if (sourceName == ""):
            sourceName = "master.png"
        resultPath = input("Path for encoded image: ")
        if (resultPath == ""):
            resultPath = "../"
        resultName = input("Name of ending image: ")
        if (resultName == ""):
            resultName == "encoded.png"
        stringToEncode = input("String to encode: ")
        if (stringToEncode == ""):
            stringToEncode = "Dont be so lazy next time and give me a string"
        encode = Encode(sourceName, resultName, sourcePath, resultPath)
        startTime = time()
        encode.Encode(encode.textToBinary(stringToEncode))
        endTime = time()
        print("Data encoded and checked in: " + str(endTime - startTime) + " seconds")
        encoding = False
    while decoding:
        sourcePath = input("Path for starting image: ")
        if (sourcePath == ""):
            sourcePath == "../"
        sourceName = input("Name of ending image: ")
        if (sourceName == ""):
            sourceName = "master.png"
        resultPath = input("Path for encoded image: ")
        if (resultPath == ""):
            resultPath = "../"
        resultName = input("Name of starting image: ")
        if (resultName == ""):
            resultName == "encoded.png"
        decode = Decode(sourceName, resultName, sourcePath, resultPath)
        print(decode.binaryToText(decode.Decode()))
        decoding = False
