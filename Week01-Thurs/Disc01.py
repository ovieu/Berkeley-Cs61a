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

##1.4 handle_overflow(s1, s2)
def handle_overflow(s1, s2):
	if (s1 > 30) and (s2 > 30):
		print("No Space Left")
	elif (s1 > 30) and (s2 < 30):
		space = 30 - s2
		print("{} spot left in Section 2".format(space))
	elif (s1 < 30) and (s2 > 30):
		space = 30 - s1
		print("{} spot left in Section 1".format(space))
	else:
		print("No Overflow")
