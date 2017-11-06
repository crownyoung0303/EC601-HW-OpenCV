import cv2
import numpy as np
import copy

def Gaussian_Noise(img,mean,sigma):
    img_noise = copy.deepcopy(img)
    im = np.zeros(img.shape, np.uint8)
    cv2.randn(im,mean,sigma)
    img_noise=cv2.add(img_noise, im)
    return img_noise

def Salt_and_Pepper_Noise(img,pa,pb):
    row,col,ch = img.shape
    out = copy.deepcopy(img)
    num_salt = row*col*pb
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in img.shape]
    out[coords] = 1
    num_pepper = row*col*pa
    coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in img.shape]
    out[coords] = 0
    return out

def main():
    img_path = "D:/graduate/ec601/opencv/sushi.jpg"
    img = cv2.imread(img_path,1)
    img_gau = Gaussian_Noise(img,0,50)
    img_sp = Salt_and_Pepper_Noise(img,0.01,0.01)
    cv2.imshow("Original", img)
    cv2.imshow("Gaussian Noise", img_gau)
    cv2.imshow("Salt and Pepper Noise", img_sp)
    img_box = cv2.blur(img_gau,(3,3))   
    cv2.imshow("Gaussian Noise Box filter", img_box)
    
    img_gau_filter = cv2.GaussianBlur(img_gau,(3,3),1.5)
    cv2.imshow("Gaussian Noise Gaussian filter", img_gau_filter)
    
    iamge_median = cv2.medianBlur(img_gau,3)
    cv2.imshow("Gaussian Noise Median filter", iamge_median)
       
    img_box = cv2.blur(img_sp,(3,3))   
    cv2.imshow("Salt and Pepper Noise Box filter", img_box)
    
    img_gau_filter = cv2.GaussianBlur(img_sp,(3,3),1.5)
    cv2.imshow("Salt and Pepper Noise Gaussian filter", img_gau_filter)
    
    img_median = cv2.medianBlur(img_sp,3)    
    cv2.imshow("Salt and Pepper Noise Median filter", img_median)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()