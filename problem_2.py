#2d numpy array size(20,20), random int bw(0,225]
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)#ensures same values next time when executed
arr1=np.random.randint(0,225, size=(20,20))


#3 create greyscale img, horizonatl grad(0-225 L->R)
#and other vertical grad(0->225 top to bottom) of size
#(256,256)pixels and display them

#------------------------------#
#  Generate 1D arrays that increase or decrease at 
# regular intervals with numpy.linspace() 
# //to creat ethe gradient scale
#print(np.linspace(0, 10, 4))
# [ 0.          3.33333333  6.66666667 10.        ]

# Arrange it in 2D with numpy.tile()
# //to replicate in each row
# a = np.array([0, 1, 2, 3])
# print(np.tile(a, (3, 2)))
# [[0 1 2 3 0 1 2 3]
#  [0 1 2 3 0 1 2 3]
#  [0 1 2 3 0 1 2 3]]
#------------------------------#

#horizontal grad 
hori_img=np.tile(np.linspace(0,225,256),(256,1))
#plt.imshow(hori_img, cmap="gray", interpolation="nearest")

#vertical grad
vert_img=np.tile(np.linspace(0,224,256).reshape(256,1),(1,256))
#plt.imshow(vert_img, cmap="gray", interpolation="nearest")

# Plot both images side by side
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].imshow(hori_img, cmap="gray", interpolation="nearest")
axs[0].set_title("Horizontal Gradient")
axs[0].axis("off")

axs[1].imshow(vert_img, cmap="gray", interpolation="nearest")
axs[1].set_title("Vertical Gradient")
axs[1].axis("off")

plt.tight_layout()

plt.show()



#2.generate and display img that has to be created using numpy 
# arr after resizing to (200,200). use nearest neighbour 
# interpolation to inc pixel to (10x10) of same val, and 
# no smoothing or avg is applied to that
# resized_arr = arr.repeat(10, axis=0).repeat(10, axis=1)  # Each pixel becomes a 10x10 block

#---to print the matrix--------#
# for i in range(20):
#     for j in range(20):
#         print(arr1[i][j])
#------------------------------#



#1. calc max, min and median of each row and colmn separately
#------------------------------#
#arr1[i] gives you the i-th row.
# arr1[:, j] gives you the j-th column.

# np.max(), np.min(), and np.median() compute 
#------------------------------#

#for rows and cols
for i in range(20):#accessing rows
    row=arr1[i]
    print(f"\nrow {i+1}:max={np.max(row)}, min={np.min(row)}, median={np.median(row)}")
#------------------------------#
#f-string lets you embed Python expressions directly inside 
# string literals, using curly braces {}.
# name = "Alice"
# age = 25
# print(f"My name is {name} and I am {age} years old.")
#------------------------------#

for j in range(20):#accessing colmn
    col=arr1[:,j]
    print(f"\ncol {j+1}:max={np.max(col)}, min={np.min(col)}, median={np.median(col)}")