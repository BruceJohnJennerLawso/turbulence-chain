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
	
	datasetA = dataSet(topo, a, "VD, spacing = 10.0", "r")
	datasetB = dataSet(topo, b, "HD, spacing = 10.0", "g")
		
	
	
	graphLin("Apparent Conductivity by Elevation", "plume4.png", "Apparent Conductivity (mS/m)", "Relative Elevation (m)", -5, 5, 0, 53, True, datasetA, datasetB)
	
