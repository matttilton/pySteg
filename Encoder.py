from cImage import FileImage
from cImage import EmptyImage
from cImage import Pixel

master = FileImage("master.png")
result = EmptyImage(master.getWidth(), master.getHeight())


def toBinary(data):
    result = ''.join(format(ord(x), 'b') for x in data)
    print(result)
    return str(result)


def Encode(data):
    count = 0
    for row in range(master.getHeight()):
        for col in range(master.getWidth()):
            masterPixel = master.getPixel(col, row)
            if (int(data[count]) == 1):
                newPixel = flipLSB(masterPixel)
            else:
                newPixel = masterPixel
            result.setPixel(col, row, newPixel)
    result.save("Encoded.png")


def flipLSB(pixel):
    red = pixel.getRed()
    red = bin(red)
    if(red[-1] == 1):
        red[-1] = 0
    elif(red[-1] == 0):
        red[-1] = 1
    red = int(red, 2)
    pixel.setRed(red)
    return pixel

Encode(toBinary("test"))
