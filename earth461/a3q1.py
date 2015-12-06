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
	dx = 100.0 - 15.0
	
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
	
	datasetA = dataSet(plumeConductivities, a, "VD, spacing = 3.66, slope %f" % ((a[len(a)-1] - a[0])/dx), "r")
	datasetB = dataSet(plumeConductivities, b, "HD, spacing = 3.66, slope %f" % ((b[len(b)-1] - b[0])/dx), "c")
	datasetC = dataSet(plumeConductivities, c, "VD, spacing = 10.0, slope %f" % ((c[len(c)-1] - c[0])/dx), "r--")
	datasetD = dataSet(plumeConductivities, d, "HD, spacing = 10.0, slope %f" % ((d[len(d)-1] - d[0])/dx), "c--")
	datasetE = dataSet(plumeConductivities, e, "VD, spacing = 20.0, slope %f" % ((e[len(e)-1] - e[0])/dx), "r^")
	datasetF = dataSet(plumeConductivities, f, "HD, spacing = 20.0, slope %f" % ((f[len(f)-1] - f[0])/dx), "c^")
		
	
	
	graphLin("Apparent Conductivity by Plume conductivity", "plume1.png", "Apparent Conductivity (mS/m)", "Plume Conductivity (mS/m)", 0, 150, 0, 65, True, datasetA, datasetB, datasetC, datasetD, datasetE, datasetF)
	
		
