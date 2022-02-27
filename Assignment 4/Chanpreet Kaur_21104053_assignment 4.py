print('ASSIGNMENT 4')
#Question 1
#Tower of Hanoi
#n(given)==3
print('QUESTION 1\n Tower of hanoi')
def towerOfHanoi(n,source , helper, destination):
    if n>=1:
        towerOfHanoi(n-1,source,destination,helper)
        print('Move the disc from',source,'to', destination)
        towerOfHanoi(n-1,helper,source,destination)
n=3
print("A is source , B is helper , C is destination:")
towerOfHanoi(n,'A','B','C')  

print("="*100)

#Question 2
print("QUESTION 2\n Pascal's triangle")
#Pascal's triangle

x=int(input('Enter the number:'))
#function for factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

#function for nCr
def combination(n1 , r1):
    if n1>=r1:
       numerator=factorial(n1)
       denominator=factorial(r1)*factorial(n1-r1)
       return numerator//denominator        
#function for iterative method
def pascal_loop(n):
    i=1
    while i<n:
        j=0
        space=n-i
        print('  '*space,end='')
        while j<i:
            print(combination(i-1,j),'   ',end='')
            j=j+1
        print('\n')
        i=i+1

 #functions for recursive method
def helper(a,spaces) :
    if a<0:
        return 

    else:
        helper(a-1,spaces)
        j=0
        print(' '*(3*spaces-2*a),end='')
        while j<=a:
            
            print(combination(a,j),'   ',end='')
            j+=1
        print('\n')    



def pascal_recur(n):
    x=n
    helper(n,x)
print('Iterative method')
pascal_loop(x+1)
print('Recursive method')
pascal_recur(x-1)


print('='*100)
#Question 3
print('Question 3\n ')
def check_zero(x):
    if x==0:
        print('The number is zero')
    else:
        print('The number is not zero')


num1=int(input('Enter the first number:'))
num2=int(input('Enter the second number:'))
quo=num1//num2
remainder=num1%num2
#part a
print("part a")
print(callable(quo))
print(callable(remainder))
#part b
print("part b")
print(check_zero(quo))
print(check_zero(remainder))
#part c
print("part c")
list1 = [quo+4 , remainder+4 , quo+5, quo+5, remainder+5, quo+6, remainder+6]

result = []
for i in range(len(list1)):
    if list1[i] > 4:
        result.append(list1[i])
print(f"Filtered out numbers that are greater than 4 are : {result}")

#part d
print("part d")
setresult = set(result)
print("Set:",setresult)
#part e
print("part e")
immutableSet=frozenset(setresult) 
print("Immutable set:",immutableSet)
#part f
print("part f")
print("Hash value of the max value from the above set:", hash(max(immutableSet)))
print("\n")
print('='*100)
#Question 4
print('QUESTION 4\n Creating a student class')
#creating class
class Students:
    def __init__(self,name,roll_num):#creating constructor
        print("Constructor called")
        self.name=name
        self.roll_num=roll_num
        print('Name',self.name,'and SID of the given student is',self.roll_num)
    def __del__(self):#creating destructor
        print("Destructor called")

#creating objects
s1=Students('Chanpreet',21104053)
s2=Students('Sakshi',21104056)
print('='*100)
#Question 5
#creating a class 
print('QUESTION 5\n Performing functions on class of employee')
class Employee:
    def __init__(self,Name,Salary):
        self.name=Name
        self.salary=Salary
        print(self.name,"is paid",self.salary)
#declaring objects
first=Employee('Mehak',40000)
second=Employee('Ashok',50000)
third=Employee('Viren',60000)   
#part a
first.salary=70000

print(first.name,"is paid",first.salary)
print(second.name,"is paid",second.salary)
print(third.name,"is paid",third.salary)
#part b
del third
print('The object is deleted')
print('='*100)  

#Question 6
print('QUESTION 6\n Friendship Tester' )
#taking input lowering all chars and striping the spaces
george=input('Enter the word by George:').lower().strip()
barbie=input('Enter the word by Barbie:').lower().strip()
#making the input a list and sorting them
George=list(george)
Barbie=list(barbie)
George.sort()
Barbie.sort()
#checking if their friendship is true
if George==Barbie:
    print('Their friendship is true.')
else:
    print('Their friendship is not true.') 

print('='*50,'END OF ASSIGNMENT','='*50)       




















