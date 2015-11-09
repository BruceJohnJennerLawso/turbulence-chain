## q1.py #######################################################################
## plotting potentials for a spike electrode by distance from the source #######
## basically seeing how far away you have to go to see it as basically #########
## a point source ##############################################################
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


	vRatio = []

	for cy in nValues:
		voltRatio = vSpikeOverPoint(cy)
		if((closeEnough(0.25, voltRatio, 0.01))or(closeEnough(0.5, voltRatio, 0.001))or(closeEnough(0.75, voltRatio, 0.01))or(closeEnough(0.9, voltRatio, 0.001))or(closeEnough(0.95, voltRatio, 0.0005)) ):
			print "n = %f, V/V = %f" % (cy, voltRatio)
		vRatio.append(voltRatio)


	plotData = dataSet(nValues, vRatio, "V Spike/V Point", "c")
	graphLin("V Spike over V Point for increasing n values", "1.png", "V Spike/V Point", "n", 0, 10, 0, 1, True, plotData)
