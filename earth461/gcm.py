## gcm.py ######################################################################
## ground conductivity meters ##################################################
################################################################################
import math
from plotting import *

def omega(f):
	return (2*(math.pi*f))
	
## phi functions, would work if we could integrate to infinity #################
################################################################################
	
def responseVD(z):
	output = 4*z
	output /= ((4*(z**2))+1)**(3.0/2.0)
	return output
	
def responseHD(z):
	output = 2
	output -= (4*z)/(((4*(z**2))+1)**0.5)
	return output
	
def responsePERP(z):
	output = 2
	output /= (((4*(z**2))+1)**0.5)
	output -= ((8*(z**2))/(((4*(z**2))+1)**(3.0/2.0)))
	return output
	
def responseVCX(z):
	output = 1
	output -= ((2*z)/(((4*(z**2))+1)**0.5))
	output -= (2*z)/(((4*(z**2))+1)**(3.0/2.0))
	return output
	
	
def responseEffectiveVD(z):
	output = z/(math.sqrt((4*(z**2))+1600))
	output += z/(math.sqrt((4*(z**2))+400))
	return output	
	
def responseEffectiveVDHD(z):
	output = 4
	output -= (8*z)/(((4*(z**2))+1)**0.5)
	output -= (4*z)/(((4*(z**2))+1)**1.5)
	return output
	
## cumulative response functions, cause we cant integrate to infinity ##########
################################################################################	
	
def cumulativeResponseVD(z, h=0):
	output = 1
	output /= math.sqrt((4*((z + h)**2))+1)
	return output
	
def cumulativeResponseHD(z, h=0):
	output = math.sqrt(4*((z+h)**2) +1)
	output -= (2*(z+h))
	return output
	
def cumulativeResponsePERP(z, h=0):
	output = 1
	output -= (2*(z+h))/(math.sqrt((4*((z+h)**2)) +1))
	return output
	
def cumulativeResponseVCX(z):
	output = 1
	output -= z
	output += (math.sqrt(4*(z**2) +1))/(2)
	output -= 1/(2.0*(math.sqrt(4*(z**2) +1)))
	return output
		
		
def heightAdjustedCumulativeResponseVD(z, h):
	output = cumulativeResponseVD( (z), (h) )
	output /= cumulativeResponseVD(0, h)
	return output
	
class layer:
	def __init__(self, conductivity, depth):
		self.Conductivity = conductivity
		self.Depth = depth
	
	def getConductivity(self):
		return self.Conductivity
		
	def getDepth(self):
		return self.Depth
			
			
def trapezoidIntegral(x_min, x_max, intervals, func):
	intervalLen = abs(x_max - x_min)
	intervals = np.arange(x_min, x_max, (intervalLen/intervals))
	output = 0
	print 1, len(intervals)
	for i in range(1, len(intervals)):
		area = average(func(intervals[i]), func(intervals[i-1]))
		area *= (intervals[i] - intervals[i-1])
		output += area
	return output				
	
	
	
def apparentConductivity(coilSpacing, cumulativeResponseFunction, layers, h=0):
	output = 0
	
	layerBottom = 0
	lastResponse = 1
	
	##print layers
	
	##print "%d layers" % len(layers)
	##for i in range(0, len(layers)):
		##print "layer %d, conductivity %f mS/m, depth %f m" % (i, layers[i].getConductivity(), layers[i].getDepth())

	
	for i in range(0, len(layers)):
		##print "last layer index %d" % (len(layers) -1)
		layerBottom += layers[i].getDepth()		
		conductivity = layers[i].getConductivity()
		if(h != 0):
			response = cumulativeResponseFunction(layerBottom/coilSpacing, h/coilSpacing)
		else:
			response = cumulativeResponseFunction(layerBottom/coilSpacing)			
			
		if(i != (len(layers)-1)): 
			output += (conductivity)*(lastResponse - response)
			lastResponse = response
		else:
			output += (conductivity*(lastResponse))
			break
	return output
	
def conductivityByPlume(plumeConductivity, coilSpacing, cumulativeResponseFunction, h=0):
	layerList = []
	layerList.append(layer(4, 6))
	layerList.append(layer(plumeConductivity, 3))			
	layerList.append(layer(15, 6))
	layerList.append(layer(40, 6))
	return apparentConductivity(coilSpacing, cumulativeResponseFunction, layerList)
	
if(__name__ == "__main__"):
	plumeConductivities = np.arange(15, 100, 2.0)
	a = []
	b = []
	c = []
	d = []
	e = []
	f = []
	for conductivity in plumeConductivities:
		a.append(conductivityByPlume(conductivity, 3.66, cumulativeResponseVD))
		b.append(conductivityByPlume(conductivity, 3.66, cumulativeResponseHD))
		c.append(conductivityByPlume(conductivity, 10.0, cumulativeResponseVD))
		d.append(conductivityByPlume(conductivity, 10.0, cumulativeResponseHD))
		e.append(conductivityByPlume(conductivity, 20.0, cumulativeResponseVD))
		f.append(conductivityByPlume(conductivity, 20.0, cumulativeResponseHD))										
	
	datasetA = dataSet(plumeConductivities, a, "VD, spacing = 3.66", "r")
	datasetB = dataSet(plumeConductivities, b, "HD, spacing = 3.66", "g")
	datasetC = dataSet(plumeConductivities, c, "VD, spacing = 10.0", "b")
	datasetD = dataSet(plumeConductivities, d, "HD, spacing = 10.0", "c")
	datasetE = dataSet(plumeConductivities, e, "VD, spacing = 20.0", "r--")
	datasetF = dataSet(plumeConductivities, f, "HD, spacing = 20.0", "g^")
		
	
	
	graphLin("Apparent Conductivity by Plume conductivity", "plume1.png", "y", "x", 0, 150, 0, 23, True, datasetA, datasetB, datasetC, datasetD, datasetE, datasetF)
	
		
		
	
