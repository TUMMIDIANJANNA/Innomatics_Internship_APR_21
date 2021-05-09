#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1
T =int(input())
import re
for i in range(T):
    N = input()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$',N)))


# In[2]:


#Question 2
regex_pattern = r"\D+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


# In[ ]:


#Question 3
string = input()
import re
m = re.search(r"([a-z0-9])\1+", string)
print(m.group(1) if m else -1)


# In[ ]:


#Question 4
import re
s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
print('\n'.join(a or ['-1']))


# In[ ]:


#Question 5
import re
s = input()
v = input()
for i,x in enumerate(s):
    if re.match(v,s[i:]):
        print((i,i+len(v)-1))
if re.search(v, s)==None:
    print((-1,-1)) 


# In[ ]:


#Question 6
import re
S=int(input())
for i in range(S):
      pattern1=re.compile(r'(?<= )(&&)(?= )')
      pattern2=re.compile(r'(?<= )(\|\|)(?= )')
      print(pattern2.sub('or', pattern1.sub('and', input())))


# In[ ]:


#Question 7
thousand = "(?:(M){0,3})?"
hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"

regex_pattern = r"^" + thousand + hundred + ten + unit + "$"
import re
print(str(bool(re.match(regex_pattern, input()))))


# In[ ]:


#Question 8
test = int(input())
for i in range(test):
    string  = input()
    if(len(string)==10 and string[0] in ['9', '8', '7'] and string.isnumeric()):
        print("YES")
    else:
        print("NO")


# In[ ]:


#Question 9
import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)


# In[ ]:


#Question 10
import re
for i in range(int(input())):
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if matches:
        print(*matches, sep='\n')


# In[ ]:


#Question 11
import re

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        self.value(attrs)

    def handle_endtag(self, tag):
        print ("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        self.value(attrs)

    def value(self, attrs = None):
        if attrs:
           [print('->', attr, '>', val) for attr, val, in attrs]
ss = '\n'.join([input() for x in range(int(input()))])

parser = MyHTMLParser()

parser.feed(ss)


# In[ ]:


#Question 12
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if "\n" not in list(data):
            print(">>> Data")
            print(data)
    def handle_comment(self, data):
        if "\n" not in list(data):
            print(">>> Single-line Comment")
        else:
            print(">>> Multi-line Comment")
        print(data)
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# In[ ]:


#Question 13
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

parser = MyHTMLParser()

for i in range(int(input())):
    parser.feed(input())


# In[ ]:


#Question 14
import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')


# In[ ]:


#Question 15
import re

is_grouping = re.compile(r'^(?:.{4}\-){3}.{4}$').match
is_consecutive = re.compile(r'(.)\1{3}').search
is_valid = re.compile(r'^[456]\d{15}$').match

for _ in range(int(input())):
    card_no = input()
    if is_grouping(card_no):
        card_no = card_no.replace('-', '')
    if is_valid(card_no) and not is_consecutive(card_no):
        print('Valid')
    else:
        print('Invalid')


# In[ ]:


#Question 16
regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"	# Do not delete 'r'.



import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# In[ ]:


#Question 17
import re

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))

