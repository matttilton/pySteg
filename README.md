# pySteg
Simple steganography encoder/decoder written in python.

Encoding:
  Convert text string to binary. For every 1 in the binary string, make a diference in the coresponding pixel (subtract 1 if greater than 0, otherwise add 1). The actual value is not important, the only important thing is that it causes a difference (smaller differences are better, since they will be harder to detect with eyes).
  
Decoding:
  Read every pixel of both the image that you want to decode and the key image. If a pixel is different record a 1, if it is not record a 0. Convert binary string back to ascii.

There is plenty of room for improvement, feel free to make suggestions.
