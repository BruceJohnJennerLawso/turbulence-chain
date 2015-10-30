## conductivity.py #############################################################
## conductivity of a saturated sand based on various factors ###################
################################################################################
from plotting import *

def getClayConductivity(Sw, n, TDS, phi, m, a, P, surfaceComponent):
	output = Sw**(n-1)
	output *= (( (Sw*TDS*(phi**m))/(a*P*10000) ) + (surfaceComponent))
	return output


def getConductivity(a, phi, m, TDS, P, Sw = "Null", n = "Null"):
	output = (phi**m)*TDS
	if((Sw != "Null")and(n != "Null")):
		output *= (Sw**(n))
	output /= (P*10000*a)
	return output

def adjustResistivityForTemperature(T1, T2, resistivity):
	output = resistivity*((T1+21.5)/(T2/21.5))
	return output
	
def adjustConductivityForTemperature(T1, T2, conductivity):
	return resistivityToConductivity(adjustResistivityForTemperature(T1, T2, conductivityToResistivity(conductivity)))
	## ahahahahaha
	
def resistivityToConductivity(resistivity):
	if(resistivity != 0):
		return (1/resistivity)
	else:
		## umm, aww dammit
		raise ValueError('shit hit the infinity fan (see conductivity.py)')
		
def conductivityToResistivity(conductivity):
	if(conductivity != 0):
		return (1/conductivity)
	else:
		## umm, aww dammit
		raise ValueError('shit hit the infinity fan (see conductivity.py)')		
