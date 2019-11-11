a=int(input('A class:'))
b=int(input('B class:'))
c=int(input("C class:"))
d=a//2
d1=a%2 
i=b//2
i1=b%2
f=c//2
f1=c%2
g=d1+i1+f1
if g>=1:
	print(d+i+f+g)
else:
	print(d+i+f)