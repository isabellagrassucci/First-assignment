#basic data types
#1-lists
if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        n= input().split()
        cmd= n[0]
        arg= n[1:]
        if cmd!= "print":
            cmd+= "("+ ",".join(arg) +")"
            eval("lst."+cmd)
        else:
            print (lst)

#basic data types
#2-tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t= tuple(integer_list)
    print (hash(t))

#basic data types
#3-list comprehension
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print ([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k)!=n)])

#basic data types
#4-find the second largest number
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    s= set(arr)
    l= list(s)
    l.sort()
    print (l[-2])


#basic data types
#5-nested lists
if __name__ == '__main__':
    scores = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])
    scores.sort(key=lambda x: (x[1], x[0]))
    #lowest score evur
    minScore = scores[0][1]
    while min(scores, key=lambda x: x[1])[1] == minScore:
        scores.pop(0)
    for i in filter(lambda x: x[1] == scores[0][1], scores):
        print(i[0], sep ='\n')

#basic data types
#6-find the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sum=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in (student_marks[query_name]):
        sum+= i
    print ("%.2f" % (sum/3))
