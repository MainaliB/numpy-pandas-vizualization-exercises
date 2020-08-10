#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
# imported numpy as np


# In[2]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7]) # created an array


# In[3]:


#1.How many negative numbers are there?
# indexing using less than 0 and then using the shape function to get the number of negative numbers
a[a<0].shape


# In[4]:


#2.How many positive numbers are there?
# indexing using greater than 0 and then using the shape function to get the number of positive numbers
a[a>0].shape 


# In[5]:


#3.How many even positive numbers are there?
a[(a>0)&(a%2==0)].shape # using and to get the positive and even numbers from array


# In[8]:


#4.If you were to add 3 to each data point, how many positive numbers would there be?
b = a+3
b[b>0].shape # first we add three to the data and then use greater than 0 filter to get the positive numbers


# In[16]:


#5. If you squared each number, what would the new mean and standard deviation be?
c = a**2 # first we square each number in the array, then calculate the mean and standard deviation using the function
print(f"The new mean is {c.mean()}")
print(f"The new standard deviation is {c.std()}")


# In[20]:


#6. A common statistical operation on a dataset is centering. 
#This means to adjust the data such that the center of the data is at 0. 
#This is done by subtracting the mean from each data point. Center the data set.

# we simply subtract the mean from the elements in array to center the data set

a-a.mean()


# In[26]:


#7. Calculate the z-score for each data point. Recall that the z-score is given by:
z_score = (a-a.mean())/a.std() # we calculate the z score using the z score formula
print(f"The z score is {z_score}")


# In[29]:


#8.Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py 
#and add your solutions. 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a) # using the sum function to get the sum of all the elements in a list
sum_of_a  


# In[31]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a) # using the min function to get the minimum value from within the list
min_of_a


# In[33]:


#Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a) # using the max function to get the maximum value within a list
max_of_a


# In[36]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a)/len(a) 
#using the sum to get the total sum and len to get the len and dividing the sum by len to get the average
mean_of_a


# In[41]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all
#the numbers in the above list together
total_product = 1   # using for loop tp get the product of all the elements in the list
for n in a:
    total_product = n * total_product
total_product


# In[43]:


# Exercise 6 - Make a variable named squares_of_a. 
#It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [n**2 for n in a] # using list comprehension to get the square of each element in the list
squares_of_a


# In[45]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers.
odds_in_a = [n for n in a if n%2==1] # using list comprehension to get the odds in the list
odds_in_a


# In[47]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [n for n in a if n%2 == 0] # using list comprehension to get the evens in the list
evens_in_a


# In[48]:


## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]


# In[87]:


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable.
#**Hint, you'll first need to make sure that the "b" variable is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)
# sum_of_b 
b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array(b)
b.sum() # just using the sum function in numpy to get the sum
b.shape


# In[86]:


# Exercise 2 - refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
# min_of_b
b.min() # using the min function from numpy to get the mean


# In[60]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
b.max() # using the max function from numpy to get the max


# In[61]:


# Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
b.mean() # using the mean function from numpy to get the mean


# In[63]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number
b.prod() # using the prod function from numpy to get the product


# In[83]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2) 
b**2 # vectorized operations of arrays in numpy is simple so we use the basic python syntax to get the square of each element in an array


# In[65]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)
b[b%2==1] # we index the array to get the numbers that have remainder of 1 when divided by 2


# In[66]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)
b[b%2==0]#we index the array to get the numbers that have remainder of 0 when divided by 2


# In[88]:


# Exercise 9 - print out the shape of the array b.
b.shape # using .shape function to get the dimension of an array


# In[93]:


# Exercise 10 - transpose the array b.
c = np.transpose(b) # transpose function allows you to transpose the array
c.shape


# In[92]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
d = np.reshape(b, (1,6)) # reshaping using the numpy builtin reshape function
d


# In[94]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
e = np.reshape(d,(6,1)) # reshaping using the numpy builtin reshape function
e


# In[96]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array(c)
c


# In[97]:


# Exercise 1 - Find the min, max, sum, and product of c.
# you can calculate the min,max,sum,and product of an array using the built in functions
print(f"The min of c is {c.min()}, the max is {c.max()}, the sum is {c.sum()} and the product is {c.prod()}")


# In[98]:


# Exercise 2 - Determine the standard deviation of c.
# the standard deviation is calculated using the built in std() function
print(f"The standard deviation of c is {c.std()}")


# In[100]:


# Exercise 3 - Determine the variance of c.
# Variance is the square of the standard deviation. So,
variance = (c.std())**2
variance


# In[101]:


# Exercise 4 - Print out the shape of the array c
c.shape #.shape function prints the dimensions of the array


# In[105]:


# Exercise 5 - Transpose c and print out transposed result.
d = np.transpose(c) # np.transpose() allows the transpose of an array
d


# In[107]:


# Exercise 6 - Get the dot product of the array c with c. 
e = np.dot(c,c) #.dot function allows you to conduct matrix multiplication in numpy
e


# In[121]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
f = np.transpose(c) # transpose c 
g = c*f # multiply c with its transposed version

g.sum() # get sum using the sum function


# In[120]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
h = c*f # we have already transposed c and assigned it to f
h.prod() # using the .prod function to get the product of the elements in the array


# In[123]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)
d


# In[126]:


# Exercise 1 - Find the sine of all the numbers in d
np.sin(d) # .sin function allows you to get the sine of all the number in an array


# In[127]:


# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d) # .cos function allows you to get the cosine value of the elemen in array


# In[128]:


# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d) #.tan function allows you to get the tangent value of elements in an array


# In[129]:


# Exercise 4 - Find all the negative numbers in d
d[d<0] # indexing with a condition d is less than 0


# In[130]:


# Exercise 5 - Find all the positive numbers in d
d[d>0] # indexing with a condition d is greater than 0


# In[131]:


# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d) # .unique function allows you to get the unique value of an array


# In[132]:


# Exercise 7 - Determine how many unique numbers there are in d.
np.unique(d).shape # first we use the .unique function to get the unique values then use .shape function to get the count


# In[133]:


# Exercise 8 - Print out the shape of d.
d.shape # .shape function allows you to get the shape of an array


# In[134]:


# Exercise 9 - Transpose and then print out the shape of d.
z = np.transpose(d) #transpose function transposes the array
z.shape   #shape function gives the dimension


# In[136]:


# Exercise 10 - Reshape d into an array of 9 x 2
y = np.reshape(d, (9,2)) # reshape function allows you to reshape an array to your desire
y


# In[ ]:




