import cv2

img_color = cv2.imread('image2.jpg', cv2.IMREAD_COLOR)

cv2.imshow('Color', img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray', img_gray)
cv2.waitKey(0)

ret, img_binary = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary", img_binary)
cv2.waitKey(0)


cv2.destroyAllWindows()