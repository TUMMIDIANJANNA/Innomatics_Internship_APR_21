#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n])


# In[ ]:


#Question 2
import numpy as np
n= int(input())
x = np.random.randint(2,6,n)
print(x)
y = sorted(x,reverse=True)[1]
for i in sorted(x):
    if i == y:
        print(i)
    


# In[ ]:


#Question 2
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    max1=arr[-1]
    arr.sort(reverse=True)
    for x in arr:
        if x!=max1:
            result = x
            print(result)
            break


# In[ ]:


#Question 3
if __name__ == '__main__':
    l = []
    second_score_names = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
        scores.add(score)
    second_score = sorted(scores)[1]
    for name,score in l:
        if score == second_score:            
            second_score_names.append(name)  
    for name in sorted(second_score_names):
        print(name,end="\n")  


# In[ ]:


#Question 4
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    avg_query_name = sum(query_scores)/len(query_scores)
    print('{0:.2f}'.format(avg_query_name))


# In[ ]:


#Question 5
if __name__ == '__main__':
    N = int(input())
    L = []
for row in range(N): 
    inputs = input().split() 
    if len(inputs)==1: 
        command =inputs[0] 
    if len(inputs)==2:
        command = inputs[0] 
        e = int(inputs[1]) 
    if len(inputs)==3: 
        command = inputs[0] 
        i = int(inputs[1])
        e = int(inputs[2])

    if command=="insert":
        L.insert(i,e)
    elif command=="remove":
        L.remove(e)
    elif command=="append":
        L.append(e)
    elif command=="sort":
        L.sort()
    elif command=="pop":
        L.pop()
    elif command=="reverse":
        L.reverse()
    elif command=="print":
        print(L)


# In[ ]:


#Queation 6
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(int(i) for i in integer_list)
    print(hash(t))


# In[3]:


#Question 7
def average(array):
    Average = sum(set(array))/len(set(array))
    return "{0:.3f}".format(Average)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# In[4]:


#Question 8
_ = input().split()
arr = input().split()
A = set(input().split())
B = set(input().split())
l = sum((i in A)-(i in B) for i in arr)
print(l)


# In[ ]:


#Question 9
n = input().split()
a = set(map(int,input().split()))
m = input().split()
b = set(map(int,input().split()))
c = a.difference(b)
d = b.difference(a)
l = list(c.union(d))
for i in sorted(l):
    print(i)


# In[ ]:


#Question 10
n = int(input())
s = set()
for i in range(n):
    c_n = input()
    s.add(c_n)
print(len(s))


# In[ ]:


#Question 11
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1])) 
    elif command[0] =="discard":
        s.discard((int(command[1])))
print(sum(s))


# In[ ]:


#Question 12
n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))
d = list(a.union(b))
print(len(d))


# In[ ]:


#Questin 13
n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))
d = list(a.difference(b))
print(len(d))


# In[ ]:


#Question 14
n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))
d = list(a.intersection(b))
print(len(d))


# In[ ]:


#Question 15
n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))
d = list(a.symmetric_difference(b))
print(len(d))


# In[ ]:


#Question 16
n = int(input())
a = set(map(int, input().split()))
m = int(input())
for i in range(m): 
    comm, _ = input().split()
    b = set(map(int, input().split()))
    if comm == 'intersection_update':
        a.intersection_update(b)
    elif comm == 'update':
        a.update(b)
    elif comm == 'difference_update':
        a.difference_update(b)
    elif comm == 'symmetric_difference_update':
        a.symmetric_difference_update(b)
print(sum(a))


# In[ ]:


#Question 17
from collections import Counter
n = int(input())
rooms = list(int(x) for x in input().split())
count = Counter(rooms)
for key,value in count.items():
    if value == 1:
        print(key)


# In[ ]:


#Question 18
n = int(input())
for i in range(n):
    a = input()
    s_1= set(input().split())
    b = input()
    s_2=set(input().split())
    print(s_1.issubset(s_2))


# In[ ]:


#Question 19
a = set(input().split())
for _ in range(int(input())):
    b = set(input().split())
    if not a.issuperset(b):
        print(False)
        break
else:
    print(True)

