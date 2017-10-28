#collections

#1-counter
from collections import Counter
x= int(input())
lst= input().split()
n= int(input())
price=0
for i in range(n):
    cust= input().split()
    if cust[0] in Counter(lst).keys():
        price+= int(cust[1])
        lst.remove(cust[0])
print (price)

#2-DefaultDict
from collections import defaultdict
dic=defaultdict(list)
lst=[]
n,m=map(int, input().split())
for i in range(n):
    dic[input()].append(i+1)
for i in range(m):
    lst+=[input()]
for i in lst:
    if i in dic:
        print(" ".join(map(str,dic[i])))
    else:
        print(-1)


#3-namedtuple
from collections import namedtuple
n = int(input())
title = (input())
element=0
Student = namedtuple('Student',title)
for i in range(n):
    x,y,z,w= input().split()
    stud= Student(x,y,z,w)
    element+= int(stud.MARKS)
average= float(element)/n
print ("%0.02f" %average)


#4-OrderedDict
from collections import OrderedDict
n=int(input())
dic= OrderedDict()
for _ in range(n):
    item_name,net_price= input().rsplit(None,1)
    net_price= int(net_price)
    if item_name in dic:
        dic[item_name]+= net_price
    else:
        dic[item_name]= net_price
for i,j in dic.items():
    print (i,j)


#5-word order
from collections import *
n=int(input())
lst=[]
for i in range(n):
    lst.append(input())
dic=OrderedDict()
for i in lst:
    if i not in dic:
        dic.update({i:1})
        continue
    dic[i]+=1
print(len(dic))
print(*dic.values())



#6-deque
from collections import deque
deq= deque()
n=int(input())
for _ in range(n):
    line= input().split()
    cmd= line[0]
    arg= line[1:]
    cmd+= "("+ "".join(arg)+")"
    eval("deq."+cmd)
print (*deq)



#7-piling up!
from collections import deque
n=int(input())
for i in range(n):
    num_cubes=int(input())
    cubes=deque(map(int,input().split()))
    maxx=max(cubes)
    while len(cubes)>=1:
        if cubes[0]>=cubes[len(cubes)-1] and cubes[0]<=maxx:
            maxx=cubes[0]
            cubes.popleft()
        elif cubes[0]<=cubes[len(cubes)-1] and cubes[len(cubes)-1]<=maxx:
            maxx=cubes[len(cubes)-1]
            cubes.pop()
        else:
            break
    if len(cubes)>0:
        print("No")
    elif len(cubes)==0:
        print("Yes")



#8-most common
#!/bin/python3

import sys
from collections import OrderedDict
from operator import itemgetter
if __name__ == "__main__":
    s = input().strip()
    dic=OrderedDict()
    for i in s:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    a=sorted(dic.items(), key= lambda x: (-x[1],x[0]))
    for i in range(3):
        print(*a[i])