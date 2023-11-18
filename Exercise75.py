n=int(input('n='))
m=int(input('m='))
d=min(n,m)
while n%d!=0 or m%d!=0:
    d=d-1
print ('the greatest common divisor of',n, 'and', m,':',d)