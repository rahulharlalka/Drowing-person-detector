import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
import time
import numpy as np

webcam= cv2.VideoCapture(0)

if not webcam.isOpened():
    print('could not open webcam')
    exit()

t0=time.time()
centre0=np.zeros(2)
isDrowning=False

while webcam.isOpened():

    status,frame=webcam.read()
    if not status:
        print("could not read frame")
    bbox,label,conf= cv.detect_common_objects(frame)

    if len(bbox)>0:
        bbox=bbox[0]
        centre=[0,0]

        centre=[(bbox[i][0]+bbox[i][2])/2,(bbox[i][1]+bbox[i][3])/2]
        hmov=abs(centre[0]-centre0[0])
        vmov=abs(center[1]-centre0[1])

        x=time.time()
        threshold=10

        if(hmov>threshold or vmov>threshold):
            print(x-t0,'s')
            t0=time.time()
            isDrowning=False

        else:
            print(x-t0, 's')
            if((time.time() - t0) > 10):
                isDrowning = True

        print('bbox: ', bbox, 'centre:', centre, 'centre0:', centre0)
        print('Is he drowning: ', isDrowning)

        centre0 = centre
    # draw bounding box over detected objects

    out = draw_bbox(frame, bbox, label, conf,isDrowning)

    #print('Seconds since last epoch: ', time.time()-t0)

    # display output
    cv2.imshow("Real-time object detection", out)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release resources
webcam.release()
cv2.destroyAllWindows()


