# EC601-HW-OpenCV
## Exercise 1
Mat img = imread("image.jpg");

A picture is represented by a pixel matrix according to the structure of cvMat:
typedef struct CvMat
{
  int type;    
  int step;
  /* for internal use only */
  int* refcount;
  int hdr_refcount;
  union
  {
    uchar* ptr;
    short* s;
    int* i;
    float* fl;
    double* db;
  } data;
## Exercise 2
the values of the pixel at (20,25) in the RGB: 44 37 31
the values of the pixel at (20,25) in the YCrCb: 38 132 124
the values of the pixel at (20,25) in the HSV: 14 75 44

For RGB, value ranges are all: 0~255
For YCbCr, value ranges are: 16~235,16~240,16~240
For HSV, value ranges are: 0~180,0~255,0~255
