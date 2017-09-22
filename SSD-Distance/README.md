# SSD-with-Distance
SSD in Tensorflow with virtual distance calculated

![alt text](img/output.png)

Thanks to [Balancap](https://github.com/balancap) for the original SSD in Tensorflow, I just updated the code and add virtual distance feature.

Please, it is not very accurate.

My code not able to train yet, so you need to download model from [here](https://drive.google.com/open?id=0B0qPCUZ-3YwWT1RCLVZNN3RTVEU), create new folder 'checkpoint' and put the pretrained in that folder

To visualize a picture,
```bash
python test_detect.py
```
after you change picture location here,
```python
img = mpimg.imread('img/img.jpg')
```

To process a video,
```bash
python detect_video.py
```
after you change video location and video name to save
```python
cap = cv2.VideoCapture('first.mp4')

fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, cv2.cv.CV_CAP_PROP_FPS, (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))))
```

