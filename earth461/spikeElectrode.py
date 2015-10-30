## spikeElectrode.py ###########################################################
## when point sources arent a good enough approximation ########################
################################################################################
import math


##def vPointSourceElectrode(

def vSpikeOverPoint(n):
	output = n/2.0
	tempVal = math.sqrt(n**2 + 1)
	output *= math.log( (tempVal + 1)/(tempVal -1) )
	return output

def apparentRhoOverReal(n):
	## 10/10 would be a good name for a band
	output = n
	tempVal = math.sqrt(n**2 + 1)	
	otherTempVal = math.sqrt(4*(n**2) + 1)
	output *= (math.log((tempVal + 1)/(tempVal -1)) - math.log((otherTempVal + 1)/(otherTempVal - 1)))
	return output
