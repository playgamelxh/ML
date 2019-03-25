#encoding=utf-8
from PIL import Image
import cv2 as cv
from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt

"""
脚本说明：生成二维码
"""

"""
函数说明：生成二维码
"""
def create(str = '', save_path = ''):

    image = ImageCaptcha(width=300, height=80, font_sizes=[52])
    # 生成numpy格式，不保存为本地图片
    # data = image.generate('123abc')
    if save_path == '':
        save_path = "./img/%s.png"%(str)
    # 保存为本地图片
    image.write(str, save_path)
    # X=cv2.imread("out.png")
    # print(X)
    # captcha_image = Image.open(X)
    # captcha_source = np.array(captcha_image)
    # print(captcha_source)


if __name__ == '__main__':

    # create('12te')

    file_path = '/www/ML/other/verification_code/img/12te.png'

    image = cv.imread(file_path)
    cv.namedWindow("input", cv.WINDOW_NORMAL)
    cv.imshow("input", image)

    # 高斯模糊
    image = cv.GaussianBlur(image, (1, 15), 0)
    cv.namedWindow('gaus_blur_image', cv.WINDOW_NORMAL)
    cv.imshow('gaus_blur_image', image)

    image = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.namedWindow("filter", cv.WINDOW_NORMAL)
    cv.imshow("filter", image)

    cv.waitKey(0)
    cv.destroyAllWindows()