from cImage import *

master = fileImage("master.png")
key = fileImage("key.png")
result = EmptyImage(master.getWidth(), master.getHeight())

for row in range(master.getHeight()):
    for col in range(master.getWidth()):
        masterPixel = master.getPixel(col, row)
        keyPixel = master.getPixel(col, row)

        if masterPixel != keyPixel:
            resultPixel = Pixel(255, 255, 255)
            result.setPixel(col, row, resultPixel)
        else:
            resultPixel = Pixel(0, 0, 0)
            result.setPixel(col, row, resultPixel)
