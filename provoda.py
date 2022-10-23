import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import binary_erosion, binary_dilation, binary_opening

image = np.load("C:\\Users\\Public\\Pictures\\wires6.npy.txt")
labeled = label(image)
mask = np.array([[0,1,0],
                 [0,1,0],
                 [0,1,0]])

for i in range(1, labeled.max() + 1):
    one_wire = np.zeros_like(image)
    one_wire[labeled == i] = 1
    chng = binary_opening(one_wire, mask)
    chng_labeled = label(chng)
    if chng_labeled.max() > 1:
        print(str(i) + " провод порван на " + chng_labeled.max() + " части(-ей)")
    else:
        print(str(i) + " провод не порван")

plt.subplot(121)
plt.imshow(image)
plt.show()
