## a3q1.py #####################################################################
## plotting apparent conductivity for various coil #############################
## orientations as a function of plume conductivity in the earth ###############
################################################################################
from gcm import *


def conductivityByPlume(plumeConductivity, coilSpacing, cumulativeResponseFunction):
	layerList = []
	layerList.append(layer(4, 6))
	layerList.append(layer(plumeConductivity, 3))			
	layerList.append(layer(15, 6))
	layerList.append(layer(40, 600000000))
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
	datasetB = dataSet(plumeConductivities, b, "HD, spacing = 3.66", "c")
	datasetC = dataSet(plumeConductivities, c, "VD, spacing = 10.0", "r--")
	datasetD = dataSet(plumeConductivities, d, "HD, spacing = 10.0", "c--")
	datasetE = dataSet(plumeConductivities, e, "VD, spacing = 20.0", "r^")
	datasetF = dataSet(plumeConductivities, f, "HD, spacing = 20.0", "c^")
		
	
	
	graphLin("Apparent Conductivity by Plume conductivity", "plume1.png", "Apparent Conductivity (mS/m)", "Plume Conductivity (mS/m)", 0, 150, 0, 53, True, datasetA, datasetB, datasetC, datasetD, datasetE, datasetF)
	
		
