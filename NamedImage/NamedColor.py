from PIL import Image
#Image size
width = 400
height = 400

somecolor = (255, 255, 255)
somecolor2 = (100, 100, 100)
somecolor3 = (70, 70, 70)
somecolor4 = (50, 50, 50)

image = Image.new('RGB', (height, width))

for verticalPixel in range(height):
    for horizontalPixel in range(width):
        ##linear line
        if (verticalPixel/2 == horizontalPixel):
            image.putpixel((verticalPixel, horizontalPixel), somecolor)
        ##liner line
        if (verticalPixel*2 == horizontalPixel):
            image.putpixel((verticalPixel, horizontalPixel), somecolor)
        ##liner line -1/2 slope
        if (verticalPixel+horizontalPixel == height):
            image.putpixel((verticalPixel, horizontalPixel), somecolor)

        ##Drawing a square
        if (verticalPixel == 10 and horizontalPixel > 10 and horizontalPixel < 390):
            image.putpixel((verticalPixel, horizontalPixel), somecolor)
        if (verticalPixel == 390 and horizontalPixel > 10 and horizontalPixel < 390):
            image.putpixel((verticalPixel, horizontalPixel), somecolor)
        if (horizontalPixel == 10 and verticalPixel > 10 and verticalPixel <390):
            image.putpixel((verticalPixel, horizontalPixel), somecolor)
        if (horizontalPixel == 390 and verticalPixel > 10 and verticalPixel <390):
            image.putpixel((verticalPixel, horizontalPixel), somecolor)


image.save("testImage.png")
image.show()