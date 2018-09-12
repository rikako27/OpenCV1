import cv2
import matplotlib.pyplot as plt

#read picture
img = cv2.imread("adult-beautiful-happy-38554.jpg")

#resize photo
#img = cv2.resize(img, (width, height))
resize_img = cv2.resize(img, (600, 300))

#save resized photo
cv2.imwrite("resize-output.jpg", resize_img)

#display
plt.imshow(cv2.cvtColor(resize_img, cv2.COLOR_BGR2RGB))
plt.show()