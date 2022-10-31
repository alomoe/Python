import numpy as np
from skimage.measure import label
from skimage.morphology import binary_erosion

mask = np.array([np.array([[1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1]]),

                  np.array([[1, 1, 0, 0, 1, 1],
                            [1, 1, 0, 0, 1, 1],
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1]]),

                  np.array([[1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 0, 0, 1, 1],
                            [1, 1, 0, 0, 1, 1]]),

                  np.array([[1, 1, 1, 1],
                            [1, 1, 1, 1],
                            [1, 1, 0, 0],
                            [1, 1, 0, 0],
                            [1, 1, 1, 1],
                            [1, 1, 1, 1]]),

                  np.array([[1, 1, 1, 1],
                            [1, 1, 1, 1],
                            [0, 0, 1, 1],
                            [0, 0, 1, 1],
                            [1, 1, 1, 1],
                            [1, 1, 1, 1]])], dtype=object)

image = np.load("C:\\Users\\Public\\Pictures\\ps.npy.txt")  
labeled = label(image)

forms =[0,0,0,0,0]

for i in range(0, len(mask)):
    erosed = binary_erosion(labeled, mask[i])
    erosed = label(erosed1)
    k = erosed.max()
    forms[i]=k
        
print("the number of objects of each type = ", forms)
print("total number of objects = ", sum(forms))
