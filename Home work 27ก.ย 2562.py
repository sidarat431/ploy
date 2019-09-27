#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.แมงมุมตัวหนึ่ง ตกลงไปในบ่อที่มีความสูง H เมตร มันพยายามจะไต่ให้ถึงปากบ่อ ในเวลากลางแมงมุมไต่ขึ้นไปได้ U เมตร เวลากลางคืนมันนอนหลับจึงไม่ได้ไต่แต่กลับไถลลงมาเป็นระยะทาง D เมตร ให้เขียนโปรแกรมเพื่อหาว่าแมงมุมจะใช้เวลากี่วันในการไต่ออกจากบ่อ (กำหนดให้แมงมุมเริ่มไต่ในเวลากลางวัน)
H = int(input("H: "))
U = int(input("U: "))
D = int(input("D: "))
k = 0
day = 1
while True:
    k = k+U
    if k>=H:
     break
    k = k-D
    day = day+1
print(day,"day(s).")


# In[3]:


#2.ให้เขียนโปรแกรมรับจำนวนเต็ม Dและ Tจากนั้นพิมพ์เลขตั้งแต่ 1 ถึง D ที่ Tหารลงตัว 
D = int(input("Enter D: "))
T= int(input("Enter T: "))
for x in range(1,D+1):
    if  x%T == 0:
        print(x)


# In[5]:


#3.ร้านขายผลไม้ร้านหนึ่ง พยายามเพิ่มยอดขายโดยการเสนอโปรโมชั่นพิเศษ ถ้าคุณซื้อผลไม้มากกว่า 5 ชนิด ที่มีมูลค่ารวมเกิน 80 บาท คุณจะได้ส่วนลด 20% 
count = int(input("ต้องการผลไม้: "))
money = int(input("ราคา: "))
if count > 5 and money > 60:
   s = money-money*0.1
else:
   s = money
print("You have to pay",int(s),"bath.")


# In[6]:


#4.ตะพาบตัวหนึ่ง ตกลงมาจากสระน้ำที่มีความสูง H เมตร มันพยายามจะไต่ขึ้นไปที่เดิม ในเวลากลางวันตะพาบไต่ขึ้นไปได้ U เมตร เวลากลางคืนมันหมดแรงจึงไม่ได้ไต่แต่กลับไถลลงมาเป็นระยะทาง D เมตร ให้เขียนโปรแกรมเพื่อหาว่าตะพาบจะใช้เวลากี่วันในการไต่สระขึ้นไปที่เดิม (กำหนดให้ตะพาบเริ่มไต่ในเวลากลางวัน)
H = int(input("H: "))
U = int(input("U: "))
D = int(input("D: "))
k = 0
day = 1
while True:
    k = k+U
    if k>=H:
     break
    k = k-D
    day = day+1
print(day,"day(s).")


# In[8]:


#5.มานะขายกุ้งไป 30 กิโลกรัม ราคากิโลกรัมละ  200บาท เอาเงินที่ขายได้ไปซื้อโดนัทราคาชิ้นละ 15 บาท มานะจะซื้อโดนัทได้กี่ชิ้น กำหนดให้ได้โดนัท 10 ชิ้น
S=int(input("ขายกุ้งไป:"))
D=int(input("ราคาชิ้นละ:"))
Donut=int(input("โดนัทชิ้นละ:"))
money=S*D
count = int(money//Donut)
print("จะได้โดนัทปริมาณ:",count,"ชิ้น")
if count < 1:
    print("ไม่สามารถซื้อได้")
elif count > 12:
    print("เกินจำนวนที่ต้องการ")
else :
   count == 15
   print("ได้ครบตามจำนวน")


# In[10]:


#6.ให้เขียนโปรแกรมรับจำนวนเต็ม P และ K จากนั้นพิมพ์เลขตั้งแต่ 1 ถึง P ที่ K หารลงตัว 
p = int(input("Enter P: "))
k = int(input("Enter K: "))
for x in range(1,p+1):
    if  x%k == 0:
        print(x)


# In[11]:


#7.ร้านขายทุเรียนร้านหนึ่ง พยายามเพิ่มยอดขายโดยการเสนอโปรโมชั่นพิเศษ ถ้าคุณซื้อทุเรียนมากกว่า 5 ลูก ที่มีมูลค่ารวมเกิน 1000 บาท คุณจะได้ส่วนลด 20% 
count = int(input("ต้องการทุเรียน: "))
money = int(input("ราคา: "))
if count > 5 and money > 1000:
   s = money-money*0.1
else:
   s = money
print("You have to pay",int(s),"bath.")


# In[12]:


#8.พลอยมีเงิน 2500 บาทซื้อปลาหมึกไป 10 กิโลกรัม ราคากิโลกรัมละ  150 บาท เอาเงินที่เหลือไปซื้อแตงโมราคาลูกละ 30 บาท พลอยจะซื้อแตงโมได้กี่ลูก กำหนดให้ได้แตงโม 33 ลูก
A=int(input("พลอยมีเงิน:"))
B=int(input("ซื้อปลาหมึกไป:"))
P=int(input("ปลาหมึกกิโลกรัมล่ะ:"))
ปลาหมึก=B*P
W=int(input("แตงโมลูกละ:"))
money=(A-(B*P))
count = int(money//W)
print("จะได้แตงโมปริมาณ:",count,"ลูก")
if count < 1:
    print("ไม่สามารถซื้อได้")
elif count > 50:
    print("เกินจำนวนที่ต้องการ")
else :
    count == 33
    print("ได้ครบตามจำนวน")


# In[13]:


#9.ให้เขียนรับตัวเลขฐาน 2 จากผู้ใช้ จากนั้นแปลงให้เป็นเลขฐานสิบ
x = input("Enter binary number: ")
d = len(x)-1
sum = 0
for y in x:
   if y == '1':
      sum = sum+2**d
   d = d-1
print(sum)


# In[15]:


#10.เขียนโปรแกรมรับจำนวนเต็มบวก 1 จำนวน จากนั้นให้แสดงผลลัพธ์เป็นจำนวนเต็มดังกล่าวที่เขียนอยู่ในรูปของตัวเลขฐาน สอง
x = int(input("Enter number: "))
x0 = x
sum = ''
d = 0
z = 0
while True:
   y = int(x%2)
   x = int(x/2)
   sum = str(y)+sum
   if y==1:
      z = z+2**d
   if z==x0:
      break
   d = d+1
z = int(sum)
print(z)


# In[ ]:





# In[ ]:




