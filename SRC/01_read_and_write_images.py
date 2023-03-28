import cv2

# Read the image file

image_file = cv2.imread("Images\lena.jpg", 1) 
"""
You can use the flags parameter as 1, -1, 0
"""

print(image_file) # this will give you the matrix of that image 

# TO see the image 
cv2.imshow("image",image_file)

# TO wait till you see the image
k = cv2.waitKey(0)

# Lets us use some conditions

if k == 27:
   cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("Images\lena_copy.jpg",image_file)
    cv2.destroyAllWindows()