## q2.py #######################################################################
## apparent resistivity over true resistivity for ##############################
## increasing spacing of a wenner array ########################################
################################################################################
from plotting import *
from spikeElectrode import *

def closeEnough(a, b, tolerance):
	if(abs(a-b) <= tolerance):
		return True
	return False

if(__name__=="__main__"):
	
	init_range = range(1,1000)
	nValues = []
	for i in init_range:
		nValues.append(i/100.0)

	rhoRatio = []

	for cy in nValues:
		resistivityRatio = apparentRhoOverReal(cy) 
		rhoRatio.append(resistivityRatio)
		if((closeEnough(0.25, resistivityRatio, 0.01))or(closeEnough(0.5, resistivityRatio, 0.001))or(closeEnough(0.75, resistivityRatio, 0.01))or(closeEnough(0.9, resistivityRatio, 0.001))or(closeEnough(0.95, resistivityRatio, 0.0005)) ):
			print "n = %f, rho/rho = %f" % (cy, resistivityRatio)

	plotData = dataSet(nValues, rhoRatio, "Resistivity Spike/Resistivity Point", "y")
	graphLin("Resistivity Spike over Resistivity Point for increasing n values", "2.png", "Resistivity Spike/Resistivity Point", "n", 0, 10, 0, 1, True, plotData)
