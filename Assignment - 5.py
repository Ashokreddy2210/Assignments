#!/usr/bin/env python
# coding: utf-8

# In[ ]:



get_ipython().set_next_input("1. What does an empty dictionary's code look like");get_ipython().run_line_magic('pinfo', 'like')


 Empty dictionary  is denoted by a set of curly braces {} with nothing inside.


# In[ ]:



2. What is the value of a dictionary value with the KEY 'foo' and the value 42?

In this case, the key is 'foo' and the value is 42.


# In[ ]:


get_ipython().set_next_input('3. What is the most significant distinction between a dictionary and a list');get_ipython().run_line_magic('pinfo', 'list')

The most significant distinction between a dictionary and a list  is the way they are indexed


# In[ ]:


4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

When we try to get it we get a KEY ERROR 


# In[ ]:


5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and
'cat' in spam.keys()?

No difference 


# In[ ]:


6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and
'cat' in spam.values()?

'cat' in spam checks for 'cat' key in dictionary
'cat' in spam.values() checks for value 'cat' in spam


# In[ ]:


get_ipython().set_next_input('7. What is a shortcut for the following code');get_ipython().run_line_magic('pinfo', 'code')
if 'color' not in spam:
spam['color'] = 'black'


spam.setdefault('color','black')


# In[ ]:


get_ipython().set_next_input('8. How do you "prettyprint" dictionary values using which module and function');get_ipython().run_line_magic('pinfo', 'function')

pprint.pprint()

