# -*- coding: utf-8 -*-
import math

if __name__ == "__main__":
    learning_rate = 0.01
    for a in range(1, 100):
        cur = 0
        for i in range(1, 120):
            cur -= learning_rate * (cur * cur - a)
            # cur -= (a / 100) * (cur * cur - a)
        print("%d的平方根近似为%.8f,真实值为%.8f" % (a, cur, math.sqrt(a)))
