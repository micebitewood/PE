
fin=open('G:\Dropbox\PE\prime.txt', 'r')
prime=fin.read()
prime=prime.split()
del prime[0]
i=0
while i<len(prime):
    prime[i]=int(prime[i])
    i+=1
i=0
count=[0 for x in range(0, 1000000)]
while i<len(prime):
    j=prime[i]
    while j<1000000:
        count[j]+=1
        j+=prime[i]
    i+=1
i=0
while i<1000000:
    if count[i+3]==4:
        if count[i+2]==4:
            if count[i+1]==4:
                if count[i]==4:
                    print(i)
                    break
                else:
                    i+=1
            else:
                i+=2
        else:
            i+=3
    else:
        i+=4