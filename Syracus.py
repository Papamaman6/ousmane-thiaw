#
def Collatz(a):
    nbrlter=0
    while a!=1:
        if a%2==0:
            a=a//2
        else:
            a=3*a+1
        print (a)
    nbrlter+=1
    return (nbrlter)
var = Collatz (int(input()))
print (var)   