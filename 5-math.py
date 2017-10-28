#math
#polar coordinates
import cmath
z= complex(input())
distance= abs(z)
a= cmath.phase(z)
print (distance)
print (a)


#math
#2-find angle mbc
import math
l1= int(input())
l2= int(input())
l= l1/l2
rad= math.atan(l)
deg= str(round(math.degrees(rad)))
print ((deg)+"°")

#math
#3-triangle quest 2
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (((10**i-1)//9)**2)


#math
#4-divmod
a= int(input())
b= int(input())
print (a//b)
print (a%b)
print (divmod(a,b))

#math
#5-power
a= int(input())
b= int(input())
m= int(input())
print (a**b)
print (pow(a,b,m))

#math
#6-integers
a= int(input())
b= int(input())
c= int(input())
d= int(input())
print (a**b+c**d)


#math
#7-triangle quest
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**(i)//9)*i)

