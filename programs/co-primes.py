def gcd(a,b):
    if a>b:
        small=b
    else:
        small=a
    for i in range(1,small):
        if((a%i==0) and (b%i==0)):
            gcd=i
    return gcd
a=int(input("enter number:"))
b=int(input("enter number:"))
gcd(a,b)
if gcd(a,b)==1:
    print(a,b, "are co-primes")
else:
    print(a,b ,"are not co-primes")
    

