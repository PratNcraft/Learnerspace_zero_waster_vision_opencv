#problem_4
import cv2
import numpy as np
# 1.read image and ocnvert it into grayscale. count no. of pixels 
# having brightness greater than certain threshold(>200). highlight 
# these bright pixels by drawing white dots at their postn on img
image=cv2.imread("image_1.png")
new_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image.shape) 
#find brightness level
#----------------------------------------------------#
#use -np.where(gray > threshold): for grayscale img (2-D array)-
# This returns the coordinates (Y, X) of all pixels where the condition is True.
#(y_coords, x_coords)  # NOT (x, y) !!!!!
# bright_pixels[0] contains all Y (row) indices.
# bright_pixels[1] contains all X (column) indices.
# we get them as(array of y coords, array of x_coords)
#eg- coords = (array([10, 15, 20]), array([5, 25, 35])) we get
# coords are(10,5),(15,25), (20,35) we need

# {
#for rgb image(3-D array), it gives varied answer, as it has to comare to 3 diff 
# values r, g, b. 
#bright_pixels[0]   y- coord
#bright_pixels[1]   x-coord
#bright_pixels[0-2] channel index; 0-b, 1-g, 2-r   
# }
#----------------------------------------------------#
brightness=200
bright_pixels=np.where(new_image>brightness) #returns tuple contains coords of y and x
num1=len(bright_pixels[0]) #getting no. of pixels in it (using only the y axis coord nos.)

#accessing all elements in bright_pixels-

#but they are stored separately in diff tuples as y and x coords
# *coords unpacks the tuple into separate arguments
# zip(...) pairs them element-wise
for y,x in zip(*bright_pixels):     #as its stores as (y_coord,x_coord)
                 #(src,centre,rad,color,thickness)
      cv2.circle(new_image,(x,y),1,(255,255,255),1)  #circle takes vals as x and y coord

cv2.imshow("brighter_img",new_image)

#2.read image in colored format and 
#a) (x1,y1,x2,y2) draw boxes on img of co-od:[(50,60,150,120),
# (200,180,300,250)]
#b) label each box with name "obj1"&2'
#c) display final img with all annotations

#-----------------------------------------------#
#my original image has size (171, 295, 3), hence the 2nd tuple won;'t work 
#on it, hence willhave to resize it
#syntax- resized_image = cv2.resize(src, dsize, fx=0, fy=0, interpolation=cv2.INTER_LINEAR)
# dsize: tuple representing the desired output size, (width, height). 
# fx (optional): Scale factor along the horizontal axis. If dsize provided and fx is 0, 
# fx is calculated based on dsize.width and src.width.
# fy (optional): Scale factor along the vertical axis. If dsize provided and fy is 0, fy 
# is calculated based on dsize.height and src.height.
#-----------------------------------------------#

#-----------------------------------------------#
#image, text string, starting point (e.g., top-left corner of the 
# rectangle minus some offset for visibility), font type, font scale, 
# color, and thickness as arguments.
#-----------------------------------------------#
resize=cv2.resize(image,None,fx=2,fy=2)
font_1=cv2.FONT_HERSHEY_COMPLEX_SMALL
coords=[(50,60,150,120),(200,180,300,250)]    
x=1 #to change object number (object#  #=1,2)
for i in coords:
       cv2.rectangle(resize,(i[0],i[1]),(i[2],i[3]),(0,0,0),1) 
                            # src,2 corners, color, thickness
       cv2.putText(resize, f"object{x}",(i[0],i[1]-5),font_1, 1, (0,0,0),1)
       x+=1

cv2.imshow("final_img",resize)
#3 create a blank image size 500x500 and-
#a) drraw red rect(w/o infill), green circle (with infill), blue diagonal
#line on it
#b) add your name as watermark in bottom-right corner. 
#c) save and display it

# numpy.zeros(shape, dtype=float, order='C', *, like=None)
#a
blank=np.zeros((500,500,3),dtype=np.uint8,)

#b
cv2.rectangle(blank,(100,50),(400,400),(0,0,255),1)
cv2.circle(blank, (250,250), 100,(0,255,0),-1 )
cv2.line(blank,(10,10),(450,450), (255,0,0),1)

#c
font_2=cv2.FONT_HERSHEY_PLAIN
cv2.putText(blank, "Pratusha Pudakalkatti",(300,495),  font_2, 1, (255,255,255), 1, cv2.LINE_AA)
# cv2.imwrite(filename, image)-
# filename-name of the file to save the image as, including its extension
cv2.imwrite("design.png", blank)   #save it
shapes=cv2.imread("design.png")    #display it
cv2.imshow("figures",shapes )
cv2.waitKey(0)
cv2.destroyAllWindows()