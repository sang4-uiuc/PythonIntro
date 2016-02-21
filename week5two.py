#using elif and try and except for this program
try:
	score = raw_input("Enter Score: ")
	x = float(score)
	if x >= 0 and x <= 1.0:
		if x >= 0.9:
			print "A"
		elif x >= 0.8:
			print "B"
		elif x >= 0.7:
			print "C"
		elif x >= 0.6:
			print "D"
		else:
			print "F"
	
	else:
		print "not in range"
#it's not good to put all those in try right?
#any other way i can do this?

except:
	print "Error, please re-enter a number between 0 and 1.0"
	quit()


