## a5q2a.py ####################################################################
## determining parameters for a unknown layer based on reflection ##############
## data ########################################################################
################################################################################
import numpy as np
from gpr import *

def findLayer2(vNMO1, t0_1, vNMO2, t0_2):
	d1 = vNMO1*t0_1
	layer1 = Layer(d1, vNMO1)
	
	v2 = getLayerVelocity(vNMO1, t0_1, vNMO2, t0_2)
	d2 = getLayerDepth(v2, t0_1, t0_2)
	layer2 = Layer(d1, v2)
	
	layer1.printLayer()
	layer2.printLayer()

if(__name__ == "__main__"):
	vNMO1 = 0.115
	## m/ns
	t0_1 = 50
	## ns
	vNMO2 = 0.093
	## m/ns
	t0_2 = 105
	## ns
	findLayer2(vNMO1, t0_1, vNMO2, t0_2)
