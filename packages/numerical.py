#function to check if number is prime
def factors(n):
    count=0
    for i in range(1,n):
        if n%i==0:
            if isprime(i):
                count=count+1
    return count
def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def noofprimefactors(n):
    count=0
    for i in range(1,n):
        if n%i==0:
            if isprime(i):
                count+=1
    return count
p=int(input())
q=int(input())
for i in range(0,q):
    a=int(input())
    if noofprimefactors(a)==p:
        print("YES")
    else:
        print("NO")