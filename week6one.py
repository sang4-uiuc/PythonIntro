def computepay(h,r):
	if h > 0 and h <= 40:
		total = h * r
		return total
	elif h > 40:
		total = 40 * r + ((h-40) * (1.5*r))
		return total
	else:
		return "Please enter a valid number of hours"

try:
	hrs = raw_input("Enter Hours:")
	rate = raw_input("Enter Rate:")
	hrs = float(hrs)
	rate = float(rate)
except:
	print "Please enter valid numbers!"
	quit()

p = computepay(hrs,rate)
print p
