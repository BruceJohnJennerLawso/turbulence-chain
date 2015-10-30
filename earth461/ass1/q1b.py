## q2.py #######################################################################
## log log conductivity by ppm again, this time with different values ##########
## depending on temperature ####################################################
################################################################################
from conductivity import *

if(__name__ == "__main__"):
		
	tds_values = range(50, 50000)
	
	tencConductivities = []
	twentyfivecConductivities = []
	fortycConductivities = []
	
	for cy in tds_values:
		tencConductivities.append(adjustConductivityForTemperature(25, 10, getConductivity(1.0, 0.40, 1.5, cy , 0.5))*1000)
		twentyfivecConductivities.append(getConductivity(1.0, 0.40, 1.5, cy , 0.5)*1000)		
		fortycConductivities.append(adjustConductivityForTemperature(25, 40, getConductivity(1.0, 0.40, 1.5, cy , 0.5))*1000)		
		## 0.5 works here cause we can 
		
	ten = dataSet(tds_values, tencConductivities, "10 Degrees C", "b-")
	twentyfive = dataSet(tds_values,twentyfivecConductivities,"25 Degrees C", "g-")
	forty = dataSet(tds_values, fortycConductivities, "40 Degrees C", "r-")	
	graphLogLog("log conductivity by log TDS for various\n temperatures of saturated sands", \
				"log sand conductivity (mS/m)", "log TDS (ppm)", 1, 1e6, 1e-2, 1e4, True, \
				 ten, twentyfive, forty)
