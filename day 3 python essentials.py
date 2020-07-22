#!/usr/bin/env python
# coding: utf-8

# ASSIGNMENT SUM OF ADD N NUMBERS USING WHILE LOOP
# 

# In[4]:


num=15
sum=0
while(num>0):
    sum=sum+num
    num=num-1
    print("the sum is",sum)


# prime numbers in python
# 

# In[78]:


number=int(input("enter num:"))
if number > 1:
      for i in range(2, number):
        if (number % i) ==0:
                print(number,"is not prime")
                break  
        else:
                print(number,"is prime")
else:
                    print(number,"is not prime")

