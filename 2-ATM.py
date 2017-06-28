x,y=raw_input().split()
x=int(x)
y=float(y)
if(y>x+0.50 and x%5==0):
	y=y-x-0.50
	print y
else:
	print y 
