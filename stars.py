import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import binary_erosion
from scipy.ndimage import morphology


mask1 = [[1, 0, 0, 0, 1],
         [0, 1, 0, 1, 0],
         [0, 0, 1, 0, 0],
         [0, 1, 0, 1, 0],
         [1, 0, 0, 0, 1],]

mask2 = [[0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],]


image = np.load("C:\\Users\\Public\\Pictures\\stars.npy")  
labeled = label(image)

erosed1 = binary_erosion(labeled, mask1)
erosed1 = label(erosed1)

erosed2 = binary_erosion(labeled, mask2)
erosed2 = label(erosed2)

print(erosed1.max() + erosed2.max())
