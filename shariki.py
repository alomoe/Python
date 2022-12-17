import cv2
import random
import numpy as np
import time

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
cam.set(cv2.CAP_PROP_EXPOSURE, -4)
cam.set(cv2.CAP_PROP_AUTO_WB,0)

color_str=['blue','yellow']

yellow_lower = np.array([11,180,175])
yellow_upper = np.array([30,240,245])

red_lower = np.array([0,200,155])
red_upper = np.array([10,250,200])

blue_lower = np.array([80,230,100])
blue_upper = np.array([150,255,170])

time_start = 0
x_start=0
y_start=0
random.shuffle(color_str)

def speed(time_start,time_end,x_start,y_start,x,y):
            length=((x - x_start)**2+(y - y_start)**2)**0.5
            k = 53 / (2*radius)
            speed=length*k/(time_end-time_start)
            return speed

def contours(hsv, lower, upper):
    mask=cv2.inRange(hsv, lower, upper)
    contours=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

while cam.isOpened():
    _, frame = cam.read()
    frame = cv2.GaussianBlur(frame, (21,21), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    contours_r, _ = contours(hsv, red_lower, red_upper)
    contours_b, _ = contours(hsv, blue_lower, blue_upper)
    contours_y, _ = contours(hsv, yellow_lower, yellow_upper)

    posledov={}

    if len(contours_r) > 0:
        c = max(contours_r, key=cv2.contourArea)
        (x,y), radius = cv2.minEnclosingCircle(c)
        if radius > 20:
               cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 0)
               color="red"
               posledov[color]=x
           
    if len(contours_b) > 0:
        c = max(contours_b, key=cv2.contourArea)
        (x,y), radius = cv2.minEnclosingCircle(c)
        if radius > 20:
               cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 0)
               color="blue"
               posledov[color]=x
                
    if len(contours_y) > 0:
        c = max(contours_y, key=cv2.contourArea)
        (x,y), radiusy = cv2.minEnclosingCircle(c)
        if radiusy > 20:
              cv2.circle(frame, (int(x), int(y)), int(radiusy), (0,255,255), 0)
              color="yellow"
              posledov[color]=x


    sorted_posledov = sorted(posledov,key=posledov.get)

    if len(sorted_posledov)==1:
        time_end=time.time()
        spd=speed(time_start,time_end,x_start,y_start,x,y)
        x_start=x
        y_start=y
        time_start=time_end
        cv2.putText(frame,f"speed = {spd}", (10,460), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0))

    count=0
    
    for i in range(0,len(sorted_posledov)):
        if sorted_posledov[i]==color_str[i]:
            count+=1

    if count==2:
        cv2.putText(frame,f"perfect!", (10,30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0))
    else:
        cv2.putText(frame,f"make a combination!", (10,30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0))
        

    cv2.imshow("Image", frame)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
