import cv2
import pytesseract as tess
from PIL import Image
import math
import numpy as np


class MapProcessor:

    def __init__(self, map):
        self.original = cv2.imread(map)
        self.gray_map = cv2.imread(map, 0)

    def make_processing(self):
        thres = self.prepare_map_to_process(self.gray_map)
        items = self.find_contours(thres)
        digi_array = self.make_digital_array(items)
        return digi_array


    def prepare_map_to_process(self, image):
        blur = cv2.blur(image, (2, 2))
        _, thres = cv2.threshold(blur, 230, 255, cv2.THRESH_BINARY)

        return thres

    def find_contours(self, threshold_imgage):

        im2, contours, hierarchy = cv2.findContours(threshold_imgage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        font = cv2.FONT_HERSHEY_SIMPLEX
        items = []

        for i in contours:
            area = cv2.contourArea(i)
            # if area > 1500 and area < 3850:
            if 1500 < area < 3850:
                x, y, w, h = cv2.boundingRect(i)

                # cv2.rectangle(self.original, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # cv2.imshow("elo", self.original)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()

                roi = threshold_imgage[y:y + h, x:x + w]
                items.append(roi)

        return items

    def make_digital_array(self, items):

        digital_array = []
        items = np.asarray(items)

        for i in items:
            if 0 not in i:
                digital_array.append(0)
                continue

            to_ocr = Image.fromarray(i)
            r = tess.image_to_string(to_ocr, lang='eng', boxes=False,
                                     config='--psm 10 --eom 3 -c tessedit_char_whitelist=0123456789')
            if r == '':
                digital_array.append(0)
            else:
                digital_array.append(int(r))

        dim = int(math.sqrt(len(digital_array)))
        res = list(reversed(digital_array))
        a = np.asarray(res)
        b = np.reshape(a, newshape=(dim, dim))

        return b






