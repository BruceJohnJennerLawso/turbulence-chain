## a4q2.py #####################################################################
## using resistivity values from inversion of an ###############################
## ERT survey to compare expected apparent conductivities ######################
## against actual measurements #################################################
################################################################################
import numpy as np
from conductivity import *
from gcm import *
import math

def conductivityForLayers(coilSpacing, h, layerConductivities, cumulativeResponseFunction):
	layerList = []
	print layerConductivities
	layerBottoms = [0.5, 1.0125, 1.5635, 2.17, 2.8375, 3.571]
	for i in range(0, len(layerBottoms) - 1):
		layerList.append(layer(layerConductivities[i], layerBottoms[i]))
	layerList.append(layer(layerConductivities[len(layerConductivities)-1], 6))	
	## we tack on that last halfspace at the end of the list that goes to
	## infinity		
	return apparentConductivity(coilSpacing, cumulativeResponseFunction, layerList, h)


def graphApparentConductivities(averageWindow,  EMposition, ERTposition, coilSpacing, h, lineNo,  outputFile, *layerDatas):
	
	apparent1 = []
	## apparent1 is the apparent conductivities with the coils raised height h
	## off of the ground
	apparent2 = []	
	## apparent2 is the same with the coils on the ground at height 0

	for i in range(0, len(EMposition) ):
		layerConductivities = []
		for layer in layerDatas:
			if(averageWindow == 0):
				layerConductivities.append(layer[i])
			else:
				tail = averageWindow/2.0
				hits = 0
				average = 0
				for j in range(0, len(EMposition) - 1):
					if(abs(EMposition[j] - EMposition[i]) <= tail): 
						average += layer[j]
						hits += 1
				layerConductivities.append( (average/float(hits)) )
						
		
		apparent1.append(conductivityForLayers(coilSpacing, h, layerConductivities, cumulativeResponseVD))
		apparent2.append(conductivityForLayers(coilSpacing, 0, layerConductivities, cumulativeResponseVD))		
	apparentData1 = dataSet(EMposition, apparent1, "Apparent Conductivity for line %d, h = %f" % (lineNo, h), "r--")
	apparentData2 = dataSet(EMposition, apparent2, "Apparent Conductivity for line %d, h = %f" % (lineNo, 0), "b--")	
	print len(EMposition), len(apparent1)
	graphLin("Apparent Conductivity by Position", outputFile, "Apparent Conductivity (mS/m)", "EM 31 Survey Position (m)", 0, 70, 0, 90, True, apparentData1, apparentData2)	
	 


if(__name__ == "__main__"):
	##data_line3 = np.loadtxt("line3.txt", skiprows = 1,delimiter = ",")
	line1Data = np.genfromtxt("line1.txt", delimiter=",", filling_values=-1)
	line2Data = np.genfromtxt("line2.txt", delimiter=",", filling_values=-1)	
	line3Data = np.genfromtxt("line3.txt", delimiter=",", filling_values=-1)
	
	##positions = data_line3[:,2]
	graphApparentConductivities(0, line1Data[:,0], line1Data[:,1], 3.66, 1.0, 1, "a4q2_line1.jpg", line1Data[:,2], line1Data[:,3], line1Data[:,4], line1Data[:,5], line1Data[:,6], line1Data[:,7], line1Data[:,8])
	graphApparentConductivities(0, line2Data[:,0], line2Data[:,1], 3.66, 1.0, 2, "a4q2_line2.jpg", line2Data[:,2], line2Data[:,3], line2Data[:,4], line2Data[:,5], line2Data[:,6], line2Data[:,7], line2Data[:,8])	
	graphApparentConductivities(0, line3Data[:,0], line3Data[:,1], 3.66, 1.0, 3, "a4q2_line3.jpg", line3Data[:,2], line3Data[:,3], line3Data[:,4], line3Data[:,5], line3Data[:,6], line3Data[:,7], line3Data[:,8])		
	
	graphApparentConductivities(3, line1Data[:,0], line1Data[:,1], 3.66, 1.0, 1, "a4q2_line1_w3.jpg", line1Data[:,2], line1Data[:,3], line1Data[:,4], line1Data[:,5], line1Data[:,6], line1Data[:,7], line1Data[:,8])
	graphApparentConductivities(3, line2Data[:,0], line2Data[:,1], 3.66, 1.0, 2, "a4q2_line2_w3.jpg", line2Data[:,2], line2Data[:,3], line2Data[:,4], line2Data[:,5], line2Data[:,6], line2Data[:,7], line2Data[:,8])	
	graphApparentConductivities(3, line3Data[:,0], line3Data[:,1], 3.66, 1.0, 3, "a4q2_line3_w3.jpg", line3Data[:,2], line3Data[:,3], line3Data[:,4], line3Data[:,5], line3Data[:,6], line3Data[:,7], line3Data[:,8])		
	
	graphApparentConductivities(7, line1Data[:,0], line1Data[:,1], 3.66, 1.0, 1, "a4q2_line1_w7.jpg", line1Data[:,2], line1Data[:,3], line1Data[:,4], line1Data[:,5], line1Data[:,6], line1Data[:,7], line1Data[:,8])
	graphApparentConductivities(7, line2Data[:,0], line2Data[:,1], 3.66, 1.0, 2, "a4q2_line2_w7.jpg", line2Data[:,2], line2Data[:,3], line2Data[:,4], line2Data[:,5], line2Data[:,6], line2Data[:,7], line2Data[:,8])	
	graphApparentConductivities(7, line3Data[:,0], line3Data[:,1], 3.66, 1.0, 3, "a4q2_line3_w7.jpg", line3Data[:,2], line3Data[:,3], line3Data[:,4], line3Data[:,5], line3Data[:,6], line3Data[:,7], line3Data[:,8])			
	
	graphApparentConductivities(11, line1Data[:,0], line1Data[:,1], 3.66, 1.0, 1, "a4q2_line1_w11.jpg", line1Data[:,2], line1Data[:,3], line1Data[:,4], line1Data[:,5], line1Data[:,6], line1Data[:,7], line1Data[:,8])
	graphApparentConductivities(11, line2Data[:,0], line2Data[:,1], 3.66, 1.0, 2, "a4q2_line2_w11.jpg", line2Data[:,2], line2Data[:,3], line2Data[:,4], line2Data[:,5], line2Data[:,6], line2Data[:,7], line2Data[:,8])	
	graphApparentConductivities(11, line3Data[:,0], line3Data[:,1], 3.66, 1.0, 3, "a4q2_line3_w11.jpg", line3Data[:,2], line3Data[:,3], line3Data[:,4], line3Data[:,5], line3Data[:,6], line3Data[:,7], line3Data[:,8])			
	
	##print positions

