#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. What exactly is []?

list value that contains no items.


# In[ ]:


2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)
Let's  pretend the spam includes the list ['a','b','c','d'] for the next three queries.


 spam[2] = 'hello' 


# In[ ]:


3. What is the value of spam[int(int('3' * 2) / 11)]?

value of spam = [3]  i.e 'd'


# In[ ]:


4. What is the value of spam[-1]?

'd'


# In[ ]:


5. What is the value of spam[:2]?
Lets pretend bacon has the list [3.14, 'cat,'11,'cat,'True] for the next three questions.

['a','b']


# In[ ]:


6. What is the value of bacon.index('cat')?

1


# In[ ]:


get_ipython().set_next_input('7. How does bacon.append(99) change the look of the list value in bacon');get_ipython().run_line_magic('pinfo', 'bacon')

 [3.14, 'cat', 11, 'cat', True, 99]


# In[ ]:


get_ipython().set_next_input("8. How does bacon.remove('cat') change the look of the list in bacon");get_ipython().run_line_magic('pinfo', 'bacon')

 [3.14, 11, 'cat', True]


# In[ ]:


get_ipython().set_next_input('9. What are the list concatenation and list replication operators');get_ipython().run_line_magic('pinfo', 'operators')

+ is used for concatination 
* is used for replication


# In[ ]:


10. What is difference between the list methods append() and insert()?

 append() will add values only to the end of a list, 
 insert() can add them anywhere in the list.


# In[ ]:


get_ipython().set_next_input('11. What are the two methods for removing items from a list');get_ipython().run_line_magic('pinfo', 'list')

Two methods are del statement and remove()  for removing items from a list


# In[ ]:


12. Describe how list values and string values are identical.

Both strings and lists have lengths: a string's length is the number of characters in the string; a list's length is the number of items in the list.


# In[ ]:


get_ipython().set_next_input('13. Whats the difference between tuples and lists');get_ipython().run_line_magic('pinfo', 'lists')

Lists are mutable which are written using square brackets []
Tuples are immutable which are written using parentheses ()


# In[ ]:


14. How do you type a tuple value that only contains the integer 42?

(42,)


# In[ ]:


get_ipython().set_next_input('15. How do you get a list values tuple form? How do you get a tuple values list form');get_ipython().run_line_magic('pinfo', 'form')

list() and tuple()


# In[ ]:


16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they
get_ipython().run_line_magic('pinfo', 'contain')

It contain references to list values.


# In[ ]:


17. How do you distinguish between copy.copy() and copy.deepcopy()?

 copy.copy() function will do a shallow copy of a list 
copy.deepcopy() function will do a deep copy of a list
copy .deepcopy() will duplicate any lists inside the list


# In[ ]:




