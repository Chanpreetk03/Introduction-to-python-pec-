# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 01:32:18 2022

@author: Lenovo
"""

#Question-1 
#An input string is given
str="Python is a case sensative language"
#part a, find len of input string
print(len(str))
#part b, reverse the string
print(str[::-1])
#part c, store a part of string in a new string
str2=str[10:26]
print(str2)
#part d, replace
str.replace("a case sensative", "object oriented")
#part e, find the index of 'a'
print(str.find('a'))
#part f, remove all spaces
print(str.replace(" ",""))

print("="*100)

#Question-2 take some info and give output in given pattern
name=input("Enter your name:")
sid=int(input("Enter your student id:"))
dept_name=input("Enter your branch:")
cgpa=float(input("Enter your cgpa:"))
print("Hey, {0} Here!\nMy SID is {1}\nI am from {2} and my cgpa is {3}".format(name,sid,dept_name,cgpa))

print("="*100)

#Question-3  For given nos. use biwise operators
#given nos. a=56,b=10
a=56
b=10
#part-a bitwise-and(&)
print(a&b)
#part-b bitwise-or(|)
print(a|b)
#part-c bitwise-xor(^)
print(a^b)
#part-d left shift both a and b by 2 bits
print(a<<2 , b<<2)
#part-e right shift a by 2 bits and b by 4 bits
print(a>>2 , b>>4)

print("="*100)

#Question-4 greatest of 3 nos
n1=float(input("Enter the first number:"))
n2=float(input("Enter the second number:"))
n3=float(input("Enter the third number:"))
if n1>=n2 and n1>=n3:
    print("The first number is largest")

elif n2>=n1 and n2>=n3:
     print("The second number is largest")
     
else:
      print("The third number is largest") 
      
print("="*100)

#Question-5 check if the string "name" is in the string given by user

string=input("Enter the string:")

if string.find("name")!=-1:
    print("Yes")
    
else:
     print("No")    

print("="*100)

#Question-6 check if the given numbers(as integers) can be sides of triangle
s1=input("Enter the first side:")
s2=input("Enter the second side:")
s3=input("Enter the third side:")

if int(s1)+int(s2)<=int(s3) or int(s1)+int(s3)<=int(s2) or int(s3)+int(s2)<=int(s1):
    print("No, the triangle is not possible")
    
else:
     print("Yes, the triangle is possible")    
     
print("="*100)     










