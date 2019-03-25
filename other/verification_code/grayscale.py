#encoding=utf-8
from PIL import Image,ImageDraw
from PIL import  ImageEnhance
from PIL import  ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

'''
脚本说明：灰度化
1. 分量法 在rgb三个分量种按照需求选取一个分量作为灰度值
2. 最大值 选取rgb的最大值作为该pixel的灰度值
3. 平均值 g[i,j] = (r[i,j] + g[i,j] + b[i,j]) / 3,取rgb的平均值作为灰度值
4. 加权变换 由于人眼对绿色的敏感最高，对蓝色敏感最低，因此，按下式对RGB三分量进行加权平均能得到较合理的灰度图像。
    g[i,j] = 0.3*r[i,j] + 0.59*g[i,j] + 0.11*b[i,j]
'''


class Grayscale:

    # 原图片路径
    file_path = ''

    #处理后图片路径
    save_path = ''

    def __init__(self, file_path='', save_path=''):
        self.file_path = file_path
        self.save_path = save_path

    def set_path(self, file_path=''):
        self.file_path = file_path

    '''
    函数说明：灰度化
    '''
    def component_method(self, type='r'):
        #  1 (1-bit pixels, black and white, stored with one pixel per byte)1位像素，黑白，每字节一个像素存储
        #  L (8-bit pixels, black and white)8位像素，黑白
        #  P (8-bit pixels, mapped to any other mode using a colour palette)8位像素，使用调色板映射到任何其他模式
        #  RGB (3x8-bit pixels, true colour)3x8位像素，真彩色
        #  RGBA (4x8-bit pixels, true colour with transparency mask)4x8位像素，带透明度掩模的真彩色
        #  CMYK (4x8-bit pixels, colour separation)4x8位像素，分色
        #  YCbCr (3x8-bit pixels, colour video format)3x8位像素，彩色视频格式
        #  I (32-bit signed integer pixels)32位有符号整数像素
        #  F (32-bit floating point pixels)32位浮点像素
        img = Image.open(self.file_path).convert('L')
        plt.imshow(img)
        plt.show()

    '''
    函数说明：去噪点
    '''
    def remove_noise_method(self):
        # 打开图片
        image = Image.open(self.file_path)

        # 将图片转换成灰度图片
        image = image.convert("1")

        # 去噪,G = 50,N = 4,Z = 4
        self.clear_noise(image, 50, 3, 3)

        # 保存图片
        # image.save("d:/result.jpg")

        plt.imshow(image)
        plt.show()

    # 二值判断,如果确认是噪声,用改点的上面一个点的灰度进行替换
    # 该函数也可以改成RGB判断的,具体看需求如何
    def get_pixel(self, image, x, y, G, N):
        L = image.getpixel((x, y))
        if L > G:
            L = True
        else:
            L = False

        nearDots = 0
        if L == (image.getpixel((x - 1, y - 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x - 1, y)) > G):
            nearDots += 1
        if L == (image.getpixel((x - 1, y + 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x, y - 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x, y + 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x + 1, y - 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x + 1, y)) > G):
            nearDots += 1
        if L == (image.getpixel((x + 1, y + 1)) > G):
            nearDots += 1

        if nearDots < N:
            return image.getpixel((x, y - 1))
        else:
            return None

    # 降噪
    # 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
    # G: Integer 图像二值化阀值
    # N: Integer 降噪率 0 <N <8
    # Z: Integer 降噪次数
    # 输出
    #  0：降噪成功
    #  1：降噪失败
    def clear_noise(self, image, G, N, Z):
        draw = ImageDraw.Draw(image)

        for i in range(0, Z):
            for x in range(1, image.size[0] - 1):
                for y in range(1, image.size[1] - 1):
                    color = self.get_pixel(image, x, y, G, N)
                    if color != None:
                        draw.point((x, y), color)


if __name__ == '__main__':

    # file_name = '/www/ML/other/verification_code/img/qin.png'
    file_name = '/www/ML/other/verification_code/img/12te.png'
    save_path = '/www/ML/other/verification_code/img/save.png'
    grayscale = Grayscale(file_name)
    grayscale.component_method()
    #
    # # file_name = '/www/ML/other/verification_code/img/1.jpg'
    # grayscale.set_path(file_name)
    #
    # # 去噪点
    grayscale.remove_noise_method()



    # opencv处理
    # file_name = '/www/ML/other/verification_code/img/1.jpg'
    # # file_name = '/www/ML/other/verification_code/img/12te.png'
    # image = cv.imread(file_name)
    # cv.namedWindow('input_image', cv.WINDOW_NORMAL)
    # cv.imshow('input_image', image)
    #
    # # 高斯模糊
    # # image = cv.GaussianBlur(image, (1, 15), 0)
    # # cv.namedWindow('gaus_blur_image', cv.WINDOW_NORMAL)
    # # cv.imshow('gaus_blur_image', image)
    #
    # 边缘保留滤波EPF 均值漂移
    # image = cv.pyrMeanShiftFiltering(image, 10, 50)
    # cv.namedWindow("shift_demo", cv.WINDOW_NORMAL)
    # cv.imshow("shift_demo", image)
    #
    # # 把输入图像灰度化
    # gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # # 直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    # ret, image = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    # print("threshold value %s" % ret)
    # cv.namedWindow("binary0", cv.WINDOW_NORMAL)
    # cv.imshow("binary0", image)
    #
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # file_name = '/www/ML/other/verification_code/img/12te.png'
    # save_path = '/www/ML/other/verification_code/img/save.png'
    # image = Image.open(file_name)
    # image = image.filter(ImageFilter.MedianFilter())
    # enhancer = ImageEnhance.Contrast(image)
    # image = enhancer.enhance(2)
    # image = image.convert('1')
    # image.save(save_path);
    #
    # image = cv.imread(file_name)
    # cv.namedWindow("input", cv.WINDOW_NORMAL)
    # cv.imshow("input", image)
    #
    # image = cv.imread(save_path)
    # cv.namedWindow("output", cv.WINDOW_NORMAL)
    # cv.imshow("output", image)

    # cv.waitKey(0)
    # cv.destroyAllWindows()
