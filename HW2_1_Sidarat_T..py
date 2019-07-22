#!/usr/bin/env python
# coding: utf-8

# In[1]:


#นางสาว สิดารัศมิ์    ทั่งทอง 362515241015 EE36241N
S=input("Username :")
T=input("Password :")
if S=="ploy" and T=="1212":
    print("Welcome to sidarrat Shop.")
else :
    print("Error ,please try again.")
C=30
W=10
G=25
M=20
A=40
print("-------------------Menu-------------------")
print("Welcome to Kawin Shop")
print("1.Coffee   30 THB")
print("2. Water    10 THB")
print("3. Green tea 25 THB")
print("4. Milk       20 THB")
print("5. Apple juice 40 THB")
Sidarat=int(input("What do you want?(1-5) : "))
num=int(input("How many do you want? : "))
if Sidarat==1:
    print("You order ",num," of Coffee  ",C*num, " THB")
elif Sidarat==2:
    print("You order ",num," of Water   ",W*num, " THB")
elif Sidarat==3:
    print("You order ",num," of  Green tea ",G*num, " THB")
elif Sidarat==4:
    print("You order ",num," of Milk ",M*num, " THB")
elif Sidarat==5:
    print("You order ",num," of Apple juice ",A*num, " THB")


# In[ ]:




