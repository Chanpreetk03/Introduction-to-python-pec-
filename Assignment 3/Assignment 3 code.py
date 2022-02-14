# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:11:51 2022

@author: Lenovo
"""

#Assignment-3
#Ques 1
#take input and if it is a word count all the characters and if it is a sentence all the words
def get_occurences(input_string):
    count_dict={}
    if ' ' in input_string:
        # more than 1 words
        
        for word in input_string.split(' '):
            
            if word in count_dict:
                count_dict[word]+=1
            else:
                count_dict[word]=1
    
    else:
        #1 word
        for char in input_string:
            if char in count_dict:
                count_dict[char]+=1
            else:
                count_dict[char]=1
    
    return(count_dict)

if __name__=='__main__':
    #taking input
    string=input("Enter the string:")
    #using function
    result=get_occurences(string)
    print(result)
    print('*_'*50)

#Ques 2
#function for leap year
def leap(n):
    if n%100==0 :
        if n%400==0:
            return 1
        else :
            return 0
        
    else :
        if n%4==0 :
            return 1
        else :
            return 0
        
#next date using if else        
day=int(input("Enter the day:"))
month=int(input("Enter the month:"))
year=int(input("Enter the year:"))
if month==2:
    if leap(year)==1:
        if day>29:
            print("Invalid date")
        elif day<29:
            day=day+1
        else:
            day=1
            month=month+1
    else:
        if day>28:
             print("Invalid date")
        elif day<28:
             day=day+1
        else:
             day=1
             month=month+1
             
elif month==[1,3,5,7,8,10,12]:
    if day>31:
        print("Invalid date")
    elif day<31:
        day=day+1
    else:
        day=1
        if month==12:
            month=month+1
            year=year+1
        else:
            month=month+1
            
else:
    if day>30:
        print("Invalid date")
    elif day<30:
        day=day+1
        year=year
    else:
        day=1
        month=month+1
        year=year            
print(day, '/', month , '/',year,sep='')        

print('*_'*50)
#Ques 3
#printing tuples as lists asthe number and its square
list1=[5,6,7,8]

output=[]
for i in list1:
    output.append((i, i*i))

print(output)    
print('*_'*50)
#Ques 4
#taking grade pt. and printing grade and its performance
grade_pt=int(input("Enter the grade:"))
grade={4:'D',5:'C',6:'C+',7:'B',8:'B+',9:'A',10:'A+'}
performance={4:'Poor',5:'Below Average',6:'Average',7:'Good',8:'Very Good',9:'Excellent',10:'Outstanding'}
if grade_pt<4 or grade_pt>10:
    print("Error")
else:
    print('Your Grade is',grade[grade_pt],'and',performance[grade_pt],'performance' )  
    
print('*_'*50)
#Ques 5
#printing the given pattern 
n=6
for rows in range(n):
    print(" "*rows,end='')
    for column in range(2*(n-rows)-1):
        temp=65+column
        print(chr(temp),end='')
    print()    
print('*_'*50)
#Ques 6
#making function for taking input
def input_dictionary():
    student_dict={}
    while(True):
        option=input("Enter your option: ")
        if option=='N':
            break
        elif option=='Y':
             
            sid=input("Enter student id: ")
            sname=input("Enter your student name: ")
            student_dict[sid]=sname
             
        else:
            print("wrong option")
    return(student_dict) 
#function for sorting by index 
def sort_dict_on_index(input_dictionary):
    sorted_index_list=input_dictionary.keys()
    sorted_index_list=sorted(sorted_index_list)
    
    sorted_index_dict={}
    
    for index in sorted_index_list:
        sorted_index_dict[index]=input_dictionary[index]
    
    return(sorted_index_dict) 

#function for sorting by value
def sort_dict_values(input_dictionary):
    
    temp={}
    # doing deep copy
    for index in input_dictionary:
        temp[index]=input_dictionary[index]
    
    
    sorted_values_list=input_dictionary.values()
    sorted_values_list=sorted(sorted_values_list)
    
    sorted_values_dict={}
    
    for value in sorted_values_list:
        for index in temp.keys():
            if temp[index]==value:
                sorted_values_dict[index]=value
                temp.pop(index)
                break
            
    return(sorted_values_dict)


if __name__=='__main__':
   #a-part
   student_dictionary=input_dictionary()
   print("a." ,student_dictionary)

   #b-part

   print("b." ,sort_dict_values(student_dictionary))

   #c-part

   print("c." ,sort_dict_on_index(student_dictionary))

   #d-part

   search = input("Please Enter SID Of The Student You Want To Search: " )
   print("d. Student With The Given SID Is: " ,student_dictionary[search])
print('*_'*50)

#Ques 7
#print fibonacci series and its average
#the condition for fibonacci series is n(1)=n(0)+n(-1)
def fibbo(n):
    if n==0 or n==1 :
        return 1
    
    else:
        return fibbo(n-1)+fibbo(n-2)
    
no_term=int(input("Enter the number of terms:")) 
sum=0
if no_term<1:
    print("Incorrect input")
else:
    print("The terms are:")
    for i in range(no_term):
        term=fibbo(i)
        print(term,end=' ')    
        sum=sum+term
    print('\n')    
average=sum/no_term
print("The average is:",average)        
print('*_'*50)


#Ques 8
#for the given list do the functions
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
 # a part

A_Set = (Set1|Set2)-(Set1&Set2)
print("Set of elements in set 1 and 2 but not in both :", A_Set)

 # b part

B_Set = (Set1|Set2|Set3) - ((Set1&Set2)|(Set2&Set3)|(Set3&Set1))
print("Set of elements in only one of the three sets :", B_Set)

 # c part

C_Set= ((Set1&Set2)|(Set1&Set3)|(Set3&Set2))-(Set1&Set2&Set3)
print("Set of elements presents in only two ste ",C_Set)

 # d part

D_Set = set()
for i in range(1, 11):
     if i not in Set1:
         D_Set.add(i)
print("d. ", D_Set)

 # e part

E_Set = set()
for i in range(1, 11):
     if i not in Set1 and i not in Set2 and i not in Set3:
         E_Set.add(i)
print("e. ", E_Set) 
print('*_'*50)  