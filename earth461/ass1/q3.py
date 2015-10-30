## q3.py #######################################################################
## plot of log conductivity by log TDS in ppm ##################################
## demonstrating a saturated normal sand #######################################
## vs a saturated clayey sand ##################################################
################################################################################
from conductivity import *

if(__name__ == "__main__"):
		
	tds_values = range(50, 50000, 50)
	
	clay = []
	noclay = []
	
	surfaceComponent = 50
	
	for cy in tds_values:
		clay.append( adjustConductivityForTemperature(25, 15, (getConductivity(1.0, 0.30, 1.4, cy , 0.67)*1000) + surfaceComponent) )
		print adjustConductivityForTemperature(25, 15, (getConductivity(1.0, 0.30, 1.4, cy , 0.67)*1000) + surfaceComponent),
		noclay.append(adjustConductivityForTemperature(25, 15, getConductivity(1.0, 0.30, 1.4, cy , 0.67)*1000))		
		
	clayData = dataSet(tds_values, clay, "Clay Sand", "b-")
	noclayData = dataSet(tds_values, noclay, "Clean Sand", "r-")
	graphLogLog("log conductivity by log TDS for clay and non-clay sands", \
				"log sand conductivity (mS/m)", "log TDS (ppm)", 1, 1e6, 1e-2, 1e2, True, \
				 clayData, noclayData)
