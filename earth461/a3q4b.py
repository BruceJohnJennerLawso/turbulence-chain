## a3q4.py #####################################################################
## apparent conductivities varying with elevation ##############################
################################################################################
from gcm import *
from conductivity import *

def conductivityBySurface(topography, coilSpacing, cumulativeResponseFunction):
	layerList = []
	layerList.append(layer(5, (7.5+ topography)))
	layerList.append(layer(20, 3))	
	return apparentConductivity(coilSpacing, cumulativeResponseFunction, layerList)





if(__name__ == "__main__"):
	topo = np.arange(-5, 5, 0.1)
	a = []
	b = []
	for topog in topo:
		a.append(conductivityBySurface(topog, 10.00, cumulativeResponseVD))
		b.append(conductivityBySurface(topog, 10.00, cumulativeResponseHD))									
	
	for i in range(0, len(a)):
		a[i] = a[i] - (5*(1 - cumulativeResponseVD(7.5/10.0)))
		a[i] = a[i]/cumulativeResponseVD(7.5/10.0)
	
		b[i] = b[i] - (5*(1 - cumulativeResponseHD(7.5/10.0)))
		b[i] = b[i]/cumulativeResponseHD(7.5/10.0)
		
	
	datasetA = dataSet(topo, a, "VD, spacing = 10.0", "r")
	datasetB = dataSet(topo, b, "HD, spacing = 10.0", "g")
		
	
	
	graphLin("Apparent Aquifer Conductivity by Elevation", "plume4b.png", "Apparent Aquifer Conductivity (mS/m)", "Relative Elevation (m)", -5, 5, 0, 53, True, datasetA, datasetB)
	
