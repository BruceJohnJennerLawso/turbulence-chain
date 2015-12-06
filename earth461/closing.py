## closing.py ##################################################################
## see if integrals closing blah ###############################################
################################################################################
from plotting import *
import numpy as np

def f(x, y, z):
	output = (1 + y + z**2)
	return output

def integral(zMax, intervalSize):
	output = 0
	
	zRange = np.arange(0, zMax, intervalSize)
	for i in range(0, len(zRange)-1):
		yRange = np.arange(0, 5, intervalSize)
		for j in range(0, len(yRange)-1):
			xRange = np.arange(0, 5, intervalSize)
			for k in range(0, len(xRange)-1):
				output += f(xRange[k], yRange[j], zRange[i])*(intervalSize**3)
	return output	

if(__name__ == "__main__"):
	zMaxes = np.arange(1, 5, 0.1)
	d = []
	a = []
	b = []
	c = []
	##d = []
	
	for zMax in zMaxes:	
		print zMax, integral(zMax, 0.025)
		d.append(integral(zMax, 0.025))
	print "Finished 0.025 interval"

	for zMax in zMaxes:
		c.append(integral(zMax, 0.05))
		print zMax, integral(zMax, 0.1)
	print "Finished 0.05 interval"		
	
	for zMax in zMaxes:
		b.append(integral(zMax, 0.075))
		print zMax, integral(zMax, 0.1)
	print "Finished 0.075 interval"

	for zMax in zMaxes:
		print zMax, integral(zMax, 0.1)
		a.append(integral(zMax, 0.1))
	print "Finished 0.1 interval"

	
	
	
	
		##d.append(integral(zMax, 0.01))
	dataA = dataSet(zMaxes, a, "Stepsize = 0.1", "r--")
	dataB = dataSet(zMaxes, b, "Stepsize = 0.075", "g--")
	dataC = dataSet(zMaxes, c, "Stepsize = 0.05", "c--")
	dataD = dataSet(zMaxes, d, "Stepsize = 0.025", "k--")					
	
	graphLin("Triple Integral by zMax", "triple.png", "Integral", "zMax", 0, 5, 100, 1500, True, dataA, dataB, dataC, dataD)
