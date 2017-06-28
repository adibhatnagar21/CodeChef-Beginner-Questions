n=int(raw_input())
csim=[]
zabs=[]
n1=0
n2=0
for i in range (n):
    x,y=raw_input().split()
    x=int(x)
    y=int(y)
    n1=n1+x
    n2=n2+y
    sim=(n1-n2)
    pos=abs(n1-n2)
    csim.append(sim)
    zabs.append(pos)
big=max(zabs)
eind=zabs.index(big)
if csim[eind]==zabs[eind]:
    print '1', big
else:
    print '2', big
