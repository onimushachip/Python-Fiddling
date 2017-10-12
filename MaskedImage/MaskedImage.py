import math
from PIL import Image


##Euclidean Distance
# def distanceOfTwoPoints(px, py, qx, qy):
#     distance = math.sqrt((px - qx) ** 2 + (py - qy) ** 2)
#     return distance

##Taxicab Distance
# def distanceOfTwoPoints(px, py, qx, qy):
#     distance = (abs(qx - px) + abs(qy - py))
#     return distance

##Customed Eclidenan
# def distanceOfTwoPoints(px, py, qx, qy):
#     a = widthSource/2
#     b = heightSource/2
#     distance = math.sqrt(((qx - px)/a)**2 + ((qy - py)/b)**2)
#     return distance

##Supercircle distance
# def distanceOfTwoPoints(px, py, qx, qy):
#     n = 4 #change n for different tests (0.5 and 4)
#     distance = (abs(qx - px)**n + abs(qy - py)**n)**(1/n)
#     return distance


def maskCustom(image, centerX, centerY, radius, backgroundColor):
    processedImage = image.copy()
    (width, height) = processedImage.size
    for x in range (width):
        for y in range (height):
            if distanceOfTwoPoints(centerX, centerY, x, y) > radius:
                processedImage.putpixel((x, y), backgroundColor)
    return processedImage


someColor = (140, 124, 200)
#Open the source image
sourceImage = Image.open("sourceImage.jpg")
(widthSource, heightSource) = sourceImage.size

maskedImage = maskCustom(sourceImage, 310, 310, 150, someColor)

##Test this with the customed Euclidean distance
# maskedImage = maskCustom(sourceImage, 310, 310, 1, someColor)

maskedImage.save("processedImage.jpg")
maskedImage.show()