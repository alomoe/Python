import matplotlib.pyplot as plt
from skimage.filters import sobel
from skimage.morphology import binary_closing, binary_opening
from skimage.measure import label, regionprops
from skimage import color
import numpy as np


image = plt.imread("C:\\Users\\Public\\Pictures\\balls_and_rects.png")

hsv = color.rgb2hsv(image)[:, :, 0]
binary = hsv.copy()
binary[binary > 0] = 1
labeled = label(binary)
regions = regionprops(labeled)

color_r=[]
color_c=[]

for region in regionprops(labeled):
    bb = region.bbox
    val = np.max(hsv[bb[0]:bb[2], bb[1]:bb[3]])
    a, b = bb[2] - bb[0], bb[3] - bb[1]
    if a * b == region.area:
        color_r.append(val)
    else:
        color_c.append(val)

def count_color(color):
    dict_color={}
    for i in color:
        if len(dict_color)>0:
            arg=False
            val1=round(i,1)
            for j in dict_color.keys():
                if val1==round(j,1):
                    dict_color[j]+=1
                    arg=True
            if arg==False:
                dict_color[i]=1
        else:
            dict_color[i]=1
    return dict_color

print('Всего:', np.max(labeled))
print("Квадраты:",len(color_r))
print(count_color(color_r)) 
print("Круги:",len(color_c))
print(count_color(color_c)) 