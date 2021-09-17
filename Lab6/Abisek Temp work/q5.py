import numpy as np
import sys
from matplotlib import pyplot as plt


def decode_image(img):
	"""
	Input: 
		img: numpy matrix
		[Receives the image as a numpy matrix]
	
	Aim:
		Perform Linear contrast enhancement in the given matrix and return the scaled output.
	
	Output:
		img: numpy matrix
		[Linear contrast enhanced numpy matrix]
	"""
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
