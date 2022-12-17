import cv2
import random
import numpy as np
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
cam.set(cv2.CAP_PROP_EXPOSURE, -4)
cam.set(cv2.CAP_PROP_AUTO_WB,0)

color_str=['red','blue','yellow']

yellow_lower = np.array([11,180,175])
yellow_upper = np.array([30,240,245])

red_lower = np.array([0,200,155])
red_upper = np.array([10,250,200])

blue_lower = np.array([80,230,100])
blue_upper = np.array([150,255,170])

random.shuffle(color_str)
print(color_str)
while cam.isOpened():
    
    
    _, frame = cam.read()
    frame = cv2.GaussianBlur(frame, (21,21), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
    mask_blue = cv2.inRange(hsv, blue_lower,blue_upper)
    mask_red = cv2.inRange(hsv, red_lower,red_upper)
    mask_yellow = cv2.inRange(hsv, yellow_lower,yellow_upper)

    contours_r, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_b, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_y, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    color1=None
    color2=None
    color3=None
    posledov={}

    for i in range(0,3):
        if len(contours_r) > 0:
            cr = max(contours_r, key=cv2.contourArea)
            (xr,yr), radiusr = cv2.minEnclosingCircle(cr)
            if radiusr > 20:
                cv2.circle(frame, (int(xr), int(yr)), int(radiusr), (0,255,255), 0)
                color1="red"
                posledov[color1]=xr
        if len(contours_b) > 0:
            cb = max(contours_b, key=cv2.contourArea)
            (xb,yb), radiusb = cv2.minEnclosingCircle(cb)
            if radiusb > 20:
                cv2.circle(frame, (int(xb), int(yb)), int(radiusb), (0,255,255), 0)
                color2="blue"
                posledov[color2]=xb
        if len(contours_y) > 0:
            cy = max(contours_y, key=cv2.contourArea)
            (xy,yy), radiusy = cv2.minEnclosingCircle(cy)
            if radiusy > 20:
                cv2.circle(frame, (int(xy), int(yy)), int(radiusy), (0,255,255), 0)
                color3="yellow"
                posledov[color3]=xy
    sorted_tuple = sorted(posledov,key=posledov.get)
    count=0
    for i in range(0,len(sorted_tuple)):
        if sorted_tuple[i]==color_str[i]:
            count+=1

    if count==3:
        cv2.putText(frame,f"perfect!", (10,30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0))

    cv2.imshow("Image", frame)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break

cv2.destroyAllWindows()