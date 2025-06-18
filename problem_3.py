#problem_3
#read img in greyscale and

# #1. invert the image(pixel values) and display
import cv2
import numpy as np

img=cv2.imread("tomatoes.png", cv2.IMREAD_GRAYSCALE)#in greyscale
#or use bitwise not operation
#inv_img= ~img
inverted_image = 255-img

cv2.imshow("tomatoes_og",img)
cv2.imshow('Inverted Image', inverted_image)
cv2.waitKey(0)

#2. read img in colored format and 
#split it into R,G,B channels
#zero out red channel
# merge channel and display modified img

new_img = cv2.imread("tomatoes.png")  # Loads in BGR format
cv2.imshow("OG_img",new_img)
b, g, r = cv2.split(new_img)  # Splits into Blue, Green, Red
#opp of split is cv2.merge((b,g,r)).

cv2.imshow("Red Channel", r)
cv2.imshow("Green Channel", g)
cv2.imshow("Blue Channel", b)

cv2.waitKey(0)
cv2.destroyAllWindows()

zero_r=np.zeros(r.shape, dtype=r.dtype)
modified_img = cv2.merge((b, g, zero_r))
cv2.imshow("no_red", modified_img )
cv2.waitKey(0)

#3 read color img and flip it horizontal and vertcal and display them
#mirror the img and display it.

#horiz flip 
hori_img=np.fliplr(new_img)
cv2.imshow("horizontally inverted image", hori_img)

#verti flip
#2ways-
# use np.flip(img, axis=0)
vert_img = np.flip(new_img, axis=0)
#slicing
vert2_img=new_img[::-1,:,:]
cv2.imshow("vertically inverted image", vert_img)
cv2.imshow("2-vertically inverted image ", vert2_img)
cv2.waitKey(0)

#mirror same as horizontal flip.
cv2.destroyAllWindows()