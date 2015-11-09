## a3q6b.py ####################################################################
## plotting the ratio of conductivities for the ################################
## reading and the actual conductivity, where our reading ######################
## is taken with the coils some height h off of the ground #####################
################################################################################
from gcm import *
from conductivity import *
import math



def readingMeasuredRatio(h, coilSpacing):
	output = 1/math.sqrt((4*((h/coilSpacing)**2))+1)
	return output
	
if(__name__ == "__main__"):
	coilHeight = np.arange(0.75, 1.15, 0.05)
	ratios = []
	for h in coilHeight:
		ratios.append(readingMeasuredRatio(h, 3.66))									
	
	dataset = dataSet(coilHeight, ratios, "VD, spacing = 3.66", "r")
	
	
	graphLin("reading/measured ratio by coil height", "q6b.png", "Reading Ratio", "Height (m)", 0.70, 1.20, 0, 2, True, dataset)
	
		
