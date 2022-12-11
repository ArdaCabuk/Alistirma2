L=[]
for n in range(10000,100000):
    for i in range(2,n):
        if (n%i)==0:
            break
    else:
        L.append(n)
for x in L:
    x1=x//10
    for i1 in range(2,x1):
        if (x1%i1)==0:
            break
    else:
        x2=x1//10
        for i2 in range(2,x2):
            if (x2%i2)==0:
                break
        else:
            x3=x2//10
            for i3 in range(2,x3):
                if(x3%i3)==0:
                    break
            else:
                x4=x3//10
                for i4 in range(2,x4):
                    if(x4%i4)==0:
                        break
                else:
                    print(x)