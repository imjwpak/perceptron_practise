import cv2
import matplotlib.pyplot as plt
from sklearn import datasets

class HandWriting:
    def __init__(self):
        self.fname_ = datasets.load_digits()

    def read_file(self):
        plt.imshow(self.fname_.images[0], cmap='gray')
        plt.show()