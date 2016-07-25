from cImage import FileImage
from cImage import EmptyImage
from cImage import Pixel

encoded = FileImage("Encoded.png")
key = FileImage("master.png")


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
    print(result)

binaryToText(Decode())
