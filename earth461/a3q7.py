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
		a.append(responseHD(z/20))
		b.append(responseVD(z/20))
		c.append(responseHD(z/40))
		d.append(responseVD(z/40))			
		
		eff.append(responseEffectiveVD(z))			
	
	datasetA = dataSet(realDepth, a, "HD, spacing = 20.0", "y")
	datasetB = dataSet(realDepth, b, "VD, spacing = 20.0", "m")
	datasetC = dataSet(realDepth, c, "HD, spacing = 40.0", "r")
	datasetD = dataSet(realDepth, d, "VD, spacing = 40.0", "g")		

	datasetEff = dataSet(realDepth, eff, "HD Effective, spacing = 20.0", "b")				
		
	
	
	graphLin("Response Function by True Depth", "7.png", "True Depth (m)", "Response Function \phi(z^')", 0, 80, 0, 2, True, datasetA, datasetB, datasetC, datasetD, datasetEff)
	
	
