#sets
#1-introduction to sets

from __future__ import divison
def average(array):
    st = set(array)
    return sum(st) / len(st)
    
#sets
#2-symmetric difference
M= int(input())
m= set(map(int, input().split()))
N= int(input())
n= set(map(int, input().split()))
sd= list(m.symmetric_difference(n))
sd.sort()
for i in sd:
    print (i)
    
#sets
#3-no idea!
n,m=(input().split(), int)
arr=list(input().split())
a=set(input().split())
b=set(input().split())
happiness=0
for i in arr:
    if i in a:
        happiness+=1
    elif i in b:
        happiness+= -1
print (happiness)

#sets
#4-set.add()
s=set()
n= int(input())
for i in range(n):
    s.add(input())
print (len(s))

#sets
#5-discard remove pop
n = int(input())
s = set(map(int, input().split()))
N= int(input())
lst=[]
sum=0
for i in range(N):
    c= input().split()
    cmd= c[0]
    arg= c[1:]
    cmd+= "("+ ",".join(arg) +")"
    eval("s."+cmd)
for k in s:
    sum+= k
print (sum)
    
    
#sets
#6-union
N= int(input())
n= set(map(int, input().split()))
M= int(input())
m= set(map(int, input().split()))
print (len(n.union(m)))


#sets
#7-intersection
E= int(input())
e= set(map(int, input().split()))
F= int(input())
f= set(map(int, input().split()))
print (len(e.intersection(f)))


#sets
#8-difference
E= int(input())
e= set(map(int, input().split()))
F= int(input())
f= set(map(int, input().split()))
print (len(e.difference(f)))


#sets
#9-symmetric difference
E= int(input())
e= set(map(int, input().split()))
F= int(input())
f= set(map(int, input().split()))
print (len(e.symmetric_difference(f)))
    
#sets
#10-mutations
l= int(input())
s= set(map(int,input().split()))
n= int(input())
sm=0
for i in range(0,n*2,2):
    c= input().split()
    s1=set(map(int,input().split()))
    cmd= c[0]
    cmd+= "("+ "".join("s1") +")"
    eval("s."+cmd)
for k in s:
    sm+= k
print (sm)

#sets
#11-the captain's room
k= int(input())
l= list(map(int, input().split()))
s= set(l)
print(((sum(s)*k)-(sum(l)))//(k-1))
        
#sets
#12-check subset
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    if A.issubset(B):
        print (True)
    else:
        print (False)
        
#sets
#13-check superset
s= set(map(int,input().split()))
n= int(input())
superset= True
for i in range(n):
    a= set(map(int,input().split()))
    if a.issubset(s)== False:
        superset= False
print (superset)

    
