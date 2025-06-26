#problem2
import matplotlib.pyplot as plt
import cv2
#1 load a grayscale img and display its histogram using matplotlib
image=cv2.imread("image_1.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("img",image)
plt.hist(image.ravel(),256,[0,256])   
plt.show()
#histogram
# for cv2-syntax-cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
# hist = cv2.calcHist([image],[0],None,[256],[0,256]) #0 means gray

# usijng numpy-hist,bins = np.histogram(img.ravel(),256,[0,256])

# for matplotlib- plt.hist(img.ravel(),256,[0,256]); plt.show()
# hist=plt.hist(image.ravel(), 256,[0,256]) #[0,256 is range of color pixels, 
# 256 is range of graph.

#2. apply histo equaisation using cv2.equalizeHist() and display it
#syntax-equalized_image = cv2.equalizeHist(src)
# equalizeHist() aims to create an output image where the pixel intensities 
# are more evenly distributed, leading to improved overall contrast.
equalized_image = cv2.equalizeHist(image)
cv2.imshow("equalised img", equalized_image)
cv2.waitKey(0)   

#3. plot histo of equalised img and compare to OG

plt.hist(equalized_image.ravel(),256,[0,256])  
plt.show()
#we see that the columns in histo are more spreadout evenly.
cv2.destroyAllWindows()