#!/usr/bin/env python
# coding: utf-8

# ASSIGNMENT DAY N0 5

# In[11]:


def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(a)
    return(x)

print(move_zero([0,2,3,4,6,7,10]))
print(move_zero([10,0,11,0,15,0,43,0]))
 


# MERGE THE TWO LIST

# In[13]:


test_list1=[1,5,6,9,11]
test_list2=[3,4,7,8,10]
print("the original list1 is"+str(test_list1))
print("the original list2 is"+str(test_list2))


size_1 = len(test_list1) 

size_2 = len(test_list2) 


res = [] 

i, j = 0, 0

 

while i < size_1 and j < size_2: 

    if test_list1[i] < test_list2[j]: 

      res.append(test_list1[i]) 

      i += 1

  
    else: 

      res.append(test_list2[j]) 

      j += 1

  
res = res + test_list1[i:] + test_list2[j:] 


print ("The combined sorted list is : " + str(res)) 


# In[ ]:




