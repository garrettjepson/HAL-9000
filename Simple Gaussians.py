from __future__ import division
from __future__ import print_function
import numpy as np
from PIL import Image

#Initialize the matrix- Size (100,100)

size = 1000
arr = np.zeros((size,size))

#Initialize the Gaussian Properties

x0 = 500; y0 = 500; sigmax = 100; sigmay = 50

#Create the Gaussian Function

def Gaussian(x,y):
	result = int(round( 255*np.exp(-(x - x0)**2 / (2 * sigmax**2)) * np.exp( -(y - y0)**2 / (2 *sigmay**2))))
	return result



for i in range(size):
	for j in range(size):
		arr[i][j] = Gaussian(i,j)


im = Image.fromarray(arr)
im.show()


