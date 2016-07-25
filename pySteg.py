# TODO Consolidate file. DONE
# TODO Make classes.
# TODO Add variable for file name.
# TODO Add variable for file type.
# TODO Add variable for path to master.
# TODO Add variable for path to result.
# TODO Add interface.
# TODO Add offset
# TODO Add random seed
# TODO Add timer. DONE
# TODO Add error check
# TODO Organize
# TODO Add Docstring

from cImage import FileImage
from cImage import EmptyImage
from cImage import Pixel
from time import time

encoded = FileImage("Encoded.png")
key = FileImage("master.png")
result = EmptyImage(key.getWidth(), key.getHeight())


def Encode(data):
    count = 0
    for row in range(key.getHeight()):
        for col in range(key.getWidth()):
            keyPixel = key.getPixel(col, row)
            if count < (len(data) - 1):
                if (int(data[count]) == 1):
                    newPixel = flipLSB(keyPixel)
                else:
                    newPixel = keyPixel
                count += 1
                result.setPixel(col, row, newPixel)
            else:
                result.setPixel(col, row, keyPixel)
    result.save("Encoded.png")


def Decode():
    result = []
    for row in range(encoded.getHeight()):
        for col in range(encoded.getWidth()):
            encodedPixel = encoded.getPixel(col, row)
            keyPixel = key.getPixel(col, row)

            # 1
            if encodedPixel.getRed() != keyPixel.getRed():
                result.append(1)

            # 0
            else:
                result.append(0)
    return result


def textToBinary(data):
    result = ''.join(format(ord(x), '08b') for x in data)
    print(result)
    return str(result)


def binaryToText(data):
    binaryString = ''.join(str(x) for x in data)
    binaryList = [binaryString[i:i+8] for i in range(0, len(binaryString), 8)]
    intList = []
    for each in binaryList:
        intList.append(int(each, 2))
    charList = []
    for each in intList:
        charList.append(str(chr(each)))
    cleanCharList = []
    for each in charList:
        if each != '\x00':
            cleanCharList.append(each)
    result = ''.join(str(x) for x in cleanCharList)
    return result


def asciiTest(data):
    binaryString = ''.join(str(x) for x in data)
    binaryList = [binaryString[i:i+8] for i in range(0, len(binaryString), 8)]
    for each in binaryList:
        print(str(chr(int(each, 2))))


def flipLSB(pixel):
    tmp = pixel.getRed()
    if (tmp > 0):
        tmp -= 1
    else:
        tmp += 1
    pixel.setRed(tmp)
    return pixel

startTime = time()
StringToEncode = "go fuck yourselfgghasd"
Encode(textToBinary(StringToEncode))
encodeCheck = binaryToText(Decode())
if(encodeCheck == StringToEncode):
    print(encodeCheck)
else:
    raise ValueError("Encoding/Decoding failed " + StringToEncode + " != " + encodeCheck)
endTime = time()
print("Data encoded and checked in: " + str(endTime - startTime) + " seconds")
