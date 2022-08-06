import cv2
image1=cv2.imread('image1.jpeg')
image2=cv2.imread('image2.jpeg')
newImage = cv2.addWeighted(image1,0.3,image2,0.7,0)
cv2.imwrite('finalImg.png',newImage)
cv2.destroyAllWindows()