import math
fin=open('prime.txt', 'r')
prime=fin.read()
prime=prime.split()
i=0    
del prime[0]
while i<len(prime):
    prime[i]=int(prime[i])
    i+=1
print(prime[0:10])
i=9    
while True:
    if i in prime:
        i+=2
    else:
        k=0
        j=prime[k]
        while j<i:
            t=(i-j)/2
            s=math.sqrt(t)
            s=math.floor(s)
            if t==s*s:
                i+=2
                break
            else:
                k+=1
                j=prime[k]
        else:
            print(i)
            break
