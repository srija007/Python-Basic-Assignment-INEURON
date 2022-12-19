#!/usr/bin/env python
# coding: utf-8
1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
# In[6]:


def recur_fibonacci(n):
    if n<=1:
        return n
    else:
        return recur_fibonacci(n-1) +recur_fibonacci(n-2)
    
nterms = int(input("Enter the nth terms for the series: ")) 
for i in range(nterms):
    print(recur_fibonacci(i))
   
        

2. Write a Python Program to Find Factorial of Number Using Recursion?
# In[21]:


def fact_num(n):
    if n ==1:
        return n
    else:
        return n* fact_num(n-1)
    
    
num  =  int(input("Enter the number: "))    
if num<=1:
    print("The factorial is 1")
else:
    print(f"The factorial of the given number is {fact_num(num)}")
    

3. Write a Python Program to calculate your Body Mass Index?
# In[25]:


weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in cm: "))

#converting the height in meter:
height_meter = height * 0.01
# calculating BMI
BMI = weight / height_meter **2
print("Your body mass index is: ", round(BMI, 2))
if BMI <= 18.5:  
    print("Oops! You are underweight.")  
elif BMI <= 24.9:  
    print("Awesome! You are healthy.")  
elif BMI <= 29.9:  
    print("You are overweight.")  
else:  
    print("Seesh! You are obese.")  

4. Write a Python Program to calculate the natural logarithm of any number?
# In[27]:


import math
num =int(input("Enter the number: "))
result = math.log(num)
print(f"The log value of the given number is {result}")

5. Write a Python Program for cube sum of first n natural numbers?
# In[31]:


n = int(input("Enter the number: "))
Sum = 0
for i in range (1,n+1):
    i = i**3
    Sum = Sum +i
   
print(f"The cube sum for given natural numbers are : {Sum}")    
    
    


# In[ ]:




