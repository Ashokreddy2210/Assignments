#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')

Boolean datatypes have two values true & false. we write them as True & False they should start with capital letter


# In[ ]:


get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')

Three types of booleanoperators are
AND
OR
NOT


# In[ ]:


3. Make a list of each Boolean operator(i.e. every possible combination of Boolean
values for the operator and what it evaluate ).

AND OPERATOR  returns  true only if all the inputs are true
    
   A     B      A AND B
FALSE  FALSE     FALSE
FALSE  TRUE      FALSE
TRUE   FALSE     FALSE
TRUE   TRUE      TRUE


OR OPERATOR returns true if any of the input  values is  true

 A       B      A OR B
FALSE  FALSE    FALSE
FALSE  TRUE     TRUE
TRUE   FALSE    TRUE
TRUE   TRUE     TRUE

NOT OPERATOR returns true if the input is false 

  A     NOT A
FALSE    TRUE
TRUE     FALSE


# In[ ]:


get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
(5 > 4) and (3 == 5)                       # false   
not (5 > 4)                                # false
(5 > 4) or (3 == 5)                        #true
not ((5> 4) or (3 == 5))                   # false
(True and True) and (True == False)        # false
(not False) or (not True)                  #true


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')
 ==    EQUALS 
 >     GREATER THAN
 <     LESS THAN 
 >=    GREATER THAN OR  EQUAL TO
 <=    LESS THAN OR EQUAL TO
 get_ipython().system('=    NOT EQUAL TO ')


# In[ ]:


6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.

=  IT IS USED TO ASSIGN VALUES THIS IS AN ASSIGMENT OPERATOR
==  (EQUAL) THIS RELATIONAL OPERATOR IS  USED TO  CHECK THE OPERANDS ARE EQUAL ARE NOT 

A = 10  # here we use (=) assignment operator for assigning 10 on right to A

(3 == 5) #  this relational operator  is used to find the relation between two operands and returns in boolen value either 'true' or 'false' 


# In[ ]:


7. Identify the three blocks in this code: 
    
spam = 10
if spam == 10:
    print('eggs')    # 1st block
if spam > 5 :
    print('bacon')   # 2nd block
else :
    print('ham')     # 3rd block
    print('spam')
    print('spam')


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.

spam = 1 
if spam == 1 :
    print("Hello")
elif spam == 2 :
    print("Howdy")
else:
    print("Greetings!")


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')

We can stop the loop by pressing CTRL+C


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

break and continue are used to skip the iteration of the loop
break statement is used to  terminate whole loop
continue statement  is used to skip the current iteration
 


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

All the three are same they give output  from 0-9 


# In[38]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.

for i in range(1,11) :
    print(i)


# In[37]:


i = 1
while i<11:
    print (i)
    i = i + 1


# In[ ]:


13. If you had a function named bacon() inside a module named spam, how would you call it after
get_ipython().set_next_input('importing spam');get_ipython().run_line_magic('pinfo', 'spam')

we can call it by using    spam.bacon()

