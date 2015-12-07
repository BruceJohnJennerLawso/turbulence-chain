## gpr.py ######################################################################
## ground penetrating radar module #############################################
################################################################################
import math


## constant definitions ########################################################

def dielectricPermittivityVacuum():
	return 8.8542e-12
	## units of Farads/meter

def speedOfLight():
	return 2.99972e8
	## units of meters/second
	
def muNought():
	return (4*math.pi())/10000000
	## whatever

	
def toMetersPerNanosecond(metersPerSecond):
	return (metersPerSecond/1000000000.0)

def wavePropagation(sigma, epsilon, frequency):
	if(frequency > (sigma/(2*math.pi()*epsilon))):
		return True
	return False
	
def waveVelocity(mu, epsilon):
	output = 1/math.sqrt(mu*epsilon)
	return output	

def waveVelocityNoMu(kappa):
	## worst named function ever
	output = toMetersPerNanosecond(speedOfLight())
	output /= math.sqrt(kappa)
	return output
	
	
def toppsPermittivity(waterFraction):
	output = -(76.70*(waterFraction**3))
	output += (146.00*(waterFraction**2))
	output += (9.30*waterFraction)
	output += 3.03
	return output
	
def toppsWaterContent(permittivity):
	output = -(0.0000043*(permittivity**3))
	output += (0.00055*(permittivity**2))
	output += (0.0292*permittivity)
	output -= 0.053	
	return output
	
	
def reflectionCoeffcicient(kappa1, kappa2, mu1=False, mu2=False):
	## reflection coefficient is the ratio of amplitudes, Ar/Ai,
	## where Ai is the initial wave amplitude, Ar is the reflected wave
	## amplitude
	if((mu1 == False)or(mu2 == False)):
		output = math.sqrt(kappa1) - math.sqrt(kappa2)
		output /= (math.sqrt(kappa1) + math.sqrt(kappa2))
		return output
	else:
		output = math.sqrt(mu2/kappa2) - math.sqrt(mu1/kappa1)
		output /= (math.sqrt(mu2/kappa2) + math.sqrt(mu1/kappa1))
		return output


class Layer:
	def __init__(self,  depth, velocity):
		self.Depth = depth
		self.Velocity = velocity
	
	def getDepth(self):
		return self.Depth
		
	def getVelocity(self):
		return self.Velocity	
		
	def getTi(self):
		output = (2*self.Depth)/self.Velocity
		return output	
		
	def printLayer(self):
		print "Layer Depth: %f m, Layer Velocity: %f m/ns" % (self.Depth, self.Velocity)
		
class Reflection:
	def __init__(self, vNMO, t0):
		self.t0 = t0
		self.vNMO = vNMO


def getLayerVelocity(vNMOn, t0_n, vNMOnPlus1, t0_nPlus1):
	output = ((vNMOn**2)*t0_n)
	output -= ((vNMOnPlus1**2)*t0_nPlus1)
	output /= (t0_n - t0_nPlus1)
	return math.sqrt(output)
	
def getLayerDepth(vn, t0_n, t0_nPlus1):
	output = t0_n - t0_nPlus1
	output *= (0.5*vn)
	return output

def getNMOVelocity(*layers):
	output = 0.0
	for l in layers:
		output += ((l.getVelocity()**2)*l.getTi())
	tiSum = 0.0
	for l in layers:
		tiSum += l.getTi()
	output /= tiSum
	return output

def getTxSquaredNMO(x, i, *layers):
	vNMO = getNMOVelocity(layers)
	
	t0 = 0.0
	for cy in range(0, i):
		t0 += layers[cy].getTi()
	
	output = (t0**2) + ((x**2)/(vNMO**2))
	return output
	

	

if(__name__ == "__main__"):
	print "Hello GPR\n"
	print toMetersPerNanosecond(speedOfLight())

	frac = 0.5
	print frac, "->", toppsPermittivity(frac), "->", toppsWaterContent(toppsPermittivity(frac))
	## doesnt work, dunno why the reverse function doesnt get back the
	## original value
	
	
