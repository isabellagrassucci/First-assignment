#itertools
#1-product
from itertools import product
a= list(map(int,input().split()))
b= list(map(int,input().split()))
print (*product(a,b))

#itertools
#2-permutations
from itertools import permutations
l= input().split()
string= str(l[0])
lenght= int(l[1])
perm= list(permutations(string,lenght))
perm.sort()
for i in perm:
    s= "".join(i)
    print (s)

#itertools
#3-combinations
from itertools import combinations
l= input().split()
string= list(l[0])
lenght= int(l[1])
string.sort()
string= "".join(string)
comb=[]
for i in range(1,lenght+1):
    comb.append(list(combinations(string,i)))
for j in comb:
    for k in j:
        s= "".join(k)
        print (s)

#itertools
#4-comb with replacement
from itertools import combinations_with_replacement
l= input().split()
string= list(l[0])
string.sort()
lenght= int(l[1])
comb= list(combinations_with_replacement(string,lenght))
for i in comb:
    s= "".join(i)
    print (s)


#itertools
#5-compress the string
from itertools import groupby
for i,j in groupby(input()):
    print((len(list(j)), int(i)), end=" ")


#itertools
#6-iterables and iterators
from itertools import combinations
n= int(input())
l= list(range(1,n+1))
lst= input().split()
k= int(input())
ind=[]
comb= list(combinations(l,k))
for i in range(len(lst)):
    if 'a' in lst[i:]:
        id= lst.index('a',i)
        ind.append(id+1)
counter=0
for j in comb:
    for w in ind:
        if w in j:
            counter+=1
            break
prob= counter/len(comb)
print ("%0.12f" %prob)

#itertools
#7-maximize it
from itertools import product
k, m = map(int, input().split())
lst = []
for _ in range(k):
    lst.append([x ** 2 for x in map(int, input().split()[1:])])
comb = list(product(*lst))
print (max(sum(x) % m for x in comb))
