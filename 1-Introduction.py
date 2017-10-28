#introduction
#1 hello world
if __name__ == '__main__':
    print("Hello, World!")
    
                
#introduction
#2 if-else
if __name__ == '__main__':
    n = int(input())
    if n%2!=0:
        print ("Weird")
    else:
        if 2<=n<=5:
            print ("Not Weird")
        if 6<=n<=20:
            print ("Weird")
        if n>20:
            print ("Not Weird")
            
#introduction
#3 arithmetic operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a+b)
    print (a-b)
    print (a*b)
    
    
#introduction
#4 division
from __future__ import division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a//b)
    print (a/b)
    
#introduction
#5 loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print (i**2)

                                                
#introduction
#6-write a function            
def is_leap(year):
    leap = False
    if year%4==0:
        leap=True
        if year%100==0:
            leap=False
            if year%400==0:
                    leap= True

#introduction
#7 print function
from __future__ import print_function
if __name__ == '__main__':
    n = int(input())
    l=[]
    for i in range(n):
        l.append(i+1)
    print (*l,sep="")                                                          
                                                                                                                    
                                                                                                                                                                                

    

    
    

                    

    


        

