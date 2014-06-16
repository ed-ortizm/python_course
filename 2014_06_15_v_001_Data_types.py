
# coding: utf-8

## My First Programa in Python.

# In[5]:

# My first program is just printing printin hola mundo

print "Hola mundo"

#As we can see, it is like talking to python


# We see the simbol #, used to make comments an the code. It is useful for documenting the program, and make it more easy to maintain...

## Introductory Course to Python

### Data types:

# * int
# * float
# * String
# * Boolean
# * Tuples
# * List
# * Dictionaries
# * Sets

## Numbers:

# Type int and float are just representations of real numbers. Let's see the next example :

# In[7]:

print 0.1234567890123456789


# How I know the tipe of number I'm using : We can ask we the funtcion *Type*

# In[13]:

print type(0.1)
print type(1)


# We also have the functions **int()** and **float()** for going back and for between every represetation :
# 

# In[17]:

print 'el 1 es', type(1)
print 'el', float(1), 'es', type(float(1))


### Operation with Numbers

# * Addition $\longrightarrow$ **+**
# * Substraction $\longrightarrow$ **-**
# * Multiplication $\longrightarrow$ ** * **
# * Division $\longrightarrow$ **/**
# * Exponentiation $\longrightarrow$ ** ** **
# * Module $\longrightarrow$ **\**

                Every operation follows some rules :
                
# * int **op** int **$\longrightarrow$** int
# * int **op** float **$\longrightarrow$** float
# * float **op** float **$\longrightarrow$** float

# In[32]:

type(1+1),type(1/2)


# In[33]:

type(1/2.0),type (1.0 +2.0)


### Arithmetic Expressions

# In[34]:

1+3*2**5-2/2.0


# #How python rules the operations in this expression ?#
# Well the key  worl is **Please Excuse My Dear Sally**
# * **Please** $\longrightarrow$ ()
# * **Excuse** $\longrightarrow$ ** ** **
# * **M** $\longrightarrow$ ** * **
# * **Dear** $\longrightarrow$ ** / **
# * **Sally** $\longrightarrow$ **+,-**

# In[36]:

print (2**5) 


# In[37]:

print 32 * 3


# In[38]:

print 2/2.0


# In[40]:

print 1 + 96 -1.0


# **We suggest the use of parenthesis**, we the aims of having a clean code.

### Quiz

# Guess the right answer and then use python to compute then following the rules of thumb given before:

# * 1 ** * ** 2 + 3 ** * **4
# * (1 ** * ** 2) + (3 ** * **4)
# * 1 ** * ** (2 + 3) ** * **4

## Strings

# **"Hola mundo"** is a string. Strings must be between single or double quotes. if a number is between quotes, it is treated as a string.  Strings are indexed by sequential integers, starting with zero.

# In[52]:

print "hola mundo"
print 'hola mundo'
print type("hola mundo")
print type('0.1234567')


### Operations with strings:

# In this case we are going to cover just some aspects:

# In[59]:

print "Hola" + 'Mundo'
print "Hola " + 'Mundo'
print "Hola", 'Mundo'
print "Hola \t Mundo"
print "Hola Mundo \n"
print "Hi"


# If a number is a string, it can be redefined as a number using int() an float() funtions :

# In[61]:

print type('1.7')
print type(float('1.7'))


# To know the lenght of a string we use the function **len()**:

# In[138]:

print len('Hola mundo')


# To have access to a string element we use the notation my_string[n]; where n is an integer from 0 to len(my_string)

# In[156]:

print "hola mundo"[0]
print "hola mundo"[1]
print "hola mundo"[2]
print "hola mundo"[3]


# We can also stract a string from a string using the notation my_string[m:n]; where m and n are integers **ranging from 0 to len(my_string)**.

# In[155]:

print "hola mundo"[0:4]
print "hola mundo"[4:10]
print "hola mundo"[5:10]


## Boolean 

# Boolean data type assume just two values:
# * True
# * False

# In[64]:

print type(True)
print type(False)


# Opereations between this data type :
# * operator **and**
# * operator **or**
# * operator **not**
# 

# **and**

# In[157]:

print True  and True
print True  and False
print False and False  


# **or**

# In[66]:

print True  or True
print True  or False
print False or False


# **not**

# In[70]:

print not (True)
print not (False)


### Aritmetic Expressions

# In[84]:

print False and True or True


# The output shows how the operator **and** has priority over the operator **or**.
# Step by step we can note it :

# * Considering **and** as the first option

# In[85]:

print False and True


# In[86]:

print False or True


# Bingo!! we've got the right answer. Now let's considere **or** as a firs option:

# In[87]:

print True or True


# In[88]:

print False and True


# As we can see, this is not the right answer. This order is related as the way programmers see **and** and **or** :
# * and $\longrightarrow$ multiplication.
# * or  $\longrightarrow $ adition

# **However, parenthesis are considered in first place. Let's consider the same exmaple:**

# In[89]:

print (False and True) or True
print False and (True or True)


### Generating Boolean Values

# Boolean values are generated usin comparison operators :
# * **<** , **<=** : less than , less than  or equal to
# * **>** , **>=** : greater than, greater than or equal to
# * **==** : equal to

# **Examples**

# In[94]:

print 2 < 3 , 2 <= 3


# In[95]:

print 2 > 3 , 2 >= 3


# In[98]:

print 2 < 2 , 2 <= 2


# In[97]:

print 2 > 2 , 2 >= 2


# There is another way to generate **Boolean** types with the function **bool(argument)**. The number **0** an empty string **'  '** and not argument, are False values.
# The other data types are True. Let's see: 

# In[103]:

print bool() , bool('') , bool(0)


# In[105]:

print bool('0'),bool(1), bool("hola mundo")


## Tuples

# Tuples are groups of things in some order. Once they are defined, they cannot be changed (like strings). The group of things inside a tuple may be any kind of data type, even more tuples.Tuples' elements as strings' elements are indexed  by sequential integers, starting with zero. A tuple is created using parenthesis; **(element_0,... )**: 

# In[160]:

my_tuple = ('a',1,"Hola mundo",("Hola","mundo"))
print my_tuple
print type(my_tuple)


# We cand get elements of a tuple using the next pattern :

# In[122]:

print my_tuple[2]
print my_tuple[3][0], my_tuple[3][1]


# As stated before, tuple elemets can not be changed :

# In[128]:

my_tuple[2] = 'Nuevo mundo'


# We can also generate tuples from strings using the function **tuple**:

# In[127]:

print tuple("Hola mundo")


# To know te number of elements in a tuple we use the function **len(arg)**, as we did in strings :

# In[133]:

print len(my_tuple)
print len('hola mundo')
print len(my_tuple[2])


# As in strings, we can get tuples from tuples :

# In[172]:

print my_tuple[0:2]
print type(my_tuple[0:2])
print my_tuple[0:3]
print type(my_tuple[0:3])


## List

# A **list** is a sequence of different kinds of data. It differs from **Tuples**, because its elements can be changed. As in tuples, elements are indexed. A list is created using square brackets **[element_0,...]**.

# In[162]:

my_list = ["hola mundo",('hola','mundo'),['hola','mundo']]
print my_list
print type(my_list)


# As in tuples and strings, we can see every element of the list using the indexion property :

# In[164]:

print my_list[0]
print my_list[1][0],my_list[1][1]
print my_list[2][0],my_list[2][1]


# **Number of elements**

# In[166]:

print len(my_list)
print len(my_list[1])


# **Lists from a list**

# In[169]:

print my_list[1:2]
print type(my_list[1:2])


# **Changin elements**

# In[177]:

my_list[2][0] = 'hi'
my_list[2][1] = 'world'
print my_list[2][0] , my_list[2][1]


## Dictionaries

# **Dictionaries** are a sequence of differen data types, indexed by keys. The sintax for creating a dictionary is : {key_1 :element_1... }

# In[173]:

my_dictionary = {'a': "Hola mundo",'b':['hola','mundo'], 'c':('hola','mundo') }
print my_dictionary


# to **recover** an element we use the keys :

# In[175]:

print my_dictionary['a']
print my_dictionary['b'][0] , my_dictionary['b'][1]
print my_dictionary['c'][0] , my_dictionary['c'][1]


# **Changing elements:** in this case we use the keys:

# In[183]:

my_dictionary['b'][0] = 'hi'
my_dictionary['b'][1] = 'world'
print my_dictionary['b'][0], my_dictionary['b'][1]


## Sets

# a **set** is like a **dictionary** but there are not equal items. To construct a set we just use **the function set()**

# In[188]:

my_ls = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
my_set = set(my_ls)
print my_set
print type(my_set)


# Sets do not support indexing:

# In[189]:

print my_set[1]


# Well this is all for the moment **;)**
