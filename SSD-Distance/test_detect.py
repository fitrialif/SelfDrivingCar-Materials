import os
import numpy as np
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
slim = tf.contrib.slim
from model import ssd_vgg_512, np_methods
from core import preprocess, visualization
from detection import *

img = mpimg.imread('img/img.jpg')
rclasses, rscores, rbboxes =  process_image(img)

# using matplotlib
visualization.plt_bboxes(img, rclasses, rscores, rbboxes)

# using opencv2
#visualization.bboxes_draw_on_img(img, rclasses, rscores, rbboxes)
#cv2.imwrite("output.jpg", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))


