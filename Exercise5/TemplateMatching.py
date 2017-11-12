import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = 0;
    var_t = 0;
    location = [0, 0];
    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------ 

    # try:
    #     temp.shape
    #     print("checked for shape".format(img.shape))
    # except AttributeError:
    #     print("shape not found")
    for i in range(temp.shape[0]):
        for j in range (temp.shape[1]):
             mean_t+=temp[i,j]#all the value
    mean_t=mean_t/(temp.shape[0]*temp.shape[1])

    for i in range(temp.shape[0]):
        for j in range(temp.shape[1]):
            var_t+=(temp[i,j]-mean_t)**2/(temp.shape[0]*temp.shape[1])
    print(mean_t,var_t)

    max_corr = 0;
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s = 0;
            var_s = 0;
            corr = 0;
            sum_of_pixels=0;
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------ 
            for a in range(src.shape[0]):
                for b in range(src.shape[1]):
                    mean_s += src[a, b]  # all the value
            mean_s = mean_s / (src.shape[0] * src.shape[1])
            for a in range(src.shape[0]):
                for b in range(src.shape[1]):
                    var_s += (src[a, b] - mean_s) ** 2 / (src.shape[0] * src.shape[1])
            print(mean_s, var_s)
            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------ 
            for k in range(temp.shape[0]):
                for l in range(temp.shape[1]):
                    sum_of_pixels+=(temp[k,l]-mean_t)*(src[i+k,j+l]-mean_s)
            corr=sum_of_pixels/(var_s*var_t)/(temp.shape[0]*temp.shape[1])
            if corr > max_corr:
                max_corr = corr;
                location = [i, j];
    return location

# load source and template images
source_img = cv2.imread('/Users/emanon/Downloads/OpenCV_homework/source_img.jpg',0) # read image in grayscale
temp = cv2.imread('/Users/emanon/Downloads/OpenCV_homework/template_img.jpg',0) # read image in grayscale
location = TemplateMatching(source_img, temp, 20);#step size
print(location)
match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

# Draw a red rectangle on match_img to show the template matching result
# ------------------ Put your code below ------------------
(i,j)=location
(h,w)=temp.shape

match_img=cv2.rectangle(match_img,(i,j),(i+w,j+h),(0,0,255),3)
# Save the template matching result image (match_img)
# ------------------ Put your code below ------------------
#cv2.imwrite('MyTemplateMatching.png',match_img)


# Display the template image and the matching result
cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp)
cv2.imshow('MyTemplateMatching', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()