def fib(n):
    a=0
    b=1
    l=[0,1]
    if n==0:
        print(a)
    elif n==1 or n==2:
        print(b)
    else:
        for i in range(2,n):
            c=a+b
            l.append(c)
            a=b
            b=c
        print(l)
n=int(input("enter number:"))
print("first n fibonocci numbers:\t")
fib(n)
print("nth fibonocci number:",l[n-1])
print("elements upto n fiboncci number:\t")
for i in range(0,n):
    if l[i]<=n:
        print(l[i])
