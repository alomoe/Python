import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import erosion

def count_lakes_and_bays(region): 
    symbol = ~region.image
    labeled = label(symbol)
    lakes = 0
    bays = 0
    for reg in regionprops(labeled):
        is_lake = True
        for y, x in reg.coords: 
            if (y == 0 or x == 0) | (y == region.image.shape[0] - 1) | (x == region.image.shape[1] - 1):
                is_lake = False
                break
        lakes += is_lake
        bays += not is_lake             
    return lakes, bays


def has_vline(image): 
    return 1 in erosion(np.mean(image, 0), [1, 1, 1])

def has_hline(image): 
    return 1 in np.mean(image, 1)

def recognize(image_region):
    lakes, bays = count_lakes_and_bays(image_region)
    if lakes == 2:
        if has_vline(image_region.image):
            return 'B'
        else:
            return '8'
    elif lakes == 1:
        if bays == 4:
            return '0'
        elif bays == 2:
            if ((image_region.perimeter**2) / image_region.area) < 59:
                return 'P'
            else:
                return 'D'
        else:
            return 'A'   
    elif lakes == 0:
        if np.mean(image_region.image) == 1.0:
            return '-'
        elif has_vline(image_region.image):
            return '1'
        elif bays == 2:
            return '/'
        elif has_hline(image_region.image):
            return '*'
        elif bays == 4:
            return 'X'
        else:
            return 'W'
            

image = plt.imread("C:\\Users\\Public\\Pictures\\symbols.png")
image = np.mean(image,2)

image[image > 0] = 1
labeled = label(image)

regions = regionprops(labeled)
result = {}
summ=0
for reg in regions:
    symbol = recognize(reg)
    if symbol not in result:
        result[symbol] = 0
    result[symbol] += 1
    summ+=1
interest = {}
for res in result:
    interest[res]=str(((result[res])/summ)*100)+"%"
print (result)
print(interest)
plt.show()
