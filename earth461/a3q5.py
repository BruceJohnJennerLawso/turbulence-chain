## a3q5.py #####################################################################
## apparent conductivity as the coils are raised ###############################
## off of the ground ###########################################################
################################################################################
from gcm import *
from conductivity import *

def apparentConductivityAtHeight(h, coilSpacing, rootConductivity, cumulativeResponseFunction):
	layerList = []
	layerList.append(layer(rootConductivity, 0.3))
	layerList.append(layer(25, 3))	
	return apparentConductivity(coilSpacing, cumulativeResponseFunction, layerList, h)	


if(__name__ == "__main__"):
	height = np.arange(0, 2, 0.05)
	a = []
	b = []
	c = []
	d = []
	e = []
	
	f = []
	g = []
	h = []
	j = []
	k = []
	for hi in height:
		a.append(apparentConductivityAtHeight(hi, 1.0, 5.0, cumulativeResponseHD))
		b.append(apparentConductivityAtHeight(hi, 1.0, 15.0, cumulativeResponseHD))
		c.append(apparentConductivityAtHeight(hi, 1.0, 25.0, cumulativeResponseHD))
		d.append(apparentConductivityAtHeight(hi, 1.0, 35.0, cumulativeResponseHD))
		e.append(apparentConductivityAtHeight(hi, 1.0, 45.0, cumulativeResponseHD))													

		f.append(apparentConductivityAtHeight(hi, 1.0, 5.0, cumulativeResponseVD))
		g.append(apparentConductivityAtHeight(hi, 1.0, 15.0, cumulativeResponseVD))
		h.append(apparentConductivityAtHeight(hi, 1.0, 25.0, cumulativeResponseVD))
		j.append(apparentConductivityAtHeight(hi, 1.0, 35.0, cumulativeResponseVD))
		k.append(apparentConductivityAtHeight(hi, 1.0, 45.0, cumulativeResponseVD))
	
	
	datasetA = dataSet(height, a, "HD, spacing = 1.0, ", "r")
	datasetF = dataSet(height, f, "VD, spacing = 1.0", "r--")

	datasetB = dataSet(height, b, "HD, spacing = 1.0", "r")
	datasetG = dataSet(height, g, "VD, spacing = 1.0", "r--")	
	
	datasetC = dataSet(height, c, "HD, spacing = 1.0", "r")
	datasetH = dataSet(height, h, "VD, spacing = 1.0", "r--")		
		
	datasetD = dataSet(height, d, "HD, spacing = 1.0", "r")
	datasetJ = dataSet(height, j, "VD, spacing = 1.0", "r--")	

	datasetE = dataSet(height, e, "HD, spacing = 1.0", "r")
	datasetK = dataSet(height, k, "VD, spacing = 1.0", "r--")			
	
	graphLin("Apparent Conductivity by Elevation, root Conductivity = 5 mS/m", "plume5i.png", "Apparent Conductivity (mS/m)", "Ground Elevation (m)", 0, 2.0, 0, 53, True, datasetA, datasetF)
	graphLin("Apparent Conductivity by Elevation, root Conductivity = 15 mS/m", "plume5ii.png", "Apparent Conductivity (mS/m)", "Ground Elevation (m)", 0, 2.0, 0, 53, True, datasetB, datasetG)
	graphLin("Apparent Conductivity by Elevation, root Conductivity = 25 mS/m", "plume5iii.png", "Apparent Conductivity (mS/m)", "Ground Elevation (m)", 0, 2.0, 0, 53, True, datasetC, datasetH)
	graphLin("Apparent Conductivity by Elevation, root Conductivity = 35 mS/m", "plume5iv.png", "Apparent Conductivity (mS/m)", "Ground Elevation (m)", 0, 2.0, 0, 53, True, datasetD, datasetJ)
	graphLin("Apparent Conductivity by Elevation, root Conductivity = 45 mS/m", "plume5v.png", "Apparent Conductivity (mS/m)", "Ground Elevation (m)", 0, 2.0, 0, 53, True, datasetE, datasetK)				
	
