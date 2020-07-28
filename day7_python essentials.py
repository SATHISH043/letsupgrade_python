# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Q:1
port1={21:"ftp",22:"ssh",23:"telnet",80:"http"}
inv_port = dict([(value,key) for key,value in port1.items()])
print(inv_port)

#Q:2
tuple1= [(1,2),(3,4),(5,6)]
newlist=[]

for i in tuple1:
    sum=0
    for j in i:
        sum+=j
    newlist.append(sum)
print(newlist)
        
        
#Q3

list1= [(1,2,3),[1,2],['a','hit','less']]
lis =[]
for i in list1:
    for j in i:
        lis.append(j)
list=lis
print(list)
