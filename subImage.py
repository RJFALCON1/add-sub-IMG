import cv2
image3 = cv2.imread('image3.jpeg')
image4 = cv2.imread('image4.jpeg')
newImg = cv2.subtract(image3,image4)
cv2.imwrite('subFile.png',newImg)
cv2.destroyAllWindows()