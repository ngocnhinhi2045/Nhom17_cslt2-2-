n=int(input('Enter an integer (2 or greater): '))
print('The prime factors of',n,'are:')
i=2
while i<=n:
    if n%i==0:
        print(i)
        n=n//i
    else:
        i=i+1