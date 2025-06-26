#problem-4
import numpy as np
import cv2
#read a colored img and display its size and pixel val of diff channels

image=cv2.imread("tomatoes.png")

height, width, channels = image.shape
print(f"Image height: {height} pixels")
print(f"Image width: {width} pixels")
#print(f"Number of channels: {channels}")
#------------------------------------#
# Pixel values can be accessed using array indexing image[y, x, channel] y:row index, x:column index, channel index (0:Blue, 1:Green, 2:Red in BGR)
#pixel values @ position (100,100)
#------------------------------------#
x,y=100,100
blue_value = image[y, x, 0]
green_value = image[y, x, 1]
red_value = image[y, x, 2]
print(f"Pixel at ({x}, {y}): B={blue_value}, G={green_value}, R={red_value}")

#2.write funtn to manually convert color img to greyscale.
#  no using cv2.cvtColor()
#Gray=0.299R + 0.587G + 0.114B

b, g, r = cv2.split(image)
#------------------------------------#
#Image data in OpenCV is usually of type np.uint8—integers from 0 to 255
# gray=0.299*r+0.587*g+0.114*b --> gives in float value
#imshow() uses uint vals. so need ot convert float into uint 8 
#------------------------------------#
gray = (0.114 * b + 0.587 * g + 0.299 * r).astype(np.uint8)

cv2.imshow("grey image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
#3 count pure whilte pixels [255,255,255] in color img.

white_pixels = np.all(image == [255, 255, 255], axis=2)
# image == [255, 255, 255] creates a boolean mask of shape (H, W, 3).
# np.all(..., axis=2) collapses across the 3 channels — True only where all 
# 3 values are 255.
# np.sum() counts the True values (i.e., white pixels).

count = np.sum(white_pixels)
print("Number of pure white pixels:", count)
