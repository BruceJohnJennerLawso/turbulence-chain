## a3q3.py #####################################################################
## plotting apparent conductivity as a function of the actual plume ############
## conductivity ################################################################
################################################################################
from gcm import *

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
	plumeConductivities = np.arange(15, 100, 2.0)
	c = []
	e = []
	for conductivity in plumeConductivities:
		c.append(conductivityByPlume1(conductivity, 10.0, cumulativeResponseVD))
		e.append(conductivityByPlume1(conductivity, 20.0, cumulativeResponseVD))		
	for i in range(0, len(c)):
		c[i] = c[i]-((4*(1 - cumulativeResponseVD(6/10.0))) + (40*(cumulativeResponseVD(15.0/10.0))))
		c[i] = c[i]/(cumulativeResponseVD(6/10.0) - cumulativeResponseVD(15.0/10.0))
	
		e[i] = e[i]-((4*(1 - cumulativeResponseVD(6/20.0))) + (40*(cumulativeResponseVD(15/20.0))))
		e[i] = e[i]/(cumulativeResponseVD(6/20.0) - cumulativeResponseVD(15/20.0))
	
	
	f = []
	g = []
	for conductivity in plumeConductivities:
		f.append(conductivityByPlume2(conductivity, 10.0, cumulativeResponseVD))
		g.append(conductivityByPlume2(conductivity, 20.0, cumulativeResponseVD))		

	print g[0], g[len(g) -1]	

	for i in range(0, len(c)):
		f[i] = f[i] - ((4*(1 - cumulativeResponseVD(6/10.0))) + (40*(cumulativeResponseVD(15.0/10.0))))
		f[i] = f[i]/(cumulativeResponseVD(6/10.0) - cumulativeResponseVD(15.0/10.0))
	
		g[i] = g[i] - ((4*(1 - cumulativeResponseVD(6/20.0))) + (40*(cumulativeResponseVD(15/20.0))))
		g[i] = g[i] / (cumulativeResponseVD(6/20.0) - cumulativeResponseVD(15/20.0))
		
				
	print g[0], g[len(g) -1]					
	
	datasetC = dataSet(plumeConductivities, c, "Question 1 VD, spacing = 10.0", "r--")
	datasetE = dataSet(plumeConductivities, e, "Question 1 VD, spacing = 20.0", "r")
	datasetF = dataSet(plumeConductivities, f, "Question 2 VD, spacing = 10.0", "c--")
	datasetG = dataSet(plumeConductivities, g, "Question 2 VD, spacing = 20.0", "c")	
		
	
	
	graphLin("Effective Conductivity by Plume conductivity", "plume3.png", "Effective Conductivity (mS/m)", "Plume Conductivity (mS/m)", 0, 150, 0, 50, True, datasetC, datasetE, datasetF, datasetG)
	
		
