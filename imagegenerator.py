from __future__ import division
from __future__ import print_function
import numpy as np
from PIL import Image
from random import randint


for n in range(0,400):
	#import time
	#date_string = time.strftime("%Y-%m-%d-%H:%M:%S")
#Initialize the matrix- Size (100,100)
	size = 100
	arr = np.zeros((size,size))

#Initialize the Gaussian Properties

	x0 = randint(1,100); y0 = randint(1,100); sigmax = randint(1,10); sigmay = randint(1,10)

	center = (x0,y0)
	print (center)
#Create the Gaussian Function

	def Gaussian(x,y):
		result = int(round( 255*np.exp(-(x - x0)**2 / (2 * sigmax**2)) * np.exp( -(y - y0)**2 / (2 *sigmay**2))))
		return result

	for i in range(size):
		for j in range(size):
			arr[i][j] = Gaussian(i,j)

	im = Image.fromarray(arr)
	if im.mode !='RGB':
		im = im.convert('RGB')
		#im.show()
		im.save("/home/garrett/train/"+str(n)+".jpeg", "JPEG")
