import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage.measure import label,regionprops
from skimage.filters import  gaussian, threshold_otsu

sum=0
number=0
for i in range(1,13):
    sum_image=0
    number+=1
    
    image = plt.imread("C:\\Users\\Public\\Pictures\\images\\img ("+str(i)+").jpg")
    image = np.mean(image,2)
    image = gaussian(image, sigma=19)
    threshold = threshold_otsu(image)
    image[image < threshold] = 0
    image[image > 0] = 1
    image = skimage.util.invert(image)
    labeled = label(image)
    regions = regionprops(labeled)

    for i in regions:
        if i.perimeter>5000:
            if i.area>240000:
                if ((i.perimeter**2) / i.area)>79:
                    sum_image+=1

    print(f"Фото № {number}: {sum_image} карандашей")
    sum+=sum_image
print(f"Всего: {sum} карандашей")
