# EC601-HW-OpenCV
## Exercise 1
Mat img = imread("image.jpg");

A picture is represented by a pixel matrix according to the structure of cvMat:<br />
typedef struct CvMat<br />
{<br />
  int type;<br />
  int step;<br />
  /* for internal use only */<br />
  int* refcount;<br />
  int hdr_refcount;<br />
  union<br />
  {<br />
    uchar* ptr;<br />
    short* s;<br />
    int* i;<br />
    float* fl;<br />
    double* db;<br />
  } data;<br />
## Exercise 2
the values of the pixel at (20,25) in the RGB: 44 37 31<br />
the values of the pixel at (20,25) in the YCrCb: 38 132 124<br />
the values of the pixel at (20,25) in the HSV: 14 75 44<br />
<br />
For RGB, value ranges are all: 0-255<br />
For YCbCr, value ranges are: 16-235,16-240,16-240<br />
For HSV, value ranges are: 0-180,0-255,0-255<br />
## Exercise 3
As the kernel size increases, the image will become more and more blurring.<br />

As for filtering the noises, Median filter works better for salt-and-pepper noise.<br />

Gaussian filter works better for gaussian noise.<br />
## Exercise 4
For the binary threshold, it converts the original image only using black and white two colors.

For the semi threshold, it is the contrast image of the original one.

For the band threshold, it sets the upper band and the lower band of color which can filter some colors.

For the adaptive threshold, it looks like a sketch of the original one extracting most of the information.

The disadvantage of the binary threshold:
The performance of binary threshold may depends on the lighting conditions, if it is too dark or too bright, it may have a bad result.

The advantage of the adaptive threshold:
The adaptive threshold can use multiple thresholds which can find the best threshold according to different lighting conditions and result in a good performance in many cases.
