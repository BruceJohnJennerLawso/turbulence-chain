## plotting.py #################################################################
## generalize some stuff about creating graphs for geophysics ##################
################################################################################
import numpy as np
import matplotlib.pyplot as plt


class dataSet:
	def __init__(self, x_values, y_values, dataset_name, dataset_colour):
		self.xValues = x_values
		self.yValues = y_values
		self.datasetName = dataset_name
		self.datasetColour = dataset_colour
	
	def getXValues(self):
		return self.xValues
		
	def getYValues(self):
		return self.yValues
		
	def getDatasetName(self):
		return self.datasetName
		
	def getDatasetColour(self):
		return self.datasetColour
		


def graphLogLog(graphTitle, yLabel, xLabel, xMin, xMax, yMin, yMax, saveToFile, *datasets):
	fig, (ax1) = plt.subplots(1)
	ax1.set_xscale("log")
	ax1.set_yscale("log")
	ax1.set_adjustable("datalim")
	
	ax1.set_xlim(xMin, xMax)
	ax1.set_ylim(yMin, yMax)
	ax1.set_xlabel(xLabel)
	ax1.set_ylabel(yLabel)	
	
	for data in datasets:
		ax1.plot(data.getXValues(), data.getYValues(), data.getDatasetColour(), label=data.getDatasetName())

	ax1.grid(b=True, which='both', color='c', linestyle='-')	

	ax1.legend(loc='upper left')	
	##ax1.set_aspect(1)
	ax1.set_title(graphTitle)
	##plt.draw()
	
	
	if(saveToFile == True):
		fileName = graphTitle + '.png'
		fileName = fileName.rstrip('\n')
		## dont know why, but this still doesnt fix the garbage character
		## problem. Annoying
		plt.savefig(fileName)
		## oddly this wont playball when show() is called first
	else:
		plt.show()


def graphLin(graphTitle, fileName, yLabel, xLabel, xMin, xMax, yMin, yMax, saveToFile, *datasets):
	fig, (ax1) = plt.subplots(1)
	ax1.set_adjustable("datalim")
	
	ax1.set_xlim(xMin, xMax)
	ax1.set_ylim(yMin, yMax)
	ax1.set_xlabel(xLabel)
	ax1.set_ylabel(yLabel)	
	
	for data in datasets:
		ax1.plot(data.getXValues(), data.getYValues(), data.getDatasetColour(), label=data.getDatasetName())

	ax1.grid(b=True, which='both', color='c', linestyle='-')	

	ax1.legend(loc='upper right')	
	#ax1.set_aspect(1)
	ax1.set_title(graphTitle)
	plt.draw()
	
	
	if(saveToFile == True):
		plt.savefig(fileName)
	else:
		plt.show()


if(__name__=="__main__"):
	import math
	
	
	
	xRange = range(1,100)
	
	ln = []
	square = []
	lin = []
	
	for cy in xRange:
		ln.append(math.log(cy))
		square.append(cy**2)
		lin.append(cy)
		
	lnData = dataSet(xRange, ln, "ln values", "r")
	squareData = dataSet(xRange, square, "squared values", "g")
	linData = dataSet(xRange, lin, "linear values", "b")		
	
	
	graphLin("Testing linPlottttt", "foo.png", "y", "x", 0, 100, 0, 1000, False, lnData, squareData, linData)
	
	
	
	
	
	
	
	
