import cv2

class FaceModel:
    def __init__(self):
        self.fname_ = './data/family.jpg'

    def original(self):
        img = cv2.imread(self.fname_)
        cv2.imshow('face', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()