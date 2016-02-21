#compute gross pay using raw input

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
r = float(rate)
h = float(hrs)
pay = 0
otpay = 0
if h >40:
	pay = r * 40
	oth = h-40
	otr = r*1.5
	otpay = otr * oth
	pay = pay + otpay
#eh, i feel i'm doing this in a way that's not the most efficient
else:
	pay = r*h
print pay
