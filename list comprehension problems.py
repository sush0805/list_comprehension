#!/usr/bin/env python
# coding: utf-8

# #### find all numbers in range 1-1000 which is divisible by 7

# In[2]:


div_by_sev = [x for x in range(1,1000) if x % 7 == 0]
print(div_by_sev)


# #### Find all of the numbers from 1-1000 that have a 3 in them

# In[4]:


a = [x for x in range(1,1000) if '3' in str(x) ]
print(a)


# #### Count the number of spaces in a string

# In[6]:


s = 'hii my name is harry'
l = [x for x in s if x == ' ']
print(len(l))


# #### Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”

# In[20]:


m = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
#vow = ['a,e,i,o,u',' ']
n = [x for x in m if x not in 'a,e,i,o,u," "']
print(n)


# #### Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)

# In[21]:


items=["hi", 4, 8.99, 'apple', ('t,b','n')]
result=[n for n in enumerate(items)]
print(result)


# In[23]:


a = ['hii','hello','how r u']
b = enumerate(a)
print(list(b))


# #### Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5

# In[25]:


l1 = [1,2,3,4]
l2 = [2,3,4,5]
l = [x for x in l1 if x in l2]
print(l)


# In[27]:


l1 = [1,2,3,4]
l2 = [2,3,4,5]
l = [x for x in l1 if x not in l2]
print(l)


# #### Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending'

# In[38]:


s = "In 1984 there were 13 instances of a protest with over 1000 people attending"
f = s.split()
d = [x for x in f if x.isnumeric()]
print(d)


# #### Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’

# In[43]:


a = ['even' if x % 2 == 0 else 'odd' for x in range(20)]
print(a)


# #### Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)

# In[44]:


list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2, 7, 1, 12]
g = [(a,b) for a in list_a for b in list_b if a == b]
print(g)


# #### Find all of the words in a string that are less than 4 letters

# In[47]:


s = 'hii my name is harry i am good boy'
f = s.split()
d = [x for x in f if len(x) < 4]
print(d)


# #### Use a nested list comprehension to find all of the numbers from 1-100 that are divisible by any single digit besides 1 (2-9)

# In[48]:


result = [number for number in range(1,100) if True in [True for x in range(2,10) if number % x == 0]]
print(result)


# In[ ]:




