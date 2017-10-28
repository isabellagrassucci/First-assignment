#strings
#1-swap-case    
def swap_case(s):
    a= s.swapcase()
    return a

#strings
#2-split and join        
def split_and_join(line):
    # write your code here
    l= line.split()
    line= "-".join(l)
    return line
    
#strings
#3-what's your name    
def print_full_name(a, b):
    print ("Hello "+a+" "+b+"! You just delved into python.")
    
#strings
#4-mutation
def mutate_string(string, position, character):
    string= string[:position]+ character+ string[position+1:]
    return string
    
#strings
#5-find a string
def count_substring(string, sub_string):
    c = 0
    l= len(sub_string)
    for i in range((len(string) - l)+ 1):
        if string[i:i + l] == sub_string:
            c = c + 1
    return c

#strings
#6-string validators
if __name__ == '__main__':
    s = input()
    alnum=False
    alpha=False
    digit=False
    lower=False
    upper=False
    for i in s:
        if alnum==False:
            if i.isalnum()==True:
                alnum=True
        if alpha==False:
            if i.isalpha()==True:
                alpha=True
        if digit==False:
            if i.isdigit()==True:
                digit=True
        if lower==False:
            if i.islower()==True:
                lower=True
        if upper==False:
            if i.isupper()==True:
                upper=True
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)



#strings
#7-text alignments
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


#strings
#8-text wrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

#strings
#9-designer door math
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):
    print ((".|."*i).center(M,"-"))
print ("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2):
    print ((".|."*i).center(M,"-"))

#strings
#10-string formatting
def print_formatted(number):
    # your code goes here
    width=len(bin(number)[2:])
    for i in range(1, number+1):
        a=str(oct(i)[2:])
        b=str(hex(i)[2:]).upper()
        c=str(bin(i)[2:])
        d=str(i)
        print ((str(i)).rjust(width, " ")+(str(oct(i)[2:])).rjust(width+1, " ")+(str(hex(i)[2:]).upper()).rjust(width+1, " ")+(str(bin(i)[2:])).rjust(width+1, " "))


#strings
#11-aplhabet rangoli
from string import ascii_lowercase as ass
def print_rangoli(size):
    # your code goes here
    n = size*4 -3
    s = ass[:size][::-1]
    for i in range(1,size+1):
        locale = s[:i] # i = 5; locale = 'edcba'
        totale = '-'.join(locale + locale[::-1][1:])
        print(totale.center(n, '-'))
    for k in range(1,size)[::-1]:
        locale=s[:k]
        totale= "-".join(locale+locale[::-1][1:])
        print (totale.center(n,"-"))

#strings
#12-capitalize!
def capitalize(string):
    l= string.split(" ")
    lst=[]
    for i in l:
        el= i.capitalize()
        lst.append(el)
    st= " ".join(lst)
    return st


#strings
#13-The minion game
def minion_game(string):
    # your code goes here
    k=len(string)
    kevin=0
    for i in range(k):
        if string[i] in "AEIOU":
            kevin+=(k-i)
        stuart=k*(k+1)/2-kevin
    if stuart>kevin:
        print ("Stuart",int(stuart))
    elif kevin>stuart:
        print ("Kevin", int(kevin))
    else:
        print ("Draw")

#strings
#14-marge the tools
def merge_the_tools(string, k):
    # your code goes here
    lst=[]
    for i in range(0,len(string),k):
        lst.append(string[i:i+k])
    for el in lst:
        string=""
        for j in el:
            if j not in string:
                string+= j
        print (string)
