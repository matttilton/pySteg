# TODO Consolidate file. DONE
# TODO Make classes.
# TODO Add variable for file name.
# TODO Add variable for file type.
# TODO Add variable for path to master.
# TODO Add variable for path to result.
# TODO Add interface.
# TODO Add offset. In Progress
# TODO Add random seed
# TODO Add timer. DONE
# TODO Add error check. DONE
# TODO Organize
# TODO Add Docstrings
# TODO Add check for max data size. DONE

from cImage import FileImage
from cImage import EmptyImage
from cImage import Pixel
from time import time

key = FileImage("master.png")
backup = FileImage("Encoded.png")

def Encode(data):
    result = EmptyImage(key.getWidth(), key.getHeight())
    count = 0
    for row in range(key.getHeight()):
        for col in range(key.getWidth()):
            keyPixel = key.getPixel(col, row)
            if count < (len(data)):
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
    encoded = FileImage("Encoded.png")
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
        if each is not '\x00':
            cleanCharList.append(each)
    result = ''.join(str(x) for x in cleanCharList)
    return result


def asciiTest(data):
    binaryString = ''.join(str(x) for x in data)
    binaryList = [binaryString[i:i+8] for i in range(0, len(binaryString), 8)]
    for each in binaryList:
        print(str(chr(int(each, 2))))

def checkStorageSize():
    width = key.getWidth()
    height = key.getHeight()
    maxSize = width * height
    return maxSize

def flipLSB(pixel):
    tmp = pixel.getRed()
    if (tmp > 0):
        tmp -= 1
    else:
        tmp += 1
    pixel.setRed(tmp)
    return pixel

startTime = time()
StringToEncode = "test string"
if (len(textToBinary(StringToEncode)) <= checkStorageSize()):
    Encode(textToBinary(StringToEncode))
    encodeCheck = binaryToText(Decode())
    if(str(encodeCheck) == str(StringToEncode)):
        print("Data successfully encoded")
    else:
        backup.save("Encoded.png")
        print("Encoded.png reverted to backup")
        raise ValueError("Encoding/Decoding failed " + "\'" + encodeCheck + "\'" + " != " + "\'" + StringToEncode + "\'")
else:
    backup.save('Encoded.png')
    print('Encoded.png reverted to backup')
    raise ValueError('Input data is too large for given image. Your data is ' + str(len(textToBinary(StringToEncode))) + ' bits. Make sure that data is less than ' + str(checkStorageSize()) + " bits")
endTime = time()
print("Data encoded and checked in: " + str(endTime - startTime) + " seconds")
