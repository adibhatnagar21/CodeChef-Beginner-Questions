def fac(num):
    c=1
    for i in range(1,num+1):
        c=c*i
    return c
t=int(raw_input())
if(t>=1 and t<=100): 
    for i in range (0,t):
        a=int(raw_input())
        b=fac(a)
        print b
