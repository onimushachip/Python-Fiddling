from PIL import Image

testTom = Image.open("tom.png") #open the image needed to process
print(testTom.size)
(width, height) = testTom.size
testTomCopy = testTom.copy()

for verticalPixel in range(height):
    for horizontalPixel in range(width):
        pixel = testTomCopy.getpixel((horizontalPixel, verticalPixel))
        # print(pixel)
        (r, g, b, x) = pixel
        # avg = (r + g + b + x)//3
        newPixel = (g, r, x, b) #switching color in the old pixel
        testTomCopy.putpixel((horizontalPixel,verticalPixel), newPixel)

testTomCopy.save("testTomeCopy.png") #save the new processed image
testTomCopy.show()