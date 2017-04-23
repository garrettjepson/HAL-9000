from __future__ import division
from __future__ import print_function
import numpy as np
from PIL import Image


#Initialize the matrix- Size (100,100)

size = 1000


#Create the Gaussian Function

def Gaussian(x,y,x0,y0,sigmax,sigmay):
	result = int(round( 255*np.exp(-(x - x0)**2 / (2 * sigmax**2)) * np.exp( -(y - y0)**2 / (2 *sigmay**2))))
	return result



def Random_Gaussian(size,name):

	data = np.zeros((size,size))

	x0 = np.random.randint(0, int(round(size/2)))
	y0 = np.random.randint(0, int(round(size/2)))
	sigmax = np.random.uniform(20,150)
	sigmay = np.random.uniform(20,150)

	for i in range(size):
		for j in range(size):
			data[i][j] = Gaussian(i,j,x0,y0,sigmax,sigmay)

	np.savetxt(name + '.txt' , data, delimiter=',')




Random_Gaussian(1000,"test")
