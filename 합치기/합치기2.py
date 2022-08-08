import cv2
s_img = cv2.imread("1.jpg")
l_img = cv2.imread("2.png")
x_offset=y_offset=50
s_img = l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]]

s_img = cv2.imread("1.jpg", -1)

y1, y2 = y_offset, y_offset + s_img.shape[0]
x1, x2 = x_offset, x_offset + s_img.shape[1]

alpha_s = s_img[:, :, 2] / 255.0
alpha_l = 1.0 - alpha_s

for c in range(0, 2):
    l_img[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] +
                              alpha_l * l_img[y1:y2, x1:x2, c])