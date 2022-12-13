#!/usr/bin/env python
# coding: utf-8

# # Assignment - 1 

# In[ ]:


1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.

 *   # This is an Expression for multiplying numbers

'hello' # value 

-87.8  #  value (this is a float datatype)

- # Expression used for subtraction 
(#, Expression, used, for, division)

+  # Expression used for adding numbers and strings

6   # value


# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')

STRING -  sequence of  characters closed  inside single, double, or triple quotes.

VARIABLE - It is used to  store  information.


# In[ ]:


3.Describe three different data types.

Numeric data types: int, float, complex.
String data types: str.
Sequence types: list, tuple, range.
Boolean type: bool.


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')

Expression is a  combination of operators and operands to get value 
Arithmetic Expressions = combination of numbers and operators.We use operators like 

+   Addition
–   Subtraction
*   Multiplication
Division()
(/, Quotient)
get_ipython().run_line_magic('Remainder', '')
**  Exponentiation


# In[ ]:


5. This assignment statements, like spam = 10. What is the difference between an
get_ipython().set_next_input('expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')

Expression =  combination of operators and operands to get value
Statement = instruction that the Python interpreter can execute

here spam = 10 is a statement 


# In[ ]:


get_ipython().set_next_input('6. After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1

here we are using the +1 increment function to the variable "bacon" 
ans = 23


# In[ ]:


get_ipython().set_next_input('7. What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')

'spam'+'spamspam'  =  concatinating  output will be 'spamspamspam'

'spam'*3  = multiplying the string  output will be 'spamspamspam'


# In[ ]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')

According to the rules for naming a variable. A variable cannont start with numbers

hence egg is valid and 100 is ivalid


# In[ ]:


9. What three functions can be used to get the integer, floating-point number, or string
get_ipython().set_next_input('version of a value');get_ipython().run_line_magic('pinfo', 'value')

Functions used to get  the integer, floating-point number, or string
version of a value are :
int()
float()
str()


# In[ ]:


get_ipython().set_next_input('10.Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')

'I have eaten'+99+'burritos'

This expression cause error because we can concatenate only strings when we run this we get a error  like this
TypeError: can only concatenate str (not "int") to str
    
we can fix this by removing the integer and assigning it inside the quotes 
'I have eaten 99'+" "+'burritos'

output will be = 'I have eaten 99 burritos

