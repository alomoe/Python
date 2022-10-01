import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import face

def block_mean(image,by_size=8,bx_size=8):
    result = image.copy()
    for y in range(0, image.shape[0], by_size):
        for x in range(0, image.shape[1], bx_size):
            sub = result[y:y+by_size, x:x+bx_size]
            sub[:] = np.mean(sub)
    return result
    
image = face(True)
plt.subplot(121)
plt.imshow(image, cmap="gray")
plt.subplot(122)
dimage=image.copy()
result = block_mean(image, 16, 16)
plt.imshow(result)
plt.show()