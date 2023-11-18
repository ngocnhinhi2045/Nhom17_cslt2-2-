q=int(input('Enter a decimal number: '))
kq=""
while q>0:
    r=q%2
    r=str(r)
    kq=r+kq
    q=q//2
print(kq)
    