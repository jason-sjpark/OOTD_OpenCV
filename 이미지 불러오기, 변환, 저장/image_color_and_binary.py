import cv2

# 이미지 불러오기, 컬러 출력

img_color = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)  # 이미지 컬러로 읽어오기
# cv2.IMREAD_GRAYSCALE, cv2.IMREAD_UNCHANGED 존재

cv2.namedWindow('Show Image')  # window's name
cv2.imshow('Show Image', img_color)  # window and image

cv2.waitKey(0) # wait for input. if it is 0, it waits for permanent
# cv2.destroyAllWindows() # before exit the program, release window resources.

# 컬러 이미지를 그레이 스케일로 변환 출력

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)  #그레이 스케일로 변환

cv2.imshow('Show GrayScale Image', img_gray)
cv2.waitKey(0)

#cv2.destroyAllWindows()

#이미지 저장하기

cv2.imwrite('savedimage.jpg', img_gray)

cv2.destroyAllWindows()

