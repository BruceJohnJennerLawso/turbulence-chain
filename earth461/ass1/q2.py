## q2.py #######################################################################
## plot of conductivity vs Sw on a loglog ######################################
## plot for varying values of saturation exp ###################################
## n ###########################################################################
################################################################################
from conductivity import *

def frange(start, end, interval):
	output = range(start, end)
	for i in output:
		i = i/interval
	return output		
		

if(__name__ == "__main__"):
	init_range = range(1,1000)
	saturation = []
	for i in init_range:
		saturation.append(i/1000.0)
		
	a = []
	b = []
	c = []
	d = []
	e = []	
	
	for Sw in saturation:
		a.append(adjustConductivityForTemperature(25, 10, getConductivity(1.0, 0.39, 1.4, 250, 0.67, Sw, 1.4))*1000)
		b.append(adjustConductivityForTemperature(25, 10, getConductivity(1.0, 0.39, 1.4, 250, 0.67, Sw, 1.65))*1000)
		c.append(adjustConductivityForTemperature(25, 10, getConductivity(1.0, 0.39, 1.4, 250, 0.67, Sw, 1.9))*1000)
		d.append(adjustConductivityForTemperature(25, 10, getConductivity(1.0, 0.39, 1.4, 250, 0.67, Sw, 2.15))*1000)
		e.append(adjustConductivityForTemperature(25, 10, getConductivity(1.0, 0.39, 1.4, 250, 0.67, Sw, 2.40))*1000)								

	set_a = dataSet(saturation, a, "n = 1.4", "b-")
	set_b = dataSet(saturation, b, "n = 1.65", "g-")
	set_c = dataSet(saturation, c, "n = 1.9", "r-")
	set_d = dataSet(saturation, d, "n = 2.15", "c-")	
	set_e = dataSet(saturation, e, "n = 2.40", "y-")		
		
	graphLogLog("log conductivity by log Sw for various\n saturation exponent values (n)", \
				"log sand conductivity (mS/m)", "log Sw", 10e-4, 10e2, 1e-9, 1, True, \
				 set_a, set_b, set_c, set_d, set_e)
