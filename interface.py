from pySteg import Decode
from pySteg import Encode
from time import time

print("pySteg interface v0.1")
print("A default value will be used for any blank argument \n")

running = True

while running:
    decoding = False
    encoding = False
    help = "Press 1 to encode a file. \nPress 2 to decode a file. \nPress 3 to quit."
    action = input(">>> ")
    if (action == "1"):
        encoding = True
        decoding = False
    elif (action == "2"):
        encoding = False
        decoding = True
    elif (action == "3"):
        running = False
    elif (action == "help"):
        print(help)
    else:
        print("Unrecognized value")
    while encoding:
        sourcePath = input("Path for starting image: ")
        if (sourcePath == ""):
            sourcePath == ""
        sourceName = input("Name of starting image: ")
        if (sourceName == ""):
            sourceName = "master.png"
        resultPath = input("Path for encoded image: ")
        if (resultPath == ""):
            resultPath = ""
        resultName = input("Name of ending image: ")
        if (resultName == ""):
            resultName = "encoded.png"
        stringToEncode = input("String to encode: ")
        if (stringToEncode == ""):
            stringToEncode = "Dont be so lazy next time and give me a string"
        encode = Encode(sourceName, resultName, sourcePath, resultPath)
        startTime = time()
        encode.Encode(encode.textToBinary(stringToEncode))
        endTime = time()
        print("Data encoded in: " + str(endTime - startTime) + " seconds")
        encoding = False
    while decoding:
        sourcePath = input("Path for starting image: ")
        if (sourcePath == ""):
            sourcePath == ""
        sourceName = input("Name of ending image: ")
        if (sourceName == ""):
            sourceName = "master.png"
        resultPath = input("Path for encoded image: ")
        if (resultPath == ""):
            resultPath = ""
        resultName = input("Name of starting image: ")
        if (resultName == ""):
            resultName = "encoded.png"
        startTime = time()
        decode = Decode(sourceName, resultName, sourcePath, resultPath)
        print("\n" + decode.binaryToText(decode.Decode()))
        endTime = time()
        print("Data decoded: " + str(endTime - startTime) + " seconds")
        decoding = False
