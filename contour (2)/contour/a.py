import numpy as np
import cv2
img = cv2.imread('a.jpg', 0) # Read in your image
# contours, _ = cv2.findContours(...) # Your call to find the contours using OpenCV 2.4.x
contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # Your call to find the contours
#idx = ... # The index of the contour that surrounds your object
mask = np.zeros_like(img) # Create mask where white is what we want, black otherwise
cv2.drawContours(mask, contours, -1, 255, -1) # Draw filled contour in mask
out = np.zeros_like(img) # Extract out the object and place into output image
out[mask == 255] = img[mask == 255]

# Show the output image
cv2.imshow('Output', out)
cv2.imwrite('savedimage.jpg', out)
cv2.waitKey(0)
cv2.destroyAllWindows()