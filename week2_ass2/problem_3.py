#problem_3
import cv2
import numpy as np
import matplotlib.pyplot as plt
#create a basic image processing pipeline using opencv
#1.load an color image and convert it to grayscale
image=cv2.imread("image_1.png")
new_img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("new ing",new_img)
cv2.imshow("og",image)
# cv2.waitKey(0)

#2 apply gaussian blur 5x5 to reduce blur
#blurred_image = cv2.GaussianBlur(image, kernel_size, 0) ksize in tuple
gaussian=cv2.GaussianBlur(new_img,(5,5),0) #0 for sigma/alpha val
cv2.imshow("gaussian",gaussian)

#3 run canny edge detection and display all 3 img: OG, blurred
#cv2.Canny(image, threshold1, threshold2, apertureSize=3, L2gradient=False)

#high threshold-Any pixel with a gradient magnitude above the high threshold is immediately 
# classified as a strong edge pixel and is included in the final edge map.
# These are considered "sure edges."

#thresholds control the sensitivity of the edge detection. Lower thresholds 
# will detect more edges, including potentially noisy ones, while higher 
# thresholds will only detect the most prominent and strong edges. 
# The hysteresis thresholding helps to bridge the gap between these two
# extremes, creating a more robust and continuous edge map.
canny=cv2.Canny(new_img,100,200)
cv2.imshow("canny",canny)
cv2.waitKey(0)

#use subplots() or add_subplot() functions

# Add the first image to the figure (top-left position)
plt.subplot(1, 4, 1)  # 1 row, 3 columns, first position
plt.imshow(new_img, cmap="gray")  
plt.axis('off')  # Hide the axis labels
plt.title("original image") 

# Add the second image to the figure (top-right position)
plt.subplot(1,4,2)  # 1 rows, 3 columns, second position
plt.imshow(gaussian, cmap="gray")  
plt.axis('off')  # Hide the axis labels
plt.title("blurred") 

# Add the third image to the figure (bottom-left position)
plt.subplot(1, 4, 3)  # 1 rows, 3 columns, third position
plt.imshow(canny, cmap="gray") 
plt.axis('off')  # Hide the axis labels
plt.title("edge image")   

plt.show()
cv2.destroyWindow()
