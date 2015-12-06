## a3q6c.py ####################################################################
## determining apparent conductivity for an EM 31 ##############################
## now accounting for the 1 m elevation height above the ground ################
## graphed with different depths of layers #####################################
################################################################################
from gcm import *
from conductivity import *
import math




def conductivityByTableDepth(tableDepth, coilSpacing, cumulativeResponseFunction, h):
	layerList = []
	layerList.append(layer(5, tableDepth))
	layerList.append(layer(20, 6))			
	return apparentConductivity(coilSpacing, cumulativeResponseFunction, layerList, h)


if(__name__ == "__main__"):
	waterTableDepth = np.arange(0, 10, 0.01)
	apparentConduct = []
	traditionalConduct = []
	for tableDepth in waterTableDepth:
		apparentConduct.append(conductivityByTableDepth(tableDepth, 3.66, heightAdjustedCumulativeResponseVD, 1.0))
		traditionalConduct.append(conductivityByTableDepth(tableDepth, 3.66, cumulativeResponseVD, 1.0))		
	dataset = dataSet(waterTableDepth, apparentConduct, "VD EM 31, spacing = 3.66, height = 1.0 m", "r")

	datasetB = dataSet(waterTableDepth, traditionalConduct, "VD EM 31, spacing = 3.66, height = 0 m", "b")	
		
	
	
	graphLin("Apparent Conductivity by Vadose Zone Depth", "6c.png", "Apparent Conductivity (mS/m)", "Vadose Zone Depth (m)", 0, 10, 0, 30, True, dataset, datasetB)
	
	
