#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Question 1
# say Hello, World! with python
print("Hello, World!")


# In[10]:


#Question 2
n = int(input("Enter a number: "))
if n%2!=0:
    print("Weird")
elif n%2==0 and (n in range(2,6) or n>20):
    print("Not Weird")
else: 
    if n%2==0 and (n in range(6,21)):
        print("Weird")


# In[11]:


#Question 2
if __name__ == '__main__':
    n = int(input().strip())
if n%2!=0:
    print("Weird")
elif n%2==0 and (n in range(2,6) or n>20):
    print("Not Weird")
else: 
    if n%2==0 and (n in range(6,21)):
        print("Weird")


# In[12]:


#Question 3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


# In[13]:


#Question 3
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
print(a//b)
print(a/b)
        


# In[14]:


#Question 4
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# In[15]:


#Question 4
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
print(a+b)
print(a-b)
print(a*b)


# In[16]:


#Question 5
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)


# In[17]:


#Question 6
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0 and(year%400==0 or year%100!=0):
        return not leap
    else:
        return  leap
 
year = int(input())
print(is_leap(year))


# In[18]:


#Question 7
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")

