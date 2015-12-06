## gpr.py ######################################################################
## ground penetrating radar module #############################################
################################################################################
import math


def dielectricPermittivityVacuum():
	return 8.8542e-12
	## units of Farads/meter

def speedOfLight():
	return 2.99972e8
	## units of meters/second
	
def toMetersPerNanosecond(metersPerSecond):
	return (metersPerSecond/1000000000.0)

def wavePropagation(sigma, epsilon, frequency):
	if(frequency > (sigma/(2*math.pi()*epsilon))):
		return True
	return False
	
def waveVelocity(mu, epsilon):
	output = 1/math.sqrt(mu*epsilon)
	return output	

def waveVelocityNoMu(kappa):
	## worst named function ever
	output = toMetersPerNanosecond(speedOfLight())
	output /= math.sqrt(kappa)
	return output

if(__name__ == "__main__"):
	print "Hello GPR\n"
	print toMetersPerNanosecond(speedOfLight())
