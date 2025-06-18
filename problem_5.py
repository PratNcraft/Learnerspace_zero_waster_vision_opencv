#problem 5-
#------------------------------------#
# when B = G = R, the result is a shade of gray — not a color hue.
#------------------------------------#
import cv2
import numpy as np

#read a colored img &-
# 1. convert it into greyscale img using opencv 
# and apply gaussian blur with kernel size of (9,9) and display
image=cv2.imread("tomatoes.png")
#cv2.cvtcolor(src,cv2._FromToWhat_)
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
Gaussian = cv2.GaussianBlur(gray, (9, 9), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

#2 create a white img of same size and subtract the blurres grayscale img from the white img.//same as inversion of image
#display the result img.

height, width, channels = image.shape
white=np.ones((height,width,channels), dtype=np.uint8)*255
#------------------------------------#
#np.ones(shape, dtype=None) sets all val to one
#shape- tuple showing shape of arr to create: (height,width), (3,3)
#dtype(optional)- data type of elements
#for rgb img, np.ones((100, 100, 3), dtype=np.uint8)
#100x100 pixel grid, the 3 represents that each pixel has 3 components
#all vals set to 1
#multiplying by 255 tomake them white[255,255,255]

# if wanted black, np.zeros(shape, dtype)
#---------------------------------#

#---------------------------------#
#white is 3 channel img and gaus  1 channel(grey)
#subtracting (H,w) with (H,W,3) -> can't so need to convert gaussian to 3 chanel
#makes it 3 channel but with all having same grey value
#eg-
# When you convert to [100, 100, 100] — all three channels have the
# same intensity, so they combine evenly to form:
# gray color that’s visually identical to grayscale value 100.
#---------------------------------#
gray_3ch = cv2.cvtColor(Gaussian, cv2.COLOR_GRAY2BGR)
new_img = cv2.subtract(white, gray_3ch)

cv2.imshow("new img", new_img)
cv2.imshow("og img",gray)
cv2.waitKey(0)

#3 create blank img size(512,512)
#ceate a rectangle of blue color with top left cornor at (50,50) and bottom right (462,462) with thickness of 3 pixels
#draw circle of r=50, centre(300,300) filled with green color
#draw red diagonal line starting from top-R to bottom-L corner of thivkness=2pixels

new_img_1=np.zeros((512,512,3),dtype=np.uint8)    #black
#rectangle
#to draw rect- cv2.rectangle(image, start_point, end_point, color, thickness) color in (,,) format
cv2.rectangle(new_img_1, (50,50), (462,462),(255,0,0), 3)
#---------------------------------#
#circle 
#cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None)
#thickness - Circle outline thickness. If -1:circle is filled.
# lineType (Optional)- Circle boundary type. Default is 8-connected line.
# shift (Optional)- Number of fractional bits in center coordinates and radius.
#---------------------------------# 
cv2.circle(new_img_1, (300,300), 50, (0,225,0), -1)

#diagonal line
# cv2.line(image, start_point, end_point, color, thickness) 
cv2.line(new_img_1, (0,0), (512,512), (0,0,225), 22)

cv2.imshow("drawing", new_img_1)
cv2.waitKey(0)

cv2.destroyAllWindows()