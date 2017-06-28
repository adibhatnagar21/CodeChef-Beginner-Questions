def zeros(y):
    i=5
    count=0
    while (y/i>=1):
        count=count+y/i
        i=i*5
    return count
        
n=input()
if (n>=1 and n<=1000000000):
    for n in range(0,n):
            a=input()
            b=zeros(a)
            print b
