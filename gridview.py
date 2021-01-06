import cv2
import math
import sys

print('give 4 parameters, the file location, grid box length (pixels), font size, and line thickness')
print('optionally, you can also specify the scaling of the final output')

image = cv2.imread(sys.argv[1])
boxsize = int(sys.argv[2])
image = cv2.copyMakeBorder(image, boxsize * 2, 0, boxsize * 2 , 0, cv2.BORDER_CONSTANT, 
    value=(255,255,255))

width = image.shape[1] 
height = image.shape[0] 
xiter = math.floor(width / boxsize) 
yiter = math.floor(height / boxsize)

fontSize = int(sys.argv[3])
linethckness = int(sys.argv[4])

print(image.shape)

for i in range(yiter):
    cv2.putText(image, str(i),  (boxsize, (i+2)*boxsize), cv2.FONT_HERSHEY_PLAIN, fontSize, (0,0,0), 
        linethckness)
    cv2.line(image, (0, (i+2)*boxsize), (width, (i+2)*boxsize), (0,0,0), thickness=linethckness)

for i in range(xiter):
    cv2.putText(image, str(i),((i+2)*boxsize, boxsize*2), cv2.FONT_HERSHEY_PLAIN, fontSize, (0,0,0), 
        linethckness)
    cv2.line(image, ((i+2)*boxsize, 0), ((i+2)*boxsize, height), (0,0,0), thickness=linethckness)

if len(sys.argv) > 5:
    scale = float(sys.argv[5])
    image = cv2.resize(image, (int(image.shape[1] * scale), int(image.shape[0] * scale)))

cv2.imshow('fr', image)
cv2.waitKey(0)
cv2.destroyAllWindows()