#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[1]:


# user defined function for sWap cASE method
def swap_case(s):
    result = ''
    for letter in s:
        if letter==letter.lower():
            result+=letter.upper()
        else:
            result+=letter.lower()
        
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[ ]:


#Question 2
def split_and_join(line):
    result = '-'.join(line.split())
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    


# In[ ]:


#Question 3
def print_full_name(first, last):
    # Write your code here
    print('Hello %s %s! You just delved into python.'%(first,last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# In[ ]:


#Question 4
def mutate_string(string, position, character):
    string = string[:position]+character+string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In[11]:


#Question 5
def count_substring(string, sub_string):
    count = 0
    while sub_string in string:
        s_1 = string.find(sub_string)
        string = string[:s_1] + string[s_1 + 1:]
        count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# In[ ]:


#Question 6
if __name__ == '__main__':
s = input()
l = s.strip()
a,b,c,d,e=False,False,False,False,False
for i in l:
    if i.isalnum():
        a=True
    if i.isalpha():
        b=True
    if i.isdigit():
        c=True
    if i.islower():
        d=True
    if i.isupper():
        e=True
print(a)
print(b)
print(c)
print(d)
print(e)


# In[13]:


#Question 6 using any function
s = input()
print(any([c.isalnum for c in s]))
print(any([c.isalpha for c in s]))
print(any([c.isdigit for c in s]))
print(any([c.islower for c in s]))
print(any([c.isupper for c in s]))


# In[14]:


#Question 7
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


# In[15]:


#Question 8
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[22]:


# Question 9
n, m= map(int, input().split()) 
for i in range(1,n,2): 
    print((i*'.|.').center(m,'-'))
print('WELCOME'.center(m,'-')) 
for i in range(n-2,-1,-2): 
    print((i*'.|.').center(m, '-'))


# In[ ]:


#Question 10
def print_formatted(number):
    # your code goes here
    padding = number.bit_length()
    for i in range(1, number+1):
        print(f"{i:{padding}d} {i:{padding}o} {i:{padding}X} {i:{padding}b}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# In[ ]:


# Question 11
def print_rangoli(size):
    # your code goes here
    l = list(map(chr,range(97,123)))
    l1 = l[n-1::-1]+l[1:n]
    width = len('-'.join(l1))
    for i in range(1,n):
        print('-'.join(l[n-1:n-i:-1]+l[n-i:n]).center(width,'-'))
    for i in range(n,0,-1):
        print('-'.join(l[n-1:n-i:-1]+l[n-i:n]).center(width,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# In[ ]:


#Question 12
# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# In[ ]:


#Question 13
def minion_game(string):
    # your code goes here

    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
         if s[i] in vowels:
             kevsc += (len(s)-i)
         else:
             stusc += (len(s)-i)
  
    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")
 
if __name__ == '__main__':
    s = input()
    minion_game(s)


# In[23]:


#Question 14
def merge_the_tools(string, k):
    # your code goes here
   temp = []
   len_temp = 0
   for item in string:
       len_temp += 1
       if item not in temp:
           temp.append(item)
       if len_temp == k:
           print (''.join(temp))
           temp = []
           len_temp = 0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

