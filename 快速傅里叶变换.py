import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# img = cv.imread('FFT.png', 0)  # 直接读为灰度图像
# f = np.fft.fft2(img)  # 做频率变换
# fshift = np.fft.fftshift(f)  # 转移像素做幅度谱
# s1 = np.log(np.abs(fshift))  # 取绝对值：将复数变化成实数取对数的目的为了将数据变化到0-255
# plt.subplot(121)
# plt.imshow(img, 'gray')
# plt.title('original')
# plt.subplot(131)
# plt.imshow(s1, 'gray')
# plt.title('center')
# plt.show()

img = cv.imread('FFT.png', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
res = np.log(np.abs(fshift))

plt.subplot(131), plt.imshow(img, 'gray'), plt.title('Original Image')
plt.axis('off')
plt.subplot(132), plt.imshow(res, 'gray'), plt.title('Fourier Image')
plt.axis('off')

plt.show()
