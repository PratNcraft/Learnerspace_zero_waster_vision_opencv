#problem 5
import cv2
#1. read colored image and convert it into hsv channel
#a) split the hsv into 3 channels- H, S, V
#b) display all 3 channels separately (3 diff imgs, 1 channel at a time)
image=cv2.imread("landscape.png")
image_hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imshow("OG_img", image)
# cv2.imshow("hsv_img", image_hsv)
# cv2.waitKey(0)

#a
h,s,v= cv2.split(image_hsv)

#b
cv2.imshow("Hue",h)
cv2.waitKey(0)
cv2.imshow("Saturation",s)
cv2.waitKey(0)
cv2.imshow("value",v)
cv2.waitKey(0)


#2. load a color img and convert from bgr to hsv and reconvert to bgr 
# display all 3 imgs: Og, HSV, recvted BGR.
# observe if reocnverted img looks similar to OG img or not.
# img_1=cv2.imread("image.img")
img_hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
img_bgr=cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("OG_img", image)
cv2.imshow("hsv_img", img_hsv)
cv2.imshow("reverted_img", img_bgr)
#reverted image is as same as original image when looked, but the pixel values can be slightly different(~1)

cv2.waitKey(0)
cv2.destroyAllWindows()