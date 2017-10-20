from PIL import Image

def flipDiagonal(pic):
    (width, height) = pic.size
    newImage = Image.new("RGB", (height, width))
    for x in range(width):
        for y in range(height):
            oldPixel = pic.getpixel((x, y))
            newImage.putpixel((y, x), oldPixel)
    return newImage

testImage = Image.open("testImage.jpg")
newImage = flipDiagonal(testImage)
newImage.save("processedImage.jpg")
newImage.show()
