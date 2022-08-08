import cv2

skyImg = cv2.imread('1.jpg',1)
rplogoImg = cv2.imread('2.png',1)

## Image info
print('===== Original Image Info =====')
print('Sky Image : ', skyImg.shape)
print('RP Image  : ', rplogoImg.shape)

## Image Resize
rp = cv2.resize(rplogoImg, None, fx=0.9, fy=0.9, interpolation=cv2.INTER_AREA)

print('===== Resized RP Logo Image Info =====')
print('RP Image  : ', rp.shape)

## Image Addition
x_offset = y_offset = 10

for c in range(0,2):
    skyImg[y_offset:y_offset+rp.shape[0], x_offset:x_offset+rp.shape[1],c] = \
    rp[:,:,c] * (rp[:,:,2]/255.0) + \
    skyImg[y_offset:y_offset+rp.shape[0], x_offset:x_offset+rp.shape[1],c] * (1.0 - rp[:]/255.0)
## Result
cv2.imshow('Sky with RP Logo', skyImg)
cv2.waitKey(0)

cv2.destroyAllWindows()