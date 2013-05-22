def share(i, j):
    list_i=[]
    list_j=[]
    for k in range(0, 4):
        list_i.append(i%10)
        i//=10
        list_j.append(j%10)
        j//=10
    list_i.sort()
    list_j.sort()
    for k in range(0, 4):
        if list_i[k] != list_j[k]:
            return False
    return True
fin=open('prime.txt', 'r')
prime=fin.read()
prime=prime.split()
i=0
while i<len(prime):
    prime[i]=int(prime[i])
    i+=1
for i in prime:
    if i>1000 and i<10000:
        for j in prime:
            if j>i and j<10000 and share(i,j):
                for k in prime:
                    if k>j and k<10000 and share(i,k):
                        if i+k==2*j:
                            print(i,j,k)
