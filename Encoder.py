from cImage import FileImage
from cImage import EmptyImage
from cImage import Pixel

master = FileImage("master.png")
result = EmptyImage(master.getWidth(), master.getHeight())


def textToBinary(data):
    result = ''.join(format(ord(x), '08b') for x in data)
    print(result)
    return str(result)


def asciiTest(data):
    binaryString = ''.join(str(x) for x in data)
    binaryList = [binaryString[i:i+8] for i in range(0, len(binaryString), 8)]
    for each in binaryList:
        print(str(chr(int(each, 2))))


def Encode(data):
    count = 0
    for row in range(master.getHeight()):
        for col in range(master.getWidth()):
            masterPixel = master.getPixel(col, row)
            if count < (len(data) - 1):
                if (int(data[count]) == 1):
                    newPixel = flipLSB(masterPixel)
                else:
                    newPixel = masterPixel
                count += 1
                result.setPixel(col, row, newPixel)
            else:
                result.setPixel(col, row, masterPixel)
    result.save("Encoded.png")


def flipLSB(pixel):
    tmp = pixel.getRed()
    if (tmp > 0):
        tmp -= 1
    else:
        tmp += 1
    pixel.setRed(tmp)
    # pixel.setRed(255)
    return pixel

Encode(textToBinary("go fuck yourself"))
