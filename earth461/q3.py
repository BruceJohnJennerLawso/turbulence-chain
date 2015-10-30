## q3.py #######################################################################
## plotting horizontal and vertical resistivities across #######################
## layers ######################################################################
## of stuff ####################################################################
################################################################################
from plotting import *
from resistivityLayers import *


def plotResistivities(rho1, rho2, filename):
	init_range = range(1,1000)
	phiValues = []
	for i in init_range:
		phiValues.append(i/1000.0)

	resVertical = []
	resHorizontal = []
	Anisotropy = []

	for cy in phiValues:
		vert = resistivityVertical(cy, rho1, (1- cy), rho2)
		horiz = resistivityHorizontal(cy, rho1, (1- cy), rho2)
		anisotropy = getCoefficientOfAnisotropy(vert, horiz)
		
		resVertical.append(vert)
		resHorizontal.append(horiz)
		Anisotropy.append(anisotropy)
		
		#if((closeEnough(0.25, voltRatio, 0.01))or(closeEnough(0.5, voltRatio, 0.001))or(closeEnough(0.75, voltRatio, 0.01))or(closeEnough(0.9, voltRatio, 0.001))or(closeEnough(0.95, voltRatio, 0.0005)) ):
		#	print "n = %f, V/V = %f" % (cy, voltRatio)


	verticalData = dataSet(phiValues, resVertical, "Vertical Resistivity", "c")
	horizontalData = dataSet(phiValues, resHorizontal, "Horizontal Resistivity", "r")
	anisotropyData = dataSet(phiValues, Anisotropy, "Coefficient of Anisotropy", "b")		
	graphLin("Vertical and Horizontal Resistivities, rho1 = %f, rho2 = %f" % (rho1, rho2), filename, "Resistivity (ohm meters)", "phi 1", 0, 1, 0, 50, True, verticalData, horizontalData, anisotropyData)


if(__name__=="__main__"):
	plotResistivities(1, 3, "3a.png")
	plotResistivities(1, 30, "3bi.png")
	plotResistivities(1, 300, "3bii.png")		
