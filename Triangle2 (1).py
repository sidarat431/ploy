#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#นางสาวสิดารัศมิ์   ทั่งทอง 362515241015  EE36241N
import math
a = float(input("Fill Out a :"))
b = float(input("Fill Out b :"))
D = float(input("Fill Out D :"))
C = D*math.pi/180
c = math.sqrt((a*a)+(b*b)-(2*a*b*math.cos(C)))
print("c =", c, "cm.")

