## resistivityLayers.py ########################################################
## equivalent resistivity for layers given their ###############################
## fractions of the total thickness and their resistivity ######################
## also coefficient of anisotropy ##############################################
################################################################################
import math


def resistivityVertical(phi1, rho1, phi2, rho2):
	output = (phi1*rho1) + (phi2*rho2)
	return output
	
def resistivityHorizontal(phi1, rho1, phi2, rho2):
	output = 1/(phi1/rho1 + phi2/rho2)
	return output
	
def getCoefficientOfAnisotropy(rhoV, rhoH):
	output = math.sqrt(rhoV/rhoH)
	return output
