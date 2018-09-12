import cv2
import matplotlib.pyplot as plt

#read image
img = cv2.imread("adult-beautiful-happy-38554.jpg")

#cut photo
cut_img = img[0:2000, 1000:2000]

#save resized photo
cv2.imwrite("cut-output.jpg", cut_img)

#display
plt.imshow(cv2.cvtColor(cut_img, cv2.COLOR_BGR2RGB))
plt.show()