## a3q7.py #####################################################################
## plotting response functions for varying coil spacing ########################
## and orientation as a function of real depth z ###############################
################################################################################
from gcm import *
from conductivity import *
import math



if(__name__ == "__main__"):
	realDepth = np.arange(0, 80, 0.1)
	
	a = []
	b = []
	c = []
	d = []
	
	eff = []
	
	for z in realDepth:
		a.append(responseHD(z))
		b.append(responseVD(z))		
		
		eff.append(responseEffectiveVD(z))			
	
	datasetA = dataSet(realDepth, a, "HD, spacing = 1.0", "y")
	datasetB = dataSet(realDepth, b, "VD, spacing = 1.0", "m")		

	datasetEff = dataSet(realDepth, eff, "Effective Response, spacing = 1.0", "b")				
		
	
	
	graphLin("Response Function by True Depth", "8.png", "True Depth (m)", "Response Function \phi(z^')", 0, 80, 0, 1, True, datasetA, datasetB, datasetEff)
	
	
