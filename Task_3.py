#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Question 1
import cmath
z = input()
pa = cmath.phase(complex(z))
r = abs(complex(z))
print('{0}\n{1}'.format(r,pa))


# In[6]:


#Question 2
from math import *
ab = float(input())
bc = float(input())
print(str(int(round(degrees(acos(bc/hypot(ab,bc))),0)))+chr(176))
# or we can use atan(ab/bc) you can get the same results


# In[1]:


#Question 3
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i//9)**2)


# In[ ]:


#Question 4
a = int(input()) ; b = int(input())
print(a//b)
print(a%b)
print(divmod(a,b))


# In[ ]:


#Question 5 
a = float(input()); b = float(input()); m = float(input())
from math import*
print(int(pow(a,b)))
print(int(pow(a,b)%m))


# In[ ]:


#Question 6
a = int(input()); b = int(input()); c = int(input()); d = int(input())
print(a**b+c**d)


# In[2]:


#Question 7
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i//9)*i)

