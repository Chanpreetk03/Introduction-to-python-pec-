# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Assignment-1
#Question-1(average of three numbers)
print('enter three numbers')
#num1 , num2 , num3=number1 , number 2 , number3 

num1=float(input())
num2=float(input())
num3=float(input())
#avg=average
avg=(num1+num2+num3)/3
print('the average of given numbers is', avg)
print('-'*100)


#Question-2(To calculate person's income tax)
#tax_rate , sta_deduct , dependent_deduct are given in question

tax_rate=(20/100)
sta_deduct=10000
dependedant_deduct=3000
#gross_inc , no_ofdepend are to be taken by user

gross_inc=float(input('The gross income is $'))
no_ofdepend=int(input('Number of dependents are-'))

tax_inc=gross_inc-sta_deduct-(no_ofdepend*sta_deduct)

tax=tax_inc*tax_rate
#output
print('The tax to be paid is $', tax)

print('-'*100)


#Question-3(Make list by taking input for SID, Name, Gender, Course name and cgpa)
sid=int(input('Enter your SID:'))
name=input('Enter your name:')
gender=(input('Enter your gender (F for female, M for male or U): '))
course_name=input('Enter the course name:')
cgpa=float(input('Enter your cgpa:'))
#making list
List = [sid, name, gender, course_name, cgpa] 
#output
print(List)
print('-'*100)


#Question-4(To enter marks of 5 students into a list and display them in sorted manner.)
#Input for numbers
print('Enter the marks:')
n1=float(input())
n2=float(input())
n3=float(input())
n4=float(input())
n5=float(input())
#making list

Marks =[n1, n2, n3, n4, n5]
Marks.sort()
print(Marks)
print('-'*100)



#Question-5(a)(remove the 4th element from given list)
Given_lista=['Red' ,'Green' ,'White','Black', 'Pink', 'Yellow']
#index of 4th element is 3
del Given_lista[3]
#output
print("color", Given_lista)


Given_listb=['Red' ,'Green' ,'White','Black', 'Pink', 'Yellow']

Given_listb[3:5]=['Purple']
print(Given_listb)













    
    