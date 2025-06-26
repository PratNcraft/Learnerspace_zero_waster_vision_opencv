#problem_!
#read an image and apply a custom convolution kernel to sharpen img.
import numpy as np
import cv2
#1. define 3x3 sharpening jernel using numpy and apply using cv2.filter2D
# use laplacian kernel as sharpening filter [[0,-1,0][-1,5,-1][0,-1,0]]
image=cv2.imread("image_1.png")#, cv2.IMREAD_GRAYSCALE)

#--------------------------#
#sharpening array- [[0,-1,0][-1,5,-1][0,-1,0]] 
#--------------------------#
kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
# print(type(arr))

#--------------------------------------#
#cv2.filter2D(src, ddepth, kernel, dst=None,anchor=(-1, -1),
#delta=0, borderType=cv2.BORDER_DEFAULT)
#src:source image (input image) to be filtered.
# ddepth:desired depth of the destination image.
#if -1:output image has same depth as the input image. 
# Other options include cv2.CV_8U, cv2.CV_16S.
#kernel: The convolution kernel (a NumPy array) used for filtering.
#This is a 2D array defining the weights applied during the convolution.
#dst: Optional output image. If not provided, a new image is created.
#anchor: The anchor of the kernel, which indicates the relative position 
# of the filtered pixel within the kernel. (-1, -1) means the anchor is 
# at the kernel's center.
#delta: An optional value added to each pixel during the correlation. 
#borderType: Defines how image borders are handled during the convolution 
#(e.g., cv2.BORDER_DEFAULT, cv2.BORDER_CONSTANT, cv2.BORDER_REPLICATE).
#--------------------------------------#
sharp_img=cv2.filter2D(image, -1,kernel)

#2 display OG and filtered img side by side wiht np.stack()-
# horizontally stacking arrays. This operation concatenates arrays along 
# their second axis (columns) for 2D arrays, or along the first axis for 
# 1D arrays. It is equivalent to using numpy.concatenate() with axis=1. 
# im=np.hstack((image,sharp_img))
# cv2.imshow("sharpened_img", im)
# cv2.waitKey(0)

#--------------------------------------#
# You only need to convert to grayscale for filters like:
# Laplacian, Sobel, Canny
# or any edge detector that is based on intensity changes
# these edge filters: Work on luminance (brightness), not color
# And applying them to RGB directly can give noisy or weird results
#--------------------------------------#

#3 use 2 sobel filters 3x3 kernel for hori and verti edge detection 
#display in 2 diff imgs

#--------------------------------------#
# sobel-tofind edges in an image by calculating the gradient 
# (rate of change) of pixel intensity in particular direction—horiz or verti
# cv2.Sobel(src, ddepth, dx, dy, ksize=3)
#dx	Order of the derivative in x-direction (horizontal)
# dy	Order of the derivative in y-direction (vertical)
# ksize	Size of Sobel kernel (must be 1, 3, 5, or 7)

# You only need to convert to grayscale for filters like:
# Laplacian, Sobel, Canny
# or any edge detector that is based on intensity changes
# these edge filters: Work on luminance (brightness), not color
# And applying them to RGB directly can give noisy or weird results
#--------------------------------------#

gray = cv2.cvtColor(sharp_img, cv2.COLOR_BGR2GRAY)
sobel_hori = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_verti = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

#--------------------------------------#
# Filters like Laplacian, Sobel, etc., return pixel values that 
# can be negative or floating-point.
# But images displayed with OpenCV (cv2.imshow) or 
# saved using cv2.imwrite() must be positive integers (0–255)
#convert into int vals.
#--------------------------------------#
#convert to abs vals for imshow()
sobel_verti=cv2.convertScaleAbs(sobel_verti)
sobel_hori=cv2.convertScaleAbs(sobel_hori)
im=np.hstack((sobel_hori, sobel_verti))
cv2.imshow("horizontal_detect,vertical_detect",im)
cv2.waitKey(0)

cv2.destroyAllWindows()