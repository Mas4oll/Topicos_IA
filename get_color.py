# Python programs to find
# unique HSV code for color

# Importing the libraries openCV & numpy
import cv2
import numpy as np

#BGR
color = np.uint8([[[0, 0, 255]]])

h = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

print("Valores en HSV: ", h)


lower = [h[0]-10, 100, 100]
upper = [h[0]+10, 255, 255]

print("Low: ", lower)
print("High: ", upper)

# Make python sleep for unlimited time
cv2.waitKey(0)