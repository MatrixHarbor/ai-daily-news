import numpy as np

img_row1 = [(255,255,255),(0,0,0),(1,1,1)]

img_row2 = [(0,0,0),(255,255,255),(2,2,3)]
# image as a 2-D ndarray of pixels
img = np.array([img_row1,img_row2]) # 2-dimensional list
# img_2 = np.array(img_row1)

# print(img)
# print(img_2)
# row first, and column second -- select an element
print(img[0]) # select the first row

print(img[0,0]) # select the first row and the first column

print(img[0,0,1]) # 1st row & 1st column & 1st element

print(img[:,2]) # get every row for column 1
print(img[1,:]) # get every column for row 1