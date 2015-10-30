## q4.py #######################################################################
## loglog plotting of conductivity by Sw for clay sands ########################
## containing varying TDS levels ###############################################
################################################################################
from conductivity import *


def plotForTDS(TDS):
	init_range = range(50,1000)
	saturation = []
	for i in init_range:
		saturation.append(i/1000.0)
		
	clay = []
	noclay = []
	
	for Sw in saturation:
		noclay.append(adjustConductivityForTemperature(25, 15, getConductivity(1.0, 0.30, 1.4, TDS, 0.67, Sw, 1.5))*1000)
		clay.append(adjustConductivityForTemperature(25, 15, getClayConductivity(Sw, 1.5, TDS, 0.30, 1.4, 1.0, 0.67, 0.050)*1000))							

	clayData = dataSet(saturation, clay, "Clay Sand", "b-")
	noclayData = dataSet(saturation, noclay, "Clean Sand", "r-")
		
	graphLogLog("log conductivity by log Sw for TDS %d PPM" % TDS, \
				"log sand conductivity (mS/m)", "log Sw", 10e-5, 10e5, 1e-5, 1e5, True, \
				 clayData, noclayData)

if(__name__ == "__main__"):
	plotForTDS(5)
	plotForTDS(50)
	plotForTDS(500)
	plotForTDS(5000)
	plotForTDS(50000)
	plotForTDS(500000)


