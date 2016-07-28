"""This utility aims to provide an easy way to encode text inside of images."""
# TODO Write test cases.
# TODO Write own version of cImage.
# TODO Add interface.
# TODO Add offset.
# TODO Add random seed.

from cImage import FileImage
from cImage import EmptyImage


class Encode:
    """Class"""

    def __init__(self, key_file_name, result_file_name,
                 key_directory, result_directory):
        self.EncodedFileName = result_file_name
        self.keyDirectory = key_directory
        self.key = FileImage(self.keyDirectory + key_file_name)
        self.resultDirectory = result_directory

    def Encode(self, data):
        """Take binary data and add it to an image."""
        result = EmptyImage(self.key.getWidth(), self.key.getHeight())
        count = 0
        for row in range(self.key.getHeight()):
            for col in range(self.key.getWidth()):
                keyPixel = self.key.getPixel(col, row)
                if count < (len(data)):
                    if (int(data[count]) == 1):
                        newPixel = self.flipLSB(keyPixel)
                    else:
                        newPixel = keyPixel
                    count += 1
                    result.setPixel(col, row, newPixel)
                else:
                    result.setPixel(col, row, keyPixel)
        result.save(self.resultDirectory + self.EncodedFileName)

    def backup(self):
        try:
            self.backup = FileImage(self.EncodedFileName + ".bak")
        except:
            self.backup = None

    def textToBinary(self, data):
        """Convert text to binary."""
        result = ''.join(format(ord(x), '08b') for x in data)
        return str(result)

    def checkStorageSize(self):
        """Check maximum amount of data that can be encoded into an image."""
        width = self.key.getWidth()
        height = self.key.getHeight()
        maxSize = width * height
        return maxSize

    def flipLSB(self, pixel):
        """Invert the LSB of the red value of a pixel."""
        tmp = pixel.getRed()
        if (tmp > 120):
            tmp -= 120
        else:
            tmp += 120
        pixel.setRed(tmp)
        return pixel


class Decode:
    def __init__(self, key_file_name, result_file_name,
                 key_directory, result_directory):
        self.EncodedFileName = result_file_name
        self.keyDirectory = key_directory
        self.key = FileImage(key_file_name)
        self.resultDirectory = result_directory

    def Decode(self):
        """Extract binary data from image."""
        encoded = FileImage(self.resultDirectory + self.EncodedFileName)
        result = []
        for row in range(encoded.getHeight()):
            for col in range(encoded.getWidth()):
                encodedPixel = encoded.getPixel(col, row)
                keyPixel = self.key.getPixel(col, row)

                # 1
                if encodedPixel.getRed() != keyPixel.getRed():
                    result.append(1)

                # 0
                else:
                    result.append(0)
        return result

    def binaryToText(self, data):
        """Convert binary to text."""
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
