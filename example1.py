import cv2
import matplotlib.pyplot as plt

#load a classifier from a file
# cascade_file = "haarcascade_frontalface_alt.xml"
# cascade = cv2.CascadeClassifier(cascade_file)

#read image and convert to gray scale
img = cv2.imread("adult-beautiful-happy-38554.jpg")
print(img) #get image data

#openCV == BGR
#matplotlib == RGB
#plt.axis("off")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

#save picture
output_file = "output.jpg"
cv2.imwrite(output_file, img)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 
