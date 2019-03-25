#encoding=utf-8
import numpy as np
import cv2 as cv
"""
脚本说明：opencv包的模糊函数
模块安装： pip install opencv-python
"""

"""
均值模糊    去随机噪声有很好的去燥效果
均值滤波是典型的线性滤波算法，它是指在图像上对目标像素给一个模板，该模板包括了其周围的临近像素
（以目标像素为中心的周围8个像素，构成一个滤波模板，即去掉目标像素本身），
再用模板中的全体像素的平均值来代替原来像素值
"""
def blur_demo(image):
    # （1, 15）是垂直方向模糊，（15， 1）还水平方向模糊
    dst = cv.blur(image, (2, 15))
    cv.namedWindow('blur_demo', cv.WINDOW_NORMAL)
    cv.imshow("blur_demo", dst)

"""
中值模糊  对椒盐噪声有很好的去燥效果
中值滤波法是一种非线性平滑技术，它将每一像素点的灰度值设置为该点某邻域窗口内的所有像素点灰度值的中值
中值（又称中位数）是指将统计总体当中的各个变量值按大小顺序排列起来，形成一个数列，处于变量数列中间位置的变量值就称为中位数。
"""
def median_blur_demo(image):
    dst = cv.medianBlur(image, 5)
    cv.namedWindow('median_blur_demo', cv.WINDOW_NORMAL)
    cv.imshow("median_blur_demo", dst)

# 用户自定义模糊
def custom_blur_demo(image):
    # 除以25是防止数值溢出
    kernel = np.ones([5, 5], np.float32)/25
    dst = cv.filter2D(image, -1, kernel)
    cv.namedWindow('custom_blur_demo', cv.WINDOW_NORMAL)
    cv.imshow("custom_blur_demo", dst)

"""
加高斯噪声
"""
def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]   #blue
            g = image[row, col, 1]   #green
            r = image[row, col, 2]   #red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.namedWindow("noise image", cv.WINDOW_NORMAL)
    cv.imshow("noise image", image)
    dst = cv.GaussianBlur(image, (15, 15), 0)  # 高斯模糊
    cv.namedWindow("Gaussian", cv.WINDOW_NORMAL)
    cv.imshow("Gaussian", dst)

"""
函数说明：异常值处理
"""
def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv

"""
边缘保留滤波EPF
"""
"""
双边滤波（Bilateral filter）
双边滤波是一种非线性的滤波方法，是结合图像的空间邻近度和像素值相似度的一种折中处理，
同时考虑空域信息和灰度相似性，达到保边去噪的目的。双边滤波器顾名思义比高斯滤波多了一个高斯方差sigma－d，
它是基于空间分布的高斯滤波函数，所以在边缘附近，离的较远的像素不会太多影响到边缘上的像素值，这样就保证了
边缘附近像素值的保存。但是由于保存了过多的高频信息，对于彩色图像里的高频噪声，双边滤波器不能够干净的滤掉，
只能够对于低频信息进行较好的滤波
"""
def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.namedWindow("bi_demo", cv.WINDOW_NORMAL)
    cv.imshow("bi_demo", dst)

"""
均值漂移
"""
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.namedWindow("shift_demo", cv.WINDOW_NORMAL)
    cv.imshow("shift_demo", dst)


# 全局阈值
def threshold_demo(image):
    # 把输入图像灰度化
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # 直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print("threshold value %s"%ret)
    cv.namedWindow("binary0", cv.WINDOW_NORMAL)
    cv.imshow("binary0", binary)

# 局部阈值
def local_threshold(image):
    # 把输入图像灰度化
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # 自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary =  cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 25, 10)
    cv.namedWindow("binary1", cv.WINDOW_NORMAL)
    cv.imshow("binary1", binary)

# 用户自己计算阈值
def custom_threshold(image):
    # 把输入图像灰度化
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    h, w =gray.shape[:2]
    m = np.reshape(gray, [1,w*h])
    mean = m.sum()/(w*h)
    print("mean:",mean)
    ret, binary =  cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.namedWindow("binary2", cv.WINDOW_NORMAL)
    cv.imshow("binary2", binary)


if __name__ == '__main__':

    file_path = '/www/ML/other/verification_code/img/qin.png'
    # file_path = '/www/ML/other/verification_code/img/1.jpg'

    src = cv.imread(file_path)
    # # 加高斯噪点
    # gaussian_noise(src)
    cv.namedWindow('input_image', cv.WINDOW_NORMAL)
    cv.imshow('input_image', src)
    #
    # # 均值模糊
    # blur_demo(src)
    # # 中值模糊
    # median_blur_demo(src)
    # # 自定义模糊
    # custom_blur_demo(src)
    #
    # # 高斯模糊
    # # gaussian_noise(src)
    # dst = cv.GaussianBlur(src, (15, 15), 0)  # 高斯模糊
    # cv.namedWindow("Gaussian Blur", cv.WINDOW_NORMAL)
    # cv.imshow("Gaussian Blur", dst)

    # # 双边滤波
    # bi_demo(src)
    #
    # # 均值漂移
    # shift_demo(src)
    #
    # # 全局阈值
    # threshold_demo(src)
    # # 局部阈值
    # local_threshold(src)
    # # 用户自己计算阈值
    # custom_threshold(src)

    cv.waitKey(0)
    cv.destroyAllWindows()