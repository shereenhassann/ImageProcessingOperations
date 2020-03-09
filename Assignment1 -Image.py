# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from numpy import *
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 

value = 50
multiplicationFactorS = 0.9
multiplicationFactorL = 2
image = cv2.imread("C:\\Users\\shere\\OneDrive\\Desktop\\Jellyfish.jpg")
#cv2.imshow('original', image)
#cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray image', gray)
#cv2.waitKey(0)

subtract = gray - value
#cv2.imshow('Subtraction', subtract)
#cv2.waitKey(0)

add = gray + value
#cv2.imshow('Addition', add)
#cv2.waitKey(0)

multiplyS = gray * multiplicationFactorS
#cv2.imshow('Multiplication Small Factor', multiplyS)
#cv2.waitKey(0)

multiplyL = gray * multiplicationFactorL
#cv2.imshow('Multiplication Large Factor', multiplyL)
#cv2.waitKey(0)

inverted = cv2.bitwise_not(gray)
#cv2.imshow('Inverted', inverted)
#cv2.waitKey(0)
#impImage = mpimg.imread("C:\\Users\\shere\\OneDrive\\Desktop\\Jellyfish.jpg")

fig = plt.figure()

fig.add_subplot(331)
plt.title('Original')
plt.set_cmap('brg')
plt.imshow(image)

fig.add_subplot(332)
plt.title('Gray Scale')
plt.set_cmap('gray')
plt.imshow(gray)

fig.add_subplot(333)
plt.title('Addition')
plt.set_cmap('gray')
plt.imshow(add)

fig.add_subplot(334)
plt.title('Subtraction')
plt.set_cmap('gray')
plt.imshow(subtract)

fig.add_subplot(335)
plt.title('Multiplication small')
plt.set_cmap('gray')
plt.imshow(multiplyS)

fig.add_subplot(336)
plt.title('Multiplication Large')
plt.set_cmap('gray')
plt.imshow(multiplyL)

fig.add_subplot(337)
plt.title('Inverted')
plt.set_cmap('gray')
plt.imshow(inverted)


# Put contours in image and modify the main image
