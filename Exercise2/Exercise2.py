import cv2
import numpy as np
def convert(img_path):
    img = cv2.imread(img_path,1)
    cv2.imshow('Original', img)
       
    # RGB
    (B, G, R) = cv2.split(img)
    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("Blue", B)
    print('the values of the pixel at (20,25) in the RGB:',R[20][25],G[20][25],B[20][25])
    
    # YCrCb
    YCrCb=cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb) 
    (Y, Cb, Cr) = cv2.split(YCrCb)
    cv2.imshow("Y", Y)
    cv2.imshow("Cb", Cb)
    cv2.imshow("Cr", Cr)
    print('the values of the pixel at (20,25) in the YCrCb:',Y[20][25],Cb[20][25],Cr[20][25])
    
    # HSV
    HSV=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    (H, S, V) = cv2.split(HSV)
    cv2.imshow("Hue", H)
    cv2.imshow("Saturation", S)
    cv2.imshow("Value", V)
    print('the values of the pixel at (20,25) in the HSV:',H[20][25],S[20][25],V[20][25])

    # value range
    print('For RGB, value ranges are all: 0-255')   
    print('For YCbCr, value ranges are: 16-235,16-240,16-240')    
    print('For HSV, value ranges are: 0-180,0-255,0-255')
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def main():
    img_path = "D:/graduate/ec601/opencv/sushi.jpg"
    convert(img_path)


if __name__ == '__main__':
  main()

