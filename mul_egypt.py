def mult_egypt(n,m):
    resultat=0
    while n!=0:
        if(n%2)==1:
            resultat+=m
            n>>=1
            m<<=2
        return resultat

test = mult_egypt(1,3)
print(test)


