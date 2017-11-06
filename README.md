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
