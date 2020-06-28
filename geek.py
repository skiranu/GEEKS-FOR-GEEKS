n=int(input('Enter the number of terms:'))
def count(x):
    if x=='0':
        return True
def count1(x):
    if x=='1':
        return True
if n<=20:
    for i in range(n):
        c=0
        x=0
        d=input('Enter the input string:')
        k=len(d)
        for x in range(k):
            if count1(d[x])==True:
                f=x+1
                for n in range(f,k-1):
                    if count(d[n])==True:
                        if count1(d[n+1])==True:
                            c+=1
                        else:
                            continue
                    else:
                        break
            else:
                x+=1
        print(c)
