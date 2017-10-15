import math
from PIL import Image

def changeColor(pic):
    image = pic.copy()
    (width, height) = pic.size
    for x in range(width):
        for y in range(height):
            color = image.getpixel((x, y))
            (r, g, b) = color
            if r > g:
                newColor = (b, g, r)
            else:
                if r > b:
                    newColor = (b, g, r)
            image.putpixel((x, y), newColor)
    return image

def distance(color1, color2):
    (r1, g1, b1) = color1
    (r2, g2, b2) = color2
    distanceResult = math.sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)
    return distanceResult

def changeColorByDistance(pic, wantedColor, distanceInput):
    image = pic.copy()
    (width, height) = pic.size
    for x in range(width):
        for y in range(height):
            color = image.getpixel((x, y))
            if distance(color, wantedColor) < distanceInput:
                (r, g, b) = color
                newColor = (int(r/2), int(g/2), int(b/2)) ##Changing color
                image.putpixel((x, y), newColor)
    return image



testImage = Image.open("testImage.jpg")
# processedImage = changeColor(testImage)
processedImage = changeColorByDistance(testImage, (250, 250, 250), 60) ##change parameter
processedImage.show()
processedImage.save("processedImage.jpg")
