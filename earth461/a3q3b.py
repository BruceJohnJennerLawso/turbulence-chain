## a3q3b.py ####################################################################
## now graphing effective aquifer conductivity by TDS levels ###################
################################################################################
from gcm import *
from conductivity import *

def conductivityByPlume1(plumeConductivity, coilSpacing, cumulativeResponseFunction):
	layerList = []
	layerList.append(layer(4, 6))
	layerList.append(layer(plumeConductivity, 3))			
	layerList.append(layer(15, 6))
	layerList.append(layer(40, 6))
	return apparentConductivity(coilSpacing, cumulativeResponseFunction, layerList)


def conductivityByPlume2(plumeConductivity, coilSpacing, cumulativeResponseFunction):
	layerList = []
	layerList.append(layer(4, 6))
	layerList.append(layer(15, 6))			
	layerList.append(layer(plumeConductivity, 3))
	layerList.append(layer(40, 6))
	return apparentConductivity(coilSpacing, cumulativeResponseFunction, layerList)




if(__name__ == "__main__"):
	
	minTDS = getTDS(1.0, 0.37, 1.5, 0.015, 0.67)
	maxTDS = getTDS(1.0, 0.37, 1.5, 0.100, 0.67)	
	
	tdsValues = np.arange(minTDS, maxTDS, 1.0)
	
	##plumeConductivities = np.arange(15, 100, 2.0)
	c = []
	e = []
	for tds in tdsValues:
		c.append(conductivityByPlume1(getConductivity(1.0, 0.37, 1.5, tds, 0.67)*1000, 10.0, cumulativeResponseVD))
		e.append(conductivityByPlume1(getConductivity(1.0, 0.37, 1.5, tds, 0.67)*1000, 20.0, cumulativeResponseVD))		
	for i in range(0, len(c)):
		c[i] -= ((4*(1 - cumulativeResponseVD(6/10.0))) + (40*(cumulativeResponseVD(15/10.0))))
		c[i] /= (cumulativeResponseVD(6/10.0) - cumulativeResponseVD(15/10.0))
	
		e[i] -= ((4*(1 - cumulativeResponseVD(6/20.0))) + (40*(cumulativeResponseVD(15/20.0))))
		e[i] /= (cumulativeResponseVD(6/20.0) - cumulativeResponseVD(15/20.0))
	
	print 
	
	f = []
	g = []
	for tds in tdsValues:
		f.append(conductivityByPlume2(getConductivity(1.0, 0.37, 1.5, tds, 0.67)*1000, 10.0, cumulativeResponseVD))
		g.append(conductivityByPlume2(getConductivity(1.0, 0.37, 1.5, tds, 0.67)*1000, 20.0, cumulativeResponseVD))		
	for i in range(0, len(c)):
		f[i] -= ((4*(1 - cumulativeResponseVD(6/10.0))) + (40*(cumulativeResponseVD(15/10.0))))
		f[i] /= (cumulativeResponseVD(6/10.0) - cumulativeResponseVD(15/10.0))
	
		g[i] -= ((4*(1 - cumulativeResponseVD(6/20.0))) + (40*(cumulativeResponseVD(15/20.0))))
		g[i] /= (cumulativeResponseVD(6/20.0) - cumulativeResponseVD(15/20.0))
		
				
	for i in range(0, len(c)):
		c[i] = getTDS(1.0, 0.37, 1.5, c[i]/1000.0, 0.67)
		e[i] = getTDS(1.0, 0.37, 1.5, e[i]/1000.0, 0.67)								
		f[i] = getTDS(1.0, 0.37, 1.5, f[i]/1000.0, 0.67)
		g[i] = getTDS(1.0, 0.37, 1.5, g[i]/1000.0, 0.67)
		
	print c[0], c[len(c) -1]			
	datasetC = dataSet(tdsValues, c, "Question 1 VD, spacing = 10.0", "r--")
	datasetE = dataSet(tdsValues, e, "Question 1 VD, spacing = 20.0", "r")
	datasetF = dataSet(tdsValues, f, "Question 2 VD, spacing = 10.0", "c--")
	datasetG = dataSet(tdsValues, g, "Question 2 VD, spacing = 20.0", "c")	
		
	print e[0], e[len(e) -1]	
	
	graphLin("Effective Conductivity by TDS", "plume3b.png", "Apparent TDS (ppm)", "True TDS (ppm)", int(minTDS), int(maxTDS), 0, 2450, True, datasetC, datasetE, datasetF, datasetG)
	
		
