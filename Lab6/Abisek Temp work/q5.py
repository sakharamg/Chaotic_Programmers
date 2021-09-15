import numpy as np
import sys
from matplotlib import pyplot as plt

# write your code here

def decode_image(img):
	a = 0
	b = 255
	c = np.min(img)
	d = np.max(img)
	img -= c
	img *= ((b - a)/(d-c))
	img += a
	return img



input_path = sys.argv[2]
data = np.load(input_path)
hist, bin_edges = np.histogram(data)
updated = decode_image(data)
plt.imshow(updated)
plt.savefig('q5_result.png')