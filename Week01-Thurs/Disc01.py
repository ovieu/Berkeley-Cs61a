##Solution to Discussion Questions

##1.3 Wear_jacket function
def wears_jacket(temp, raining):
	"""
	>>>rain = False
	>>>wears_jacket(90, rain)
	False
	>>> wears_jacket(40, rain)
	True
	>>> wears_jacket(100, True)
	True
	"""
	return ((temp < 60) or (raining == True)) == True


