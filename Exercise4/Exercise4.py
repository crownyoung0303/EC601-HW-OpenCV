import cv2
import numpy as np
import copy

def main():
    img_path = "D:/graduate/ec601/opencv/sushi.jpg"
    img = cv2.imread(img_path,1)
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', gray)
    threshold_value = 128
    (T, thresh) = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_TRUNC)
    cv2.imshow("Thresholded Image", thresh)
    #binary
    (T, thresh_binary) = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary Threshold", thresh_binary)
    #band
    (T, thresh_binary_1) = cv2.threshold(gray, 27, 255, cv2.THRESH_BINARY)
    (T, thresh_binary_2) = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)
    band_thresholded_img = cv2.bitwise_and(thresh_binary_1,thresh_binary_2)
    cv2.imshow("Band Thresholding", band_thresholded_img)
    #Semi
    ret2,Semi = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    Semi = cv2.bitwise_and(gray,Semi)
    cv2.imshow("Semi Thresholding", Semi)
    #Adaptive
    adaptive_thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,101,10)
    cv2.imshow("Adaptive Thresholding", adaptive_thresh)
    cv2.waitKey(0)

if __name__ == '__main__':
  main()