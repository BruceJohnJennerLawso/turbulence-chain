## q1.py #######################################################################
## graph conductivity for sands depending on pore contents #####################
## log log graph ###############################################################
################################################################################
from conductivity import *



if(__name__ == "__main__"):

	
	tds_values = range(50, 50000)
	
	naclConductivities = []
	alkalineConductivities = []
	freshConductivities = []
	
	for cy in tds_values:
		naclConductivities.append(getConductivity(1.0, 0.40, 1.5, cy , 0.5)*1000)
		alkalineConductivities.append(getConductivity(1.0, 0.40, 1.5, cy , 0.9)*1000)		
		freshConductivities.append(getConductivity(1.0, 0.40, 1.5, cy , 0.67)*1000)
		
	nacl = dataSet(tds_values, naclConductivities, "NaCl brine", "b-")
	alkaline = dataSet(tds_values,alkalineConductivities,"alkaline groundwater", "g-")
	fresh = dataSet(tds_values, freshConductivities, "fresh groundwater", "r-")	
	graphLogLog("log conductivity by log TDS for various\n saturated sands", \
				"log sand conductivity (mS/m)", "log TDS (ppm)", 1, 1e6, 1e-2, 1e5, True, \
				 nacl, alkaline, fresh)
