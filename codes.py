pwd = power writen directory
cd = change directory:Directory is a collection of files

name = 'Poovaragavan'
print(name)

name = input('tell me your name')
print('my name is", name)
	 
tamil = 90
english = 85
maths = 90

#print(tamil + english + maths)

total = tamil + english + maths

print(total)
print(total//3) #floor division:shows only the integer value of the quotient not
	  the floating-point values
print(total/3) #normal division:shows the quotient with floating-point values
	  

age = 13
if age>=18:
	print("eligible")
else:
	print("not eligible")

import keyword 
	# Python modules can get access to code from another module by importing the file/function using import.
print(keyword.kwlist)

a = 10
b = 20
c = a<b
print(c)
print(type(c))


name = "ragavan"
adress = '''Ragavan's native is namakkal'''
print(adress)
	  
s = 'abcdefghijklmnopqrstuvwxyz' 
print(s)
print(s[0]) #index
print(s[1])
print(s[-1]) #negative index
print(s[-2])
	  
name = "Ragav"
print(name[0])
print(name[-1])
print(len(name))	  
	  
doorNo = 23
street = "k.k.Nagar"
print(str(doorNo) + street) #type casting
	  
	  Gas_price = 103.05
print(int(Gas_price))
	  
result = 0
print(bool(result))

result = 1
print(bool(result))
	  
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#print(s[-3:-15:-2]) # XVTRPN
#print(s[3:15:2]) # DFHJLN
#print(s[3:15:3]) # DGJM
print(s[3:15:4]) # DHL

#step operator
#print(s[-1:-5:-1]) #ZYXW
print(s[-5:-1:-1]) #ZYXW

#print(s[-1:-5]) #blank
#print(s[-5:-1])  #vwxy

#print(s[-1]) #z
#print(s[2:-1]) # c toy
#print(s[2:-2])  # c to X


#print(s[0:4]) #ABCD
#print(s[2:6]) #cdef
#print(s[:4])
#print(s[24:])  

# Uppercase:
name = 'ragav'
print(name.upper()) # o/p: RAGAV

# Lowercase:
name = 'RAGAV'
print(name.lower()) #o/p: ragav

name = 'ragavjordan'
length = len(name)
print(length) # o/p: 11
print(type(length)) # o/p: <class 'int'>
print(type(name)) # o/p: <class 'str'> 
print(name[length-1]) # o/p: n
print(name[0] + name[length-1].upper() + name[-1]) # o/p: rNn
print(name[0].upper() + name[1:])  # o/p: Ragavjordan
print(name[0].upper() + name[1:-1] + name[-1].upper()) # o/p: RagavjordaN
print(name[0].upper() + name[1:5] + name[5:6].upper() + name[6:11]) + name[10:].upper()) # RagavJordaN
print(name[int(length/2)].upper()) # o/p: J

name1 = 'ragavjordan'
name2 = 'vengateswaran'
print(name1 == name2) # False
print(name1 != name2) # True
print(name1>name2) # False
print(name1<name2) # True

name1 = 'ragavjordan'
name2 = 'Ragavjordan'
print(name1 == name2) # False
print(name1 != name2) # True
print(name1>name2) # True
print(name1<name2) # False
	  
age1 = 10
age2 = 12
age3 = 14
print(age1<age2<age3) # o/p: True
print(10==20==30) #o/p: False

name1 = 'ragavjordan'
name2 = 'Ragavjordan'
print(name1 == name2)
print('r'>'R')

print('I'm good')
print('I\'m good')
	  
	  
	  
file = "c:\programfiles\\'new.txt"
print(file) 
	  
	  
print(10//5) # o/p: 2
print(2**3) # o/p: 8
print(3**2) # o/p: 9
	  
mark = 65
mark = mark + 5
mark+=5
mark%=5
mark-=5 # 60
mark*=5 #
mark**=5 #
mark\\=5 #
	  
friday = True
Thursday = not friday
print(Thursday) #False

no1 = 10 
no2 = 70
print(no1==no2) # True
print(no1 and no2) #70
print(no1 or no2) #10


no1 = 0
no2 = 0.0
print(no1 and no2)
print(no1 or no2)

no1 = 0.0
no2 = 0
print(no1 and no2)
print(no1 or no2)

thursday = False
sleep = 0
print(thursday and sleep) # False
print(thursday or sleep) # 0

name = ''
know = 0
print(name and know) # blank
print(name or know) # 0

# identity operator
today = 'friday'
tomorrow = 'saturday'
print(today is tomorrow) # False
print(today is not tomorrow) #True
print(today == tomorrow) # False
print(today != tomorrow) # True

#Immutability : Memory will not be edited instead new memory will be created


#Mutabile
l1 =[90,87,65,56,78]
l2 = [90,87,65,56,78]
print(l1 == l2) # True because == declare the value of the elements
print(l1 is l2) # False because is declare the address of the refferance variable

# Membership Operators:
name = 'Ragavjordan namakkal'
print('namakkal' in name) # True
print('chennai' in name) # False
print('namakkal' not in name) #False
print('chennai' not in name) #True


print(8<<1)

# Ternary perator
no1, no2 = 15,11
result = no1 if no1>no2 else no2
print(result)

#
import math
print(math.pow(2,3)) # 8
print(math.factorial(5)) #120
print(math.ceil(8.2))# 9 - ceil means greator round off
print(math.ceil(8.8)) #9
print(math.floor(8.2)) #8 - floor means smaller round off
print(math.floor(8.8))# 8
print(math.floor(8.5))#8
print(math.ceil(8.5)) #9
print(math.pi) #3.141592653589793

# sys module - command line arguments
import sys
print(sys.argv) # argv - arguments passed in command line
print(sys.argv[0])

#http://www.kaniyam.com/python-sys-module-tamil/
 
print("hi"+ "Hello")
print("hi", "Hello")
no1, no2, no3 = 100,200,300
print(no1, no2, no3, sep =':') # separator
print(no1, no2, no3, end = ':') # end

print("no1 is %i" %no1) # %i - used instead for commas (,)
print("no1 is %d and no2 is %d"%(no1,no2)) # represents the values on the %

# Replacement Operator
# {} --> Place Holder

name = "ragavjordan"
city = "namakkal"
print("Hi {0} Welcome from {1}".format(name,city))
print("Hi {a} Welcome from {b}".format(a=name,b=city))

num1 = 100
num2 = 50
sum = num1 + num2
print("The sum of {0} and {1} is {2}".format(num1,num2,sum))

Output:
	The sum of 100 and 50 is 150
	  
# Control Flow Statements

print("Enter Mark")
mark = int(input())
mark1 = int(input())
#mark = 51
if mark>=60 and mark1>=60:
	print("First Class") 
elif mark>=50 and mark1>=50:
	print("Second Class")
elif mark>=35 and mark>=35:
	print("Pass")
else:
	print("Reappear")
	  
---> 3 marks = highest,lowest
----> # 1 - 1000% 3 & 5
	# 1 - 1000% 3 , 5 & 7	  
	  
no = 1
while no<=10:
	if no%3 == 0:
		print("Divisible by 3")
	else:
		print("not divisible by 3")
	no+=1 #no=no+1
	
no = 1
count = 0
while no<=10:
	if no%3 == 0:
		print("Divisible by 3")
		count+=1
	else:
		print("not divisible by 3")
	no+=1 #no=no+1
else:
	print("count :", count)a	  
	  
no = 1
count = 0
while n<=1000:
	if no%3
	  
	 	  
# Using 3 inputs finding the highest and lowest marks: 
Mark1 = int(input('Enter First Mark : '))
Mark2 = int(input('Enter Second Mark : '))
Mark3 = int(input('Enter Third Mark : '))
def Highest(Mark1, Mark2, Mark3):
    if (Mark1 > Mark2) and (Mark1 > Mark3):
        Highest_mark = Mark1
    elif (Mark2 > Mark1) and (Mark2 > Mark3):
        Highest_mark = Mark2
	  
    else:
        Highest_mark = Mark3
    print("The Highest Mark : ", Highest_mark)
	
def Lowest(Mark1, Mark2, Mark3):
    if (Mark1 < Mark2) and (Mark1 < Mark3):
        Highest_mark = Mark1
    elif (Mark2 < Mark1) and (Mark2 < Mark3):
        Lowest_mark = Mark2
    else:
        Lowest_mark = Mark3
    print("The Lowest Mark : ", Lowest_mark)
Highest(Mark1, Mark2, Mark3)
Lowest(Mark1, Mark2, Mark3)

	  Mark1 = int(input('Enter First Mark : '))
Mark2 = int(input('Enter Second Mark : '))
Mark3 = int(input('Enter Third Mark : '))
def Highest(Mark1, Mark2, Mark3):
    if (Mark1 > Mark2) and (Mark1 > Mark3):
        Highest_mark = Mark1
    elif (Mark2 > Mark1) and (Mark2 > Mark3):
        Highest_mark = Mark2
    else:
        Highest_mark = Mark3
    print("The Highest Mark : ", Highest_mark)
	
def Lowest(Mark1, Mark2, Mark3):
    if (Mark1 < Mark2) and (Mark1 < Mark3):
        Highest_mark = Mark1
    elif (Mark2 < Mark1) and (Mark2 < Mark3):
        Lowest_mark = Mark2
    else:
        Lowest_mark = Mark3
    print("The Lowest Mark : ", Lowest_mark)
Highest(Mark1, Mark2, Mark3)
Lowest(Mark1, Mark2, Mark3)
	  
	  
	  
	  
last = 5
while last > 0:
    if last==3:
        break
    print(last)
    last = last-1
else:
     print("Hello") 
	  
last = 5
while last > 0:
    if last==3:
        last-=1
        continue
    print(last)
    last = last-1
else:
     print("Hello")  
	  
	  
no = 1
total = 0
while no<=100:
    total = total + no
    no+=2    
else:
    print(total)
	  
no = 1
total = 0
while no<=5:
    total = total + no
    no+=1   
else:
    print(total)
	
no = 1
total = 1
while no<=5:
    total = total * no
    no+=2   
else:
    print(total)
	  
name = input("Enter your name:")
length = len(name)
i=0
while i<length:
    print(name[i])
    i+=2
	  
name = input("Enter your name:")
length = len(name)
i=1
while i<length:
    print(name[i])
    i+=2
	  
name = input("Enter your name:")
length = len(name)
i=0
count = 0
while i<length:
    if name[i] == 'a':
        print(name[i])
        count+=1
    i+=1
else:
    print(count)
	  
name = input("Enter your name:")
length = len(name)
i=0
count = 0
while i<length:
    if name[i] == 'a' or name[i] == 'e' or name[i] == 'i'or name[i] == 'o' or name[i] == 'u':
        print(name[i])
        count+=1
    i+=1
else:
    print(count)
	  
name = input("Enter your name:")
length = len(name)
i=0
count = 0
while i<length:
    if name[i] in ['a','e','i','o','u']:
        print(name[i])
        count+=1
    i+=1
else:
    print(count)
	  
no = 100
no2 = 1
while no2<=no:
    if no%no2 == 0:
        print(no2)
    no2+=1
	  
	  
no = 100
no1 = 120
big = no if no>no1 else no1
no2 = 1
while no2<=big:
    if no%no2 == 0 or no1%no2 == 0:
        print(no2)
    no2+=1
	  
# Greast common division of two numbers
no = 100
no1 = 120
big = no if no>no1 else no1
last = 0
no2 = 1
while no2<=big:
    if no%no2 == 0 or no1%no2 == 0:
        last = no2    
    no2+=1
else:
    print(last) # o/p: 120
    
    # least common division
	# Armstrong Number
	  
no = 17
div = 1
while div<no:
    if no%div==0:
        print(div)
    div+=1
    
no = 17
div = 2
last = 0
while div<no:
    if no%div==0:
        last = div 
    div+=1
else:
    print(last)
    
no = 17
div = 2
last = 0
while div<no:
    if no%div==0:
        last = div 
    div+=1
else:
    if last ==0:
        print("Prime Number")
    else:
        print("Not Prime Numbers")
	  
#count of digits:
no = int(input("Enter no"))
count = 0
while no>0:
    no = no//10
    count+=1
else:
    print(count)
	 
#count of digits and addition of digits:
total = 0
no = int(input("Enter no"))
count = 0
while no>0:
    rem = no%10
    total = total + rem
    no = no//10
    count+=1
else:
    print(count)
    print(total)
	  
total = 0
no = int(input("Enter no"))
count = 0
while no>0:
    rem = no%10
    total = (total*10) + rem #*10 = for taking reverse action
    no = no//10
    count+=1
else:
    print(count)
    print(total)
	  
# Reverse number 
total = 0
no = int(input("Enter no"))
no2 = no
count = 0
while no>0:
    rem = no%10
    total = (total*10) + rem #*10 = for taking reverse action
    no = no//10
    count+=1
else:
    if total == no2:
        print("Palindrome")
    else:    
        print("Not Palindrome")
	  
	  
# Least Common Multiple - LCM
def lcm(a,b):
    if a>b:
        greater = a
    else:
        greater = b
    while(True):
        if greater%a == 0 and greater%b == 0:
            lcm = greater
            break
        greater+=1
    return lcm

no1 = int(input("Enter first number"))
no2 = int(input("Enter second number"))

print("The LCM of", no1, "and", no2, "is", lcm(no1,no2))

Output:
Enter first number4
Enter second number8
The LCM of 4 and 8 is 8

	  
# LCM
no1 = 18
no2 = 50
big = no1 if no1>no2 else no2
while True: 
	if big%no1 ==0 and big%no2 ==0:
		print(big, "is LCM")
		break
	big+=1 

	  #Fibanocci series
f = -1
s = 1
count = 6
while count>0:
    t = f+s
    print(t)
    f = s
    s = t
    count-=1
	  
#Fibonacci series without using 3rd variable:

Number = int(input("Enter the number:"))

n1 = 0
n2 = 1

if Number == 0:
    print(Number)
else:
    for num in range(0,Number):
        if num == 1:
            N = num
        else:
            N = n1 + n2
            n1 = n2
            n2 = N
            
            print(N)
	  
	  
no =6
binary = ''
while no>0:
    val = no%2
    binary = str(val) + binary
    no = no//2
else:
    print(binary)

name = 'Ragavjordan'
for letter in name:
    print(letter)
    
for no in range(3):
    print(no)
    
for no in range(1,5):
    print(no)
    
for x in range(1,22,3):
    print(x)
    
for y in range(20,0,-3):
    print(y)
	  
# Addition of Firt N Numbers
total = 0
for no in range(1,11):
    total = total + no
    #print(no)
else:
    print(total)
    
# Factorial
total = 1
for no in range(1,11):
    total = total * no
    #print(no)
else:
    print(total)
    
# no of words in sentence
sent = "Today is Friday"
count = 0
for letter in sent:
    if letter == ' ':
        count+=1
else:
    print("no of words are",(count+1))
	  
	  
# no of sentence in paragraph
sent = "Today is Friday. Tomorrow is Saturday."
count = 0
for letter in sent:
    if letter == '.':
        count+=1
else:
    print("no of sentences are",(count))

	  
	  for no in [0,1,2]:
    print("Hello")
    
	  
result = 1
number = 5
for i in range(1,number+1):
    result = result * i
print(result)

mailid = input("Enter your mail id")

alphabets = 0
digits = 0
special = 0

for i in range(len(mailid)):
    print(mailid[i])
	  
mailid = input("Enter your mail id")

alphabets = 0
digits = 0
special = 0

for i in range(len(mailid)):
    if mailid[i].isalpha():
        alphabets = alphabets + 1
    elif mailid[i].isdigit():
        digits = digits + 1
    else:
        special = special + 1
else:
    print(alphabets)
    print(digits)
    print(special)

for col in range(5):
    print(col, end = ' ')
print()
for col in range(5):
    print(col, end = ' ')
print()
for col in range(5):
    print(col, end = ' ')
print()
for col in range(5):
    print(col, end = ' ')
	  
for row in range(10):
    for col in range(5):
        print(col, end = ' ')
    print()
	  

for col in range(1):
    print(col, end = ' ')
print()
for col in range(2):
    print(col, end = ' ')
print()
for col in range(3):
    print(col, end = ' ')
print()
for col in range(4):
    print(col, end = ' ')
print()
for col in range(5):
    print(col, end = ' ')
print()
	  
for col in range(1,2):
    print(col, end = ' ')
print()
for col in range(1,3):
    print(col, end = ' ')
print()
for col in range(1,4):
    print(col, end = ' ')
print()
for col in range(1,5):
    print(col, end = ' ')
print()
for col in range(1,6):
    print(col, end = ' ')
print()
	  
	  
no = 2
while no<=6:
    for col in range(1,no):
        print(col, end = ' ')
    print()
    no = no+1
    
for no in range(2,6):
      for col in range(1,no):
        print(col, end = ' ')
    print()
    no = no+1
	  
for col in range(5,4,-1):
    print(col, end = ' ')
print()
for col in range(5,3,-1):
    print(col, end = ' ')
print()
for col in range(5,2,-1):
    print(col, end = ' ')
print()
for col in range(5,1,-1):
    print(col, end = ' ')
print()
for col in range(5,0,-1):
    print(col, end = ' ')
print()
	  
no = 1
for row in range(2,6):
	for star in range(1,row):
		print(no*row-1, end = ' ')
		no+=1
	print() 
	  
for row in range(5,0,-1):
    for star in range(1,row):
        print(" ", end = ' ')
    for number in range(5,row-1,-1):
        print(number, end = ' ')
    print()
	  
for row in range(1, 6):
    for star in range(5, row, -1):
        print(" ", end="")
    for number in range(1, row+1):
        print(number, end=" ")
    print()
	  
	  
for i in range(1, 6):
    for j in range(0, i):
        print(i, end="")
    print()
	  
row = 0
while row<=4:
    for col in range(5,row,-1):
        print(col, end = ' ')
    print()     
    row+=1 
	  
for row in range(0,5):
    for col in range(5,row,-1):
        print(col, end = ' ')
    print()
	  
	  
for row in range(1,2):
    print(row, end = " ")
print()
for row in range(1,3):
    print(row, end = " ")
print()
for row in range(1,4):
    print(row, end = " ")
print()
for row in range(1,5):
    print(row, end = " ")
print()
for row in range(1,6):
    print(row, end = " ")
print()   

for row in range(2,7):
    for col in range(1,row):
        print(col, end = " ")
    print() 
	  
	  for i in range(B, G):
    for j in range(A, i):
        print(j, end="")
    print()
	  
#The original array
arr = [11, 22, 33, 44, 55]
print("Array is :",arr)
 
res = arr[::-1] #reversing using list slicing
print("Resultant new reversed array:",res)

for row in range(1,6):
    for col in range(65, 65+row):
        i = chr(col)
        print(i, end = " ")
    print()
	  
	  
for count in range(0,8):
    for row in range(7,count,-1):
    	print("*", end = ' ')
	print("#", end = ' ')
    for num in range(count,-1-1):
         print(num, end = ' ')
    for num1 in range(1,count+1):
         print(num1, end = ' ')
    print()
        
for i in range(0,8):
    for k in range(7,i,-1):
        print(" ",end=' ')
    for j in range(i,-1,-1):
        if(i!=j):
            print(j,end=' ')
        else:
            print('#',end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
	  
	  
for i in range(0,8):
    for k in range(7,i,-1):
        print(" ",end=' ')
    for j in range(i,-1,-1):
        if(i!=j):
            print(j,end=' ')
        else:
            print('#',end=' ')
    for j in range(1,i+1):
        if(i!=j):
            print(j,end=' ')
        else:
            print('#',end=' ')
    print() 
	  
	  
for count in range(0,8):
    for row in range(7,count,-1):
    	print("*", end = ' ')
	print("#", end = ' ')
    for num in range(count,-1-1):
         print(num, end = ' ')
    for num in range(1,count+1):
         print(num, end = ' ')
    print()
	  
	  
for i in range(1,4):
    print("  "*(3-i), end = ' ')
    for j in range(2*i-1,0,-1):
        print(j,end = ' ')
    print()
	  
#               A
#			A	B	C
#		A	B	C	D	E
#	A	B	C	D	E	F	G
#A	B	C	D	E	F	G	H	I

#               0
#			1	0	1
#		2	1	0	1	2
#	3	2	1	0	1	2	3	
#4	3	2	1	0	1	2	3	4 
	  
for count2 in range(0,8):
    for space in range(7,count2,-1):  
        print(" ", end = ' ')
    for num in range(count2,-1,-1):
        print(num, end = " ")
    for num in range(1,count2+1):
        print(num, end = ' ')
    print()
	  
	  
for count2 in range(0,8):
	for space in range(7, count2,-1):
		print(" ",end = ' ')
	print(" ", end = ' ')
	for num in range(count2,-1,-1):
		print(num, end = ' ')	
	for num in range(1,count2):
		print(num, end = ' ')
	print("#", end =' ')
	print()
	  
	  
#for row in range (7,-1,-1):
#    for star in range(row):
 #      print(" ", end = ' ')
        
for count2 in range(0,8):
    for space in range(7,count2,-1):  
        print(" ", end = ' ')
    print("#", end = ' ')
    for num in range(count2,-1,-1):
        print(num, end = " ")
    for num in range(1,count2+1):
        print(num, end = ' ')
    print("#", end = " ")
    print()
	  
for i in range(0,8):
    for k in range(7,i,-1):
        print(" ",end=' ')
    for j in range(i,-1,-1):
        if(i!=j):
            print(' ',end=' ')
        else:
            print('#',end=' ')
    for j in range(1,i+1):
        if(i!=j):
            print(' ',end=' ')
        else:
            print('#',end=' ')
    print() 
	  
	  
print("hi" *3)
	  
	  
for i in range(5):
    print(i * "*", end = ' ')
    for num in range(5):
        print(num, end = ' ')
    print()
    
for i in range(6):
    print(i * "*", end = '')
    for num in range(6-i):
        print(1, end = ' ')
    print()
    
for i in range(7):
    print(i * "*", end = '')
    for num in range(6-i):
        print(1, end = '')
    for star in range(6):
        print("*",end = ' ')
    print()
	  
	  # code 1 & code2 are " W " Patterns
# code 1:  
for i in range(7):
    print(i * "*", end = '')
    for num in range(6-i):
        print(" ", end = ' ')
    print(i * "*",end = '')
    print(i * "*", end = '')
    for num in range(6-i):
        print(" ", end = ' ')
    print(i * "*",end = ' ')
    print()
  
# code 2:
for i in range(7):
    for count in range(2):
        print(i * "*", end = '')
        for num in range(6-i):
            print(" ", end = ' ')
        print(i * "*",end = '')
    print()
	  
for star in range(7,-1,-1):
    for count in range(2):
        print(star * "*", end = '')
        for num in range(star-1,6):
            print(' ', end =' ')
        print(star * "*", end = '')
    print()
	  
no = int(input("Enter count: "))
for row in range(1,no+1):
    for star in range(1,no+1):
        print(star, end = ' ')
    print()
	  
no = int(input("Enter count: "))
for row in range(no,0,-1):
    for star in range(no,0,-1):
        print(star, end = ' ')
    print()
	  
for row in range(5):
    for j in range(5):
        print((chr(j+97)), end = '')
    print()
  # A = 65 a = 97  
	  
no = int(input("Enter count: "))
for i in range(1,no+1):
    print("_"*(no-i),"* " * i, end = '')
    print()
	  
no = int(input(" Enter count: "))
for row in range(1, no+1):
    print(" " *(no-row), "* " * row, end = ' ')
    print()
	  
no = int(input(" Enter count: "))
for row in range(1, no+1):
    print(" " *(row-1), "* " *(no+1-row), end = ' ')
    print()
	  
no = int(input(" Enter count: "))
for row in range(1, no+1):
    print(" " *(row-1), str(row) *(no+1-row), end = ' ')
    print()  
    
for star in range(7):
  print("* ", end = ' ')
print()
for row in range(7):
  for star in range(7):
    if star==0 or star==6:
      print("* ", end = ' ')
    else:
      print("  ", end = ' ')
  print()
for star in range(7):
  print("* ", end = ' ')
print()
    # output:
    
   # 1 1 1 1 1
   #   2 2 2 2
   #     3 3 3
   #       4 4
   #         5

for star in range(7-1):
  print("* ", end = ' ')  
print()
for row in range(7):
  for star in range(7):
    if star==0 or star==6:
      print("* ", end = ' ')
    else:
      print("  ", end = ' ')
  print()
for star in range(7-1):
  print("* ", end = ' ')
print()
for row in range(7):
  for star in range(7):
    if star==0 or star==6:
      print("* ", end = ' ')
    else:
      print("  ", end = ' ')
  print()
for star in range(7-1):
  print("* ", end = ' ')
print()
	  
	# List
ll = []

print(ll)
print(type(ll))

ll = [10,20,5.3,True, "Ragav"]
print(ll)
	  
name = 'ragavjordan'
l = list(name)
print(l)
	  
sen = 'my laptop is dell'
l = sen.split()
print(l)

sen = '02022022'
l = sen.split('2')
print(l)
	  
sen = '02/02/2022'
l = sen.split('/') # string - split
print(l)

print(l[0])
print(l[1])
print(l[2])
print(l[3]) # outoff range
	  
sen = '02/02/2022'
l = sen.split('/') # string - split
print(l)

print(l[-1])
print(l[-2])
print(l[-3])
	  
l = [10,20,30,15,25,35]

print(l)
print(l[:])
print(l[2:5])
print(l[::2])
print(l[2:6:2])
print(l[5:2:-1])
print(l[5:1:-2])
	  
# list is mutable(it can change)

l=[10,20,30,40]
print(l)
l[1] = 22
print(l)

# list traversing

l =[10,20,30,40,4,7,11]

i=0
while i<len(l):
  print(l[i])
  i+=1
  
for no in l:
  print(no)
  
for no in range(len(l)):
  print(no)
  
for no in range(len(l)):
  print(l[no]
       
		
# 1. Even position 2.odd position 3.even number 4.odd number 5. divide by 10

l =[10,20,30,40,4,7,11]
		
#even position
i = 0 
while i < len(l):
    if i%2!=0:
        print(l[i])
    i+=1
		
# odd position: 
i = 0 
while i < len(l):
    if i%2==0:
        print(l[i])
    i+=1

# Even Numbers
for no in l:
    if no%2==0:
        print(no)
        
# Odd Numbers
for no in l:
    if no%2==1:
        print(no)
    
# Divided By 10
for no in l:
    if no%10==0:
        print(no)
		
l1 =[10,20,30,40,4,7,11] 
l2 = [300,500,123]

l = l1+l2
print(l)
print(type(l))
print(len(l))

print(l2*2)
		
for row in range(7):
  for star in range(7):
    if star==0 or star==row-0: 
      print("*", end = ' ')
    else:
      print(" ", end = ' ')
  print()
		
		
l1 = ['a','b','c']
l2 = [10,20,30]

add = [l1, l2]

print(add) # [['a', 'b', 'c'], [10, 20, 30]]
print(len(add)) # 2
print(add[0])  #  ['a','b','c']
print(add[1])# [10,20,30]

print(add[0][0])
print(add[0][1])
print(add[0][2])

print(add[1][0])
print(add[1][1])
print(add[1][2])

for i in add:
    print(i)
    print(len(i))
    print(type(i))

for ll in add:
    for i in ll:
        print(i, end = ' ')
        print(type(i))
		
for ll in add:
    for i in ll:
        if type(i) == str:
            print(i, end = ' ')		
		
l1 = ['a','b','c']
l2 = [10,20,30]

add = [l1, l2]


for i in range(len(add)): #0 1
    for j in range(len(add[i])): # 0 1 2
        if i==1 and j==2:
            add[i][j] = "Hello"
print(add)		
		
		# Function using list
l = [10,20,30,40,50,10,20,30]

print(len(l))

print(l.count(10))
print(l.count(40))
    
print(l.index(10)) # index means position 1st identifier
l.append(100) # add at the end 
print(l)
      
l.insert(2,222) # add at he middle wherever
print(l)		
	
l1 = [10,20,30,40,50,10,20,30]

l2 = [15,25,35]

l1.remove(40)
print(l1)
print(l1.pop()) # display only the last
print(l1)
		
l1.extend(l2) # extends both lists
print(l1)

l2.extend("Ragav")
print(l2)
		
l1 = [10,20,30,40,50,10,20,30]

print(l1)
print(l1.pop())
print(l1)
print(l1.pop(0))
print(l1)
		
l = [10,20,30,40,50]

l.reverse() # print reverse order
print(l)

l.sort() # print ascending order

print(l)
print(min(l)) # print minimum
print(max(l)) # print maximum
print(sum(l)) # print total		
		
l.sort(reverse=True) # desending order
print(l)

l.reverse()
print(sorted(l))
		
l = [10,5,8]

l.sort() 
print(l)

l2 = [10,5,8]
print(sorted(l2)) # only result will be like sort
print(l2)		
		
# list aliasing

l1 = [10,20,30,40]

l2 = l1

print(l2)

l2[1] = 123
print(l1)


# slice operator

l1 = [10,20,30,40]
l2 = l1[:]

print(l1)
print(l2)

l2[1] = 123
print(l1)
print(l2)		
		
# copy() function

l1 = [10,20,30]
l2 = l1.copy()

l2[1] = 123
print(l1)
print(l2)		
		
import copy

l1 =[10,20,30]

#print(id(l1))
l2 = copy.copy(l1)
#print(id(l2))

l2[1] = 345
print(l1)
print(l2)		
		

l1 = ['Ragav','Vengat']
l2 = ['ragav','rengat']

print(l1==l2)
print(l1>l2)
print(l1<l2)
print(l1!=l2)		
		
# Membership operator

# in , not in

l=[10,20,30,40]

print(10 in l)
print(100 not in l)

for no in l:
    if no==10:
        print("true")
		
		
l =['Ragav','Vengat','Gowtham']
name = 'kavin'
present = False
for i in l:
    if name == i:
        present = True
        break
        
if present == True:
    print("Name is present")
else:
    print("Name is not present")		
		
		
===
l =['Ragav','Vengat','Gowtham','Gowtham']
name = 'Gowtham'
present = False
count = 0
for i in l:
    if name == i:
        count+=1
else:
    print(count)
----
		
l = [ [10,20,30],
      [40,50,60],
      [70,80,90]
    ]
print(l)
    
for row in range(len(l)):
    print("row", row, "-->", l[row])
 
   
for row in range(len(l)):
    for value in range(len(l[row])):
        if value==0:
            print("row", row, "-->", l[row][value])
    print()
    
for row in range(len(l)):
    for value in range(len(l[row])):
        if value==2:
            print("row", row, "-->", l[row][value])
    print()		
		
for row in range(len(l)):
    for value in range(len(l[row])):
        if value==row:
            print("row", row, "-->", l[row][value])
    print()
		
# Transpose Matrix
		
l1 = [ [10,20,30],
       [40,50,60],
       [70,80,90]
     ]

l2 = [ [0,0,0],
       [0,0,0],
       [0,0,0]
     ]

for i in range(len(l1)):
    for j in range(len(l1[0])):
        l2[i][j] = l1[j][i]

for l in l2:
    print(l)		
		
-----
		
# count of each number present in the list   

l =[10,20,30,10,20,30,10,20,30,40,50,60]
l2 = [1,1,1,-1,-1,-1,-1,-1,-1,1,1,1]

name = l[]
count = 0

  
for i in range(len(l)):
    if  l[i] == name:
        if l2[3]!=-1:
            l2[i] = -1
        count+=1
else:
     print(count)
		
------
# input: s1 = 'A1B2C3'
# output: ABC6

s1 = 'A1B2C3'
output1 = '' 
output2 = ''
total = 0

for letter in s1:
    if letter.isalpha():# isalpha - means to confirm the character or not
        output1 = output1+ letter
    else:
        output2 = output2 + letter
else: 
    for j in range(len(output2)):                                
        no1 = int(output2[j])
        total += no1    
    output = output1+str(total)
    print(output)
		
----

#input: s1 = 'gwhm' : s2 = 'ota'
# output: gowtham

s1 = 'gwhm'
s2 = 'ota'
s3 = len(s1) if len(s1)<len(s2)else len(s2)
s4 = ''
for i in range(0,s3):
    s4=s4+s1[i]+s2[i]
    
s5 = len(s1) if len(s1)>len(s2)else len(s2)
for i in range(s3,s5):
    if len(s2)-s5>0:
        s4=s4+s2[i]
    else:
        s4=s4+s1[i]
print(s4)
		
-------
		
l1 = 'AAABBBCCCDDD'
l = []
for i in l1:
    if i not in l:
        l.append(i)
else:
    print(l)
    
    # output: ['A','B','C','D']
		
s = 'gowtham sekar'
l = s.split()
for i in l:
    print(i)
    
s = '09/02/2022'
l = s.split('/')
for i in l:
    print(i)
    
s = '-'.join(l)
print(s)
		
----
# input: A1B2C3
# output: AABBBCCCC
		
------		
		
s = "SundayMondayTuesday"
l = s.split("day ")
for i in l:
    print(i)
    
b=['sun','mon','tues']
c=''
for i in range(0,len(b)):
    c=c+b[i]+"day"+" "
print(c) 
		
	---
		
s = 'g'
no1 = ord(s) # ordinal value
no1 = no1 - 32
print(no1)
print(chr(no1)) # character

s = 'today is wednesday'
words = s.split(' ')
for word in words:
    letter = word[0]
    no = ord(letter)
    no = no - 32
    print(chr(no) + word[1:])
 
--
l1 = [10,20,30]
l2 = [10,20,30]
print(l1 == l2) # values / content comparison
print(l1 is l2) # address comparison

------
		
# input: one two three four
# output: one owt three ruof

s1 = 'one two three four'
words = s1.split()
s2 = ''
s3 = ''
for i in words:
    if words.index(i)%2!=0:
        for j in range(len(i)-1,-1,-1):
            s3=s3+i[j]
        s2=s2+s3+' '
        s3=''
    else:
        s2=s2+i+' '
print(s2)

		(OR)
		
# input: one two three four
# output: one owt three ruof
		
word=input("Enter sentance: ")
s=word.split()
words=''
for i in range(len(s)):
    if i%2==0:
        first=s[i]
        words +=first+" "
    else:
        l=s[i]
        sec=l[::-1]
        words+=sec+" "
         
print(words)
		
------

# input: l = [5,10,15,20,25,30]
# output:
# total no of even numbers: 3
# total no of odd numbers: 3

l =[5,10,15,20,25,30]
  # 0  1  2  3  4  5

even = 0
odd = 0

for i in l: 
    if i%2==0:
        even += 1 
    else:
        odd += 1
print("Total no of even numbers: ", even)
print("Total no of odd numbers: ", odd)
		
-----
# input : l =[5,10,15,15,15,20,20]	
# output: 15   # print continues three times

l =[5,10,15,15,15,20,20]
#   0  1  2  3  4  5  6

l1 = len(l)

for i in range(l1 - 2):
    if l[i] == l[i+1] and l[i+1] == l[i+2]:
        print(l[i])
		
-----
		
# input: "He is a good boy"
# output: boy good a is He

l = "He is a good boy"
 #   0  1  2  3   4
l1 = l.split()
l2 =""

for word in range(len(l1)-1,-1,-1):
    l2 = l2+l1[word]+" "
print(l2)
		
------
	
# input:  He a boy
#         is good 
#output:  He is a good boy

s1 = 'He a boy'
s2 = 'is good'

name1 = s1.split()
name2 = s2.split()
name3 = len(name1) if len(name1)<len(name2)else len(name2)
l = ' '

for i in range(name3):
    l = l + name1[i] + " " + name2[i] + " "  # He is a good

l1 = len(name1) if len(name1)>len(name2)else len(name2)

for i in range(name3,l1):
    if len(name2)-l1>=0:
        l = l + name2[i] + " "
    else:
        l = l + name1[i] + " "
print(l)
		
------
		
# input: A1B2C3
# output: AABBBCCCC

#s1 = 'A1B2C3' 
#s2 = ''
		
------
		
# set - No oreder, no indexing, no slicing

s = {10,20,30,40,}
print(s) 
print(type(s))

s = set(range(10))
print(s)

l = [10,20,30,10,20,30] 
s = set(l)
print(s) # does not allow duplicate(repeated one)

s = {} # creates dictionary not accept for empy sefor reference variable
s = set()
s.add(10)
s.add(20)
s.add("Ragav")  # add - single value adding
s.add(True)
print(s)
s.update([100,200]) # update - multiple values adding
print(s)
s.update(range(1,5))
print(s)

s2 = set()
s2.update(s)
print("s2 values aree :", s2)
		
------
s1 = {10,20,30,40}

s2 = s1.copy()
print(s2)

print(s2.pop())
print(s2)
		
s1 = {10,20,30,40,5}

s2 = s1.copy()
print(s2.discard(10)) # it remove but u/p will be None
print(s2)
print(s2.discard(123))
		
-----
		
# Mathematical operation in set

# Union

a = {10,20,30,40}
b = {30,40,50,60}
print(a|b)
print(a.union(b))

# Intersection
print(a & b)
print(a.intersection(b))

# difference
print(a-b)
print(a.difference(b))
print(b-a)
print(b.difference(a))

# Symmetric Difference --> a or b not both
print(a^b)
print(a.symmetric_difference(b))
		
---
# Membership operators
# in 
# not in

name = "Ragav"
s = set(name)
print(s)
print('R' in s)
print('a' in s)
print('R' not in s)
print('a' not in s)

---
# set comprehension

s = {no for no in range(1,11) }
print(s)
s = set()
for no in range(1,11):
    s.add(no)
print(s)
---
s1 = {10,20,30}
s2 = {10,20,30}
print(s1 == s2)
print(s1 is s2)
		
----
# set is mutable

s ={10,20,30,40}
f = frozenset(s)
print(f)
---
candidate = {"Kathir", " Kavin ", 22, 5.6, True}
print(type(candidate))
for value in candidate:
    datatype = type(value)
    if datatype == str:
        print(value)
		
----
		
ifl[0] == key:
    print("present")
ifl[1] == key:
    print("present")
ifl[2] == key:
    print("present")
ifl[3] == key:
    print("present")
ifl[4] == key:
    print("present")
		
		or
		
l = [10,15,20,25,30]

key = 20

for i in l:
    if i == key:
        print("present")
    else:
        print("not present")
-----
		
# linear Search
l = [10,15,20,25,30]

key = int(input())

#for i in l:
#    if i == key:
#       print("present")
#   else:
#        print("not present")
        
        
i =0
while i<len(l):
    if l[i] == key:
        print("present")
        break
    i+=1
    
else:
    print("not present")
	
------
# Binary Search 

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

key = int(input("Enter no:"))

min =0
max = len(l)-1
while min<=max:
    mid = (min+max)//2
    if key == l[mid]:
        print("Key is present at", mid)
        break
    elif key>l[mid]:
        min = mid+1
    elif key<l[mid]:
        max = mid - 1
        
else:
    print("Key is not present")
		
--------
		
# Tuple is imutable 

t = 10,20,30,40
print(t)
print(type(t))

t = (10,20,30,40)
print(t)
print(type(t))

l = [10,20,30,40]
t = tuple(l)
print(t)

t = tuple(range(1,5))
print(t)
		
t = ()
print(type(t))

t = (10)
print(type(t))

t = 10, # or (10,)
print(type(t))		
		
		
t=(1,2,12,3,4,5,6,7,8,9,10)
t1=(0,222,333)
for i in (t):
    print(t.index(i))
#print(t.remove(12))
#print(t.add(2))
#print(t.update(2))
print(t[1:9])
print(t[12])
print(t+t1) 		
		
l1 = [10,20,30]

l2 = l1

print("l1 memory", id(l1))
print("l2 memory", id(l2))

l2 = list(l1)
print("l2 memory second time", id(l2))
print(l1 == l2)
print(l1 is l2)		
		
		
		
t1 = (10,20,30)
t2 = t1
print(id(t1))
print(id(t2))
t2 = tuple(t1)
print(id(t2))
print(t1 == t2)
print(t1 is t2)

l1 = [10,20]
l2 =l1
l1[0] = 5

print(l1)
print(l2)
		
# sallow copy
# lazy loading

import copy

l1 = [10,20,30]
print(id(l1))

l2 = copy.copy(l1)
print(id(l2))

l1[0] = 100
print(l1)
print(l2)
		
-----------
		
# tuple
		
t1 = (10,20,30)
t2 = (40,50,60)

t3 = t1 + t2
print(t3)

t4 = t1 * 2
print(t4)
		
------
#tuple packing, unpacking
		
n1,n2,n3 = 10,20,30
t = n1,n2,n3
print(t)

t2 = tuple()
print(len(t2))

t2 = 1,2,3
n1,n2,n3 = t2
print(t2)
print(n1)
print(n2)
print(n3)

t =(no for no in range(1,6))
print(t)
for i in t:
    print(i)
----
n1 = (1,2,3,4,5)
n2 = (11,12,13,14,15)
for i in (n1):
    print(n1.index(i)) # index()

print(n1[1:4])
print(n1[1:4])    # slicing
print(n1+n2)      # adding two tuple
print(min(n1))    # min
print(max(n2))    # max
print(sorted(n2)) # sorted

for i in range(len(n1)): # len()
    print(i)
    
# output:

# 0
# 1
# 2
# 3
# 4
# (2, 3, 4)
# (2, 3, 4)
# (1, 2, 3, 4, 5, 11, 12, 13, 14, 15)
# 1
# 15
# [11, 12, 13, 14, 15]
# 0
# 1
# 2
# 3
# 4

# In Tuple which are not supported:
   
# print(n1.remove(5))     # remove does not support
# print(n1.add(11))       # add does not support
# print(n1.update(6,7))   # update does not support
# print(n1 | n2)          # Union does not support
# print(n1 & n2)          # intersection does not support
# print(n1 - n2)          # difference does not support
# print(n1 ^ n2)          # symmetric_difference does not support

l =(1,2,1,2,3,2,5)
name = 2
count = 0
for i in l:
    if name == i:
        count+=1 # count()
else:
    print(count) # output: 3 
    
------
		
# Dictionary - (key-value) pair

d = {}
print(type(d))
d[10] = "Ragav"
d[123] = "Vengat"
print("Before changing", id(d))
print(d)
print(d[123])
print(d[10])

d[123] = "Gowtham"
print("After changing", id(d)) # mutable
		
-------
		
d = {}
print(type(d))
d[90] = 'Ragav'
d[10] = 'Gowtham'
d['Vengat'] = 123
print(d)

d['Ragav'] = 'Namakkal'
print(d)
print(d[90])
print(d[9]) # key error bz not defined
		
		
------
		
students = {}

no = int(input("Enter no of students"))
i = 1
while i<=no:
    name = input("Enter ypur name")
    doorNo = int(input("Enter door no"))
    students[name] = doorNo
    i+=1
    
for detail in students:
    print(detail) # key
    print(students[detail])# value
		
----
d = {}
print(type(d))
d[90] = 'Ragav'
d[10] = 'Gowtham'
d['Vengat'] = 123
print(d)

del d[90]
print(d)
d.clear() # clears the value
print(d)
del d # delete the entire dictionary
print(d)
		
----------
d = {}
print(type(d))
d[90] = 'Vengat' # entry item
d[10] = 'Gowtham'
d['ragav'] = 123
print(d.popitem()) # popitem removes radomly
print(d)
------
		
d = {}
d[90] = 'Vengat' # entry item
d[10] = 'Gowtham'
d['ragav'] = 123
print(d.keys()) # keys - refernce variable 
print(d.values()) # values - object
print(d.items()) # items - refernce variable  with object

for k in d.keys():
    print(k)
    
for v in d.values():
    print(v)
        
for k, v in d.items():
    print(k, v)
    
for item in d.items():
    print(type(item))
    print(item)
	----
		
t = [10,20,30]
d = {}
d['ragav'] = t
print(d)
t[0] = 20
print(d)
		
------
		
t = 10,20,30
d = {}
d[t] ='Ragav'
print(d)
		
----
d = {}
print(type(d))
d[90] = 'Vengat' # entry item
d[10] = 'Gowtham'
d['ragav'] = 123

d2 = d.copy() # copy means zerox
print(d2)

print(id(d))
print(id(d2))
		
d = {}
print(type(d))
d[90] = 'Vengat' # entry item
d[10] = 'Gowtham'
d['ragav'] = 123

d2 = {}
d2['jordan'] = 2323
d2.update(d) # update add @ first value
print(d2)

print(d2.get('jordan'))
print(d2.get('jack')) # none
print(d2.get('jack', 'No Data is found')) # o/p: No Data is found		
		
-----------
# getting input for dictionary from keyboard/User

#eval() - Function

students={}
no = int(input("Enter no. of students"))
i=1
while i<=no:
     name,age=input("Enter name and age: ").split()
  
     students[name]=age
     i+=1
else:
     print(students)
        
# output: 
# Enter no. of students2
#Enter name and age: gowtham 21
#Enter name and age: ragav 26
#{'gowtham': '21', 'ragav': '26'}
		
------
d = {}
# d = dict() empty dictionary
d[10] = 'gowtham'
d[20] = 'ragav'
d[5] = 'mohan'

d.setdefault(10,'vengat')
d.setdefault(100,'irshad')

print(d)
-----
d ={}

d = {'vengateswaran':123}
print(d.get('vengateswaran'))
print(d.get('gowtham'))
print(d.get('ragav', 345))
print(d.get('ragav',d.get('vengateswaran'))
	  
-------
s = 'vegateswaran'
d = {}

for letter in s:
    d[letter] = d.get(letter,0)+1
else:
    for letter,freq in d.items():
        print(letter, 'comes',freq, 'times')
-----
	  
#Frequency of each letter in a given string

s = 'vegateswaran'
freq = {}

for letter in s:
    if letter not in freq:
        freq[letter] = 1
    else:
        freq[letter] = freq[letter] + 1
else:
    print(freq)
---
s = [10,20,30,10,20,30,10,20,40,50]
freq = {}

for letter in s:
    if letter not in freq:
        freq[letter] = 1
    else:
        freq[letter] = freq[letter] + 1
else:
    print(freq)
    
big = 0
no = 0
for k, v in freq.items():
    if v>big:
        big = v
        no = k
else:
    print(no,'comes more no. of times',big)
---
s = [10,20,30,10,20,30,10,20,40,50]
freq = {}

for letter in s:
    if letter not in freq:
        freq[letter] = 1
    else:
        freq[letter] = freq[letter] + 1

for k, v in freq.items():
    if v==1:
        print(k,v)
---
prices = {'onion':50,'tomato':100,'potato':40}
for k, v in prices.items():
    if k == 'tomato':
        prices[k] = 120
else:
    print(prices)
    
prices = {'onion':50,'tomato':100,'potato':40}
for k, v in prices.items():
    prices[k] = v+10
else:
    print(prices)
    
prices = {'onion':50,'tomato':100,'potato':40}
for k, v in prices.items():
    
    v = v+(v*0.1)
else:
    print(prices)
-----
# Company: 

# 1) Dictionary --> Name: Salary
# 2) Highest Salary
# 3) Lowest Salary
# 4) Total salary, Average salary
# 5) Salary wise employee details
# 6) 'gowtham' - present or not
# 7) 50000 - salary

# no = int(input("Enter no. of students"))

Employee = {} 
i = True

while i==True:
    e=input("do you have add your employee list? yes/no : ")
    if 'yes'==e:
        Name,Salary = input("Enter Name and Salary : ").split()
        Employee[Name] = int(Salary)
    elif 'no'==e:
        i=False
    else:
        print("enter valid input!")
        
        
for i in sorted(Employee.keys()):
  print("assanding order salary",i)  

low=0
heigh=0

for val in Employee.values():
  
  if heigh <=val :
    heigh=val
  elif heigh>=val:
    low=val
 
ave=0
count=0
for v in Employee.values():
    ave+=v 
    count+=1 
print("employee average salary : ",ave//count)

char = 'gowtham'
currency = 50000

for k,v in Employee.items():
    if char==k:
        print("present")
    elif currency == v:
        print("currency present")
    
    
print("this is min value ",low)
print("this is max value ",heigh)
    
	  (OR)
	  
a= int(input())
p={}
for i in range(a):
    n=input("Enter the Name of employee: ")
    s=int(input("Enter the Salary of employee: "))
    p[n]=s
b=[]
for i,j in p.items():
    b.append(j)
print("Highest Salary: ",max(b))
print("Lowest Salary: ",min(b))
print("Total Salary: ",sum(b))
print("Average Salary: ",sum(b)/a)
c=[]
for i,j in p.items():
    if j not in c:
        c.append(j)
for i in sorted(c):
    print("Employee Detail who get Salary {0}".format(i))
    for j,k in p.items():
        if i==k:
            print(j)
d=input("Enter the Name of Employee weather present or not: ")
for i,j in p.items():
    if d==i:
        print("{0} is present and Salary of {0} is {1}".format(i,j))
        break #key has no duplication so confidentah break use panlam
else:
    print(d,"is not present")
e=int(input("Check the Salary is given or not: "))
if e in b:
    print("Yes")
    for j,k in p.items():
        if k==e:
            print(j)
else:
    print("No")
------
# def -- definition - 

def wish():
    print("Congrats - Muthu")
    print("Congrats - Ragav")
    print("Congrats - Vengat")
    print("Congrats - Irshad")
    print("Congrats - Mohan")
    print("Congrats - Gowtham")
    
wish() # Function Calling

def wish(name):
    print("Congrats", name)

wish("Ragav") # Function Calling
wish("Vengat")
wish("Gowtham")
----
def add(no1,no2):
    return no1+no2

result = add(123,234)
print(result) # 357
print(add(10,20)) # 30
	  

def add(no1,no2):
    print(no1+no2)
n = int(input("Enter no1 : "))
m = int(input("Enter no2 : "))        
      
add(n,m)
---
def wish(name):
    print(name)
    
print(wish('gowtham'))
--
def add(no1,no2):
    return no1+no2

print(add(10,20))

def wish(name):
    print(name)
print(wish("Ragav"))
-----
def factorial(no):
    result = 1
    while no>=1:
        result = result * no
        no-=1
    return result

factorial(4)

def factorial(no):
    result = 1
    while no>=1:
        result = result * no
        no-=1
    print(result)
    
for i in range(1,11):
    factorial(i)
	  
------
# linear Search

def linear_Search(l):
    
    i = 0
    key = int(input("Enter the value : "))
    while i<len(l):
        if l[i] == key:
            print("present")
            break
        i+=1

    else:
        print("not present")
	  
l = [10,15,20,25,30]
	  
linear_Search(l)
	  
---
# Binary Search 

def Binary_Search(l):
    
    key = int(input("Enter no:"))

    min =0
    max = len(l)-1
    while min<=max:
        mid = (min+max)//2
        if key == l[mid]:
            print("Key is present at", mid)
            break
        elif key>l[mid]:
            min = mid+1
        elif key<l[mid]:
            max = mid - 1

    else:
        print("Key is not present")

bst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

Binary_Search(bst)
	  
-----
l = eval(input("Emter no : "))
print(l)
	  
---
# bubble sort

def bubble_sort(list1):  
     
    srink = sorted(list1) 
    return srink

list1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", list1)   
print("The sorted list is: ", bubble_sort(list1))  
---
# prime number

def prime_number(num):
    
    if num > 1:
        for i in range(2,int(num/2)+1):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
        else:
             print(num,"is a prime number")
    else:
         print(num,"is not a prime number") 
        
num = int(input("ENter a number: "))
prime_number(num)
	  
--
	  
# count of digits
def count(a,d=0):
    
    if a >0: 
      
        c=a//10 # 12
        
        d+=1 
        
        return count(c,d) # 12, 
    else:
        print(d)

i=int(input("Enter input : ")) # 1234
count(i)

# output:
Enter input : 1234
4
---
#addition of digits


def count(a,d=0):
    
    if a >0: 
        
        c=a%10 
        e=a//10
        d+=c
        
        return count(e,d)
    else:
        print(d)

i=int(input("Enter input : "))
count(i)


# output:

Enter input : 456
15
----

#palindrome number

def pali(string):
    if(string==string[::-1]):
          print("The string is a palindrome")
    else:
          print("Not a palindrome")
      
      
string=input(("Enter a string:"))
pali(string)
	  
# output:
Enter a string:11
The string is a palindrome

Enter a string:12
Not a palindrome
---

# Factorial 

def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

num = int(input("Enter number finding factorial : "))

print(fact(num))

# output:
Enter number finding factorial : 3     
6

Enter number finding factorial : 5
120
	  
------
# filter():

def printEven(no):
    if no%2 == 0:
        return True
    else:
        return False
    
l = [10,11,12,13,5,6,7]  # iterator

even_list = list(filter(printEven, l)) # dictonary for set
print(even_list)
	

l = [10,11,12,13,5,6,7,10]  # iterator

even_list = list(filter(lambda no:no%2==0, l))
print(even_list)
	  
----

# map()

l = [45,78,15,32,65,45] # given list +2

l2 = []

def grace_mark(mark):
    return mark+2

l2 = list(map(grace_mark,l))
print(l2)
--
# map() - using lambda()

l = [78,15,32,65,45] # given list +2

l = list(map(lambda no:no+2, l))
print(l)
--
# reduce() reduces sequence of elements into a single element

from functools import *

l = [10,20,30,5,8,9]

output = reduce(lambda no1,no2:no1+no2, l)
print(output)
---
# Function aliasing:

def display(name):
    print(name)
    
display('ragav')

wish = display

#del display

wish('ragav')
---
# import 1 file call another
def add(no1,no2):
	print(no1+no2)
	
def sub(no1,no2):
	print(no1-no2)
	
def mul(no1,no2):
	print(no1*no2)
	
def div(no1,no2):
	print(no1//no2)
	  
	  =
import second
print(second.add(10,20))
	  
from second import owner, div
print(owner)
div(100,25)
--------
import sys
sys.path.insert(0, '/home/ragavjordan/Documents/Python10')

from first import add, div

add(25,8)
div(10,15)
--
import sys
print(sys.path)

print(sys.version)
---
# command line arguments

import sys
no = len(sys.argv)

print("Total Arguments ",no)
print("First Arguments",sys.argv[0])
for i in range(no):
	print(sys,argv[i])
--
import sys
name = sys.stdin.readline()
print('welcome',name)
--
# member aliasing

import sys
sys.path.insert(0,'/home/ragavjordan/Documents/github')

from second import add as plus, sub as minus
plus(10,20)
minus(20,10)
---
class Student:
    """This is my first class program"""

#print(Student.__doc__)
help(Student) # ecp + colon + q
	  
---
class Laptop:
    """This is my Laptop"""
    def __init__(self): # constructor
        pass
    
    def on(self):
        print("Switching on")
        
    def type(self):
        print("Typing")
        
powerButton = Laptop() # object
powerButton.on()
keyboard = Laptop() # object
keyboard.type()
--
class Students:
    def __init__(self,name,rollno,address):
        self.name = name
        self.rollno = rollno
        self.address = address
        
    def printDetails(self):
        print(self.name)
        
s1 = Students("Gowtham",123,"chennai")
s2 = Students("ragav",452,"Erode")
s3 = Students("Vengat",215,"Madurai")

#s1.printDetails()
#s2.printDetails()
s3.printDetails()
--
class Students:
    def __init__(self,name,rollno,address,address2):
        self.name = name
        self.rollno = rollno
        self.address = address
        
    def printDetails(self):
        print(self.name)
        
s1 = Students("Gowtham",123,"chennai")
s2 = Students("ragav",452,"Erode")
s3 = Students("Vengat",215,"Madurai")
s4 = Students("Mohan",1,"Goa")

#s1.printDetails()
#s2.printDetails()
s4.printDetails()

--
# Types of variables:

class Employee:
    def __init__(self):
        self.name = "Ragav"
        self.country = "Namakkal"
        
e1 = Employee()
#print(e1.name)
#print(e1.country)
print(e1.__dict__)

# self --> instance variable/object level varible
--
# Types of variables:

class Employee:
    def __init__(self):
        self.name = "Ragav"
        self.country = "Namakkal"
        
    def assign(self):
        self.dept = "developer"
        print(self.dept)
        
        
e1 = Employee()
e1.assign()
#print(e1.name)
#print(e1.country)
print(e1.__dict__)

# self --> instance variable/object level varible
=====
# outside the class:

class Employee:
    def __init__(self):
        self.name = "Ragav"
        self.country = "Namakkal"
        
    def assign(self):
        self.dept = "developer"
        print(self.dept)
        #del self.dept 
        
e1 = Employee()
e1.exp = 8
e1.assign()
print(e1.__dict__)
del e1.exp # - for delete
print(e1.__dict__)

# self --> instance variable/object level varible
--
class Shop:
    discount = 10
    def __init__(self,price):
        self.price = price
        
bread = Shop(20)
rice = Shop(50)
print(bread.discount)
print(rice.discount)
print(bread.discount)
--
class HumanBeing:
    sense = 6
    
    @classmethod  # Decorator
    def rational_thinking(cls,name):
        print(name,"thinks rationally")
        
HumanBeing.rational_thinking("Vengat")
HumanBeing.rational_thinking("Gowtham")
--
class SuperMarket:
    discount = 10
    
    def __init__(self,price):
        self.price =  price
    
    def calculate_price(self):
        self.final_amount = self.price - self.discount
        print(self.final_amount)

prod1 = SuperMarket(100)
prod1.calculate_price()

prod2 = SuperMarket(80)
prod2.calculate_price()
--
class SuperMarket:
    discount = 10
    
    def __init__(self,price):
        self.price =  price
    
    @classmethod
    def welcome_drink(cls):
        print("juice",cls.discount)
        
    def calculate_price(self):
        self.final_amount = self.price - self.discount
        print(self.final_amount)

prod1 = SuperMarket(100)
prod1.calculate_price()

prod2 = SuperMarket(80)
prod2.calculate_price()

SuperMarket.welcome_drink()
---
class SuperMarket:
    discount = 10
    
    def __init__(self,price):
        self.price =  price
    
    @classmethod
    def welcome_drink(cls):
        print("juice",cls.discount)
        
    @staticmethod # Not using class or self specific variables
    def bike_parking(fee):
        print("Parking fee is ",fee)
        
    def calculate_price(self):
        self.final_amount = self.price - self.discount
        print(self.final_amount)

prod1 = SuperMarket(100)
prod1.calculate_price()

prod2 = SuperMarket(80)
prod2.calculate_price()

SuperMarket.welcome_drink()
SuperMarket.bike_parking(20)
--
# Inner class
	  
class Home:
    
    def __init__(self):
        self.hhh = self.Hall()
    
    def estimate_cost(self):
        print("Home Estimation")
        
    class Hall:
        
        def build(self):
            print("Building hall")
            
h = Home()
h.estimate_cost() 
h.hhh.build()
---
# two class calling()
class Home:
    
    def __init__(self,contractor):
        self.builder = contractor
    
    def estimate_cost(self):
        print("Home Estimation" + self.builder)
        
class Hall:
        
    def build(Home):
        print("During Hall Creation", Home.builder)
            
h = Home("ABCD builder")
h.estimate_cost() 
Hall.build(h)
--
# Garbage collection - removing unused memory

import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())
--
# inheretance

class Engine:
    cc = 125
    def __init__(self):
        self.mileage = 50
                 
    def start(self):
        print("Starting", self.mileage)
        
class Bike:
    def __init__(self):
        self.engine = Engine()
        
    def ride(self):
        self.engine.start()
        print(self.engine.mileage)
        
shine = Bike()
shine.ride()
---
# is a relationship

class Parent:
    fee = 500
    def __init__(self):
        self.school = "ABCD"
        
    def admit(self):
        print("Admission in", self.school)
        
    @classmethod
    def grow(cls):
        print("Growing every child equally")
        
    @staticmethod
    def cook():
        print("cooking")
        
class Child(Parent):
    pass

c = Child()
c.cook()
c.admit()
c.groew()
print(c.fee)
--
# is a relationship

class Parent:
    fee = 500
    def __init__(self):
        self.school = "ABCD"
        
    def admit(self):
        print("Admission in", self.school)
        
    @classmethod
    def grow(cls):
        print("Growing every child equally")
        
    @staticmethod
    def cook():
        print("cooking")
        
class Child(Parent):
    pass

c= Child()
c.cook()
c.admit()
c.grow()
print(c.fee)
    
class GrandChild(Child):
    pass

gc= GrandChild()
gc.cook()
gc.admit()
gc.grow()
print(gc.fee)
	  
--
# is a relationship

class Parent:
    fee = 500
    def __init__(self):
        self.school = "ABCD"
        
    def admit(self):
        print("Admission in", self.school)
        
    @classmethod
    def grow(cls):
        print("Growing every child equally")
        
    @staticmethod
    def cook():
        print("cooking")
        
class Child(Parent):
    def __init__(self):
        self.school = "PQRS"
        super().__init__()
        
    def display(self):
        super().cook()
        
c= Child()
#c.cook()
c.admit()
c.grow()
print(c.fee)
#print(super().school)

class GrandChild(Child):
    pass

gc= GrandChild()
gc.cook()
gc.admit()
gc.grow()
print(gc.fee)
print(gc.school)
--
class Parent:
    def __init__(self,name):
        self.name = name
        
    def choose_career(self):
        print(self.name,"Army")

class Child(Parent):
    def __init__(self,name):
        self.name = name
        
    def choose_career(self):
        #super().choose_career()
        print(self.name,"IT")
      
c = Child("Ragav")
c.choose_career()
class Parent:
    def work(self):
        print("Agri")
        
class Child(Parent):
    def work(self):
        print("Business")
        
class GrandChild(Child):
    def work(self):
        #Parent.work(self)
        print("IT")
        
gc = GrandChild()
gc.work()
	  
----
# Wordle

import enchant

time=1
while time<=6:
  d = enchant.Dict("en_US")
  word=input("Enter wordle with five letters : ")
  word_list=list(word)
  s=d.check(word)
  print("correct letter with @ symbel")
  print("correct letter wrong place $ symbel")
  print("wrong letter with X symbel")
  if s==True:

    wordle=['r','o','b','i','n']
    
    for col in range(5):
      if wordle[col]==word_list[col]:

        print("@")
        
      elif word_list[col] in wordle:
        print("$")

      elif word_list[col] not in wordle:
        print("X")


  else:
    print("Not in word list")

  time+=1
	  
---
# Web Scraping:

import requests
 
r = requests.get('https://goinggnu.wordpress.com/2014/07/23/need-50-ideas-for-a-python-hackathon/')

print(r.url)
print(r.status_code)

#print(r.content)
---
# abc --> Abstract Base class
# we caanoot be onstantiated

from abc import *
class Parent(ABC):
    @abstractmethod
    def study(self):
        pass
    
    def grow(self):
        print("Growing Children")
        
class Child(Parent):
    #pass
    def study(self):
        print("Studying")
        
    def work(self):
        print("IT Job")
    
ch = Child()
ch.study()
ch.work()
ch.grow()
# p = Parent()
--
# Encapsulation

class HumanBeing:
    name = "Raja"
    _id = 123
    __adhar = 12345 # __ double underscore is private variable
    
    def work(self):
        print(HumanBeing.name)
        print(HumanBeing._id)
        print(HumanBeing._adhar)
        
hb = HumanBeing()
hb.work()
print(HumanBeing.name)
print(HumanBeing._id)
print(HumanBeing._adhar)
--
class HumanBeing:
    def __init__(self):
        self.__adhar = 1234
        
hb = HumanBeing()
print(hb._HumanBeing__adhar) # for using private variable (-hbj__hvk)
--
class VasanthAndCo:
    
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def __str__(self):
        return "{}{}{}:".format(self.brand,self.model,self.price)
        
 # string overriding
tv = VasanthAndCo("Sony","s1",20000)
print(tv)
--
no1 = int(input())
no2 = int(input())
try:
    print(no1/no3)
except ZeroDivisionError:
    print("Check no2")
except NameError:
    print("Check variable names")
print("Hi")


--
try:
    num1 = int(input())
    num2 = int(input())
    print(num1/num2)
    print(num1/num3)
except (ZeroDivisionError, ValueError) as msg:
    #print(msg)
    print("Check inputs") 
else:
    print("Hello")
finally:# Code Cleaning
    print("abcd")
# customised eception:

class PasswordError(Exception):
    
    def __init__(self, msg):
        self.msg = msg
        print(self.msg)
try:
    password = input()
    if len(password)<8:
        pe = PasswordError("Min 8 character")
        raise pe
        
except PasswordError:
    print("Check Check")
	  
-----
# scrap a flipkart.com and get rate of a given product

import bs4
from bs4 import BeautifulSoup as bs
import requests

link="https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off/"

page=requests.get(link)

page.content

soup=bs(page.content,"html.parser")


name=soup.find("div", class_="_4rR01T")
print(name.text)

price=soup.find("div", class_="_30jeq3 _1_WHN1")
print(price.text)

# o/p

realme Narzo 50A (Oxygen Blue, 64 GB)
₹11,549
--
# Bank Accounting:

class Account:
    def __init__(self,name,balance,minimum_balance):
        self.name=name
        self.balance=balance
        self.minimum_balance = minimum_balance
        
    def deposit(self,money):
        current_balance=self.balance+money
        return current_balance
    
    def withdraw(self,money):
        current_balance=self.balance-money
        return current_balance
    
    def enquiry(self):
        return self.balance
        
    def current(self):
        current=self.balance
        print("current balance",current)
    
    def saving(self):
        save=self.balance
        print("saving balance",save)
        
class Current(Account):
    def __init__(self,name,balance,minimum_balance):
        self.name=name
        self.balance=balance
        self.minimum_balance=minimum_balance
    
    def check(self):
        super().current()
        
class Savings(Account):
    def __init__(self,name,balance,minimum_balance):
        self.name=name
        self.balance=balance
        self.minimum_balance=minimum_balance
        
    def save(self):
        super().saving()
    
name=input("Enter account holder name : ")    

c=Current(name,1000,100)
print("deposite Money",c.deposit(100))
print("withdraw Money",c.withdraw(10))
c.check()

s=Savings("gowtham",1000,100)
s.save()

# o/p

Enter account holder name : jordan
deposite Money 1100
withdraw Money 990
current balance 1000
saving balance 1000

-----
	  
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import matplotlib.pyplot as plt
import numpy as np

photo = Image.open("/home/ragavjordan/Documents/Python10/photo.png")
#photo1 = Image.open("/home/ragavjordan/Pictures/photo1.png")

resize = photo.resize((300,300))
#resize1 = photo.resize((350,350))
plt.imshow(resize)

#resize.show() # save("p.png")

draw = ImageDraw.Draw(resize)
font = ImageFont.truetype("Ani.ttf",50)

draw.text((0,0),"python",(0,0,0),font = font)
plt.subplot(1,2,1)
plt.title("python screenshot")
plt.imshow(resize)
---
# to open file using (filename & mode(read"r", or write"w"))
# file writing
	  s
f = open("/home/ragavjordan/Documents/Python10/abc.txt","a")
f.write("gowtham\n")
f.write("mohan\n")
f.close()  # after write or read plz close() the compose.
# for adding name put"a" means append())
--
	  
f = open("/home/ragavjordan/Documents/Python10/abc.txt","a")
list = ['mohan','jordan','gowtham','ragav']
f.writelines(list)
f.close()
# incase for list[] use f.writelines(list)
=====
# file reading:
	  
f = open("/home/ragavjordan/Documents/Python10/abc.txt","r")
data = f.read()
print(data)
f.close()
--
f = open("/home/ragavjordan/Documents/Python10/abc.txt","r")
data = f.read(7)
print(data)
f.close()
--
# file readline()

f = open("/home/ragavjordan/Documents/Python10/abc.txt","r")
data = f.readline()
print(data, end = '')
data = f.readline()
print(data, end = '')
data = f.readline()
print(data, end = '')
f.close() 
--
# file readlines()

f = open("/home/ragavjordan/Documents/Python10/abc.txt","r")
data = f.readlines()
for line in data:
    print(line, end = '')
f.close() 
--
f = open("/home/ragavjordan/Documents/Python10/abc.txt","r")
data = f.read(10)
print(data)
print(f.readline())
data = f.read(5)
print(data)
print(f.read())
f.close() 
--
with open("/home/ragavjordan/Documents/Python10/abc.txt","r") as f:
    data = f.read(2)
    print(data)
    print(f.tell()) # tell() for showing curser
    print(f.readline())
    print(f.tell())
    data = f.read(5)
    print(data)
    print(f.tell())
    print(f.read())
    print(f.tell())
    f.close() 
--
# database - with , open

with open("/home/ragavjordan/Documents/Python10/bcd.txt","w") as f:
    f.write("gowthan")
    with open("/home/ragavjordan/Documents/Python10/bcd.txt","r+") as f:
        data = f.read()
        print(data)
        print("Cursor position", f.tell())
        f.seek(0) # seek() commanding cursor position
        print("Cursor position", f.tell())
        f.write("vengat")
       # f.seek(0)
        data = f.read()
        print(data)
        f.close()
--
with open("/home/ragavjordan/Documents/Python10/bcd.txt","w") as f:
    print("File name", f.name)
    print("Mode",f.mode)
    print(f.readable())
    print(f.writable())
    print(f.closed)
    f.close()
--
# line countwords with given file:

import os,sys
file_name = input("Enter file name")
if os.path.isfile(file_name):
    f = open(file_name,"r")
else:
    print("File doe not exist")
    
lineCount = wordCount = alphaCount = 0
for line in f:
    lineCount+=1
    alphaCount = alphaCount+len(line)
    words = line.split()
    wordCount = wordCount + len(words)
else:
    print(lineCount)
    print(alphaCount)
    print(wordCount)
--
# image_file reading:

file1 = open("/home/ragavjordan/Pictures/photo.png","rb")
file2 = open("/home/ragavjordan/Pictures/ph.png","wb")
bytes = file1.read()
file2.write(bytes)
	  
--
# Getting the Current working directory:

import os

cwd = os.getcwd()
     
print("Current working directory:", cwd)s
---
# comma separated values:

import csv

# for only write ("w") need newline = ''

with open("student.csv","r") as f:
    csv_reader = csv.reader(f)
    output = list(csv_reader)
    for line in output:
        for word in line:
            print(word,"", end = '')
        print()
--
# comma separated values:

import csv

# for only "w" need newline = ''

with open("student.csv","w",newline = '') as f:
    csv_reader = csv.reader(f)
    output = list(csv_reader)
    for no in range(count):
        sid = int(input("Enter Id"))
        sname = input("Enter Name")
        csv_writer.writerow([sid,sname])
--
# Decorator Functions:

def check_movie(func):
    def inner(name):
        if name=='beast':
            print("How do you watch",name)
        else:
            func(name)
    return inner

@check_movie
def watch_movie(name):
    print("watching",name)
    
watch_movie("Valimai")
#watch_movie("beast")
--
# Generator Functions:
# Generating sequence of values
# keyword : yield

def gen_demo():
    yield "one"
    yield "two"
    yield "Three"
    
gd  = gen_demo()
print(type(gd)) # <class genaratoe>

print(next(gd))
print(next(gd))
print(next(gd))
--
def countdown(num):
    print("Start Count Down")
    while num>0:
        yield num
        num = num -1
        
values = countdown(5)
print(values)
for no in values:
    print(no)
---
g = (no*no for no in range(5000000000000))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
--
g = [no*no for no in range(5000000000000)]
print(g(0))
print(g(1))
print(g(2))
print(g(3))
-- 
# Please don't try this code: WARNING = Hang agidum macha
	  
g = [no*no for no in range(5000000000000)]
print(g(0))
print(g(1))
print(g(2))
print(g(3))
--
#  Treating the functions as objects.
def shout(text):
    return text.upper()
 
print(shout('Hello'))
 
yell = shout
 
print(yell('Hello'))
--
# Passing the function as an argument
def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func):
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)

greet(shout)
greet(whisper)
---
import sqlite3
connection = sqlite3.connect("/home/ragavjordan/Documents/Python10/ABCD.db")
print("Database opened successfully")
connection.execute("create table contactdetails (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")
print("Table created successfully")
connection.close() 
--
# delete the table after the connection:
	  
import sqlite3
connection = sqlite3.connect("/home/ragavjordan/Documents/Python10/ABCD.db")
print("Database opened successfully")
cursor = connection.cursor()
cursor.execute('''DROP TABLE contactdetails;''') # delete
connection.close()
--
# 
import sqlite3
connection = sqlite3.connect("/home/ragavjordan/Documents/Python10/ABCD.db")
print("Database opened successfully")
cursor = connection.cursor()
sql_command = """
             CREATE TABLE Student(
             RollNo INTEGER PRIMARY KEY,
             Sname VARCHAR(20),
             Grade CHAR(1),
             gender CHAR(1),
             Average DECIMAL(5,2),
             birth_date DATE);"""
cursor.execute(sql_command)
sql_command = """INSERT INTO
     Student(RollNo,Sname,Grade,Gender,Average,birth_date)
                VALUES(null, "Akshay", 'B','M', "87.8","2001-12-12");"""
cursor.execute(sql_command)
connection.commit()  #ctrl+s
connection.close()
print("Student Table Created") 
--
# list of data in table:
	  
import sqlite3
connection = sqlite3.connect("/home/ragavjordan/Documents/Python10/ABCD.db")
print("Database opened successfully")
cursor = connection.cursor()
student_data = [("Thiru","C","M","75.2","1998-05-17"),
                ("Raja","B","F","75.2","1998-04-17"),
                ("Bala","A","M","72.2","1999-05-17"),
                ("Kannan","D","M","87.2","1998-05-27")]
for p in student_data:
    format_str = """INSERT INTO Student(Rollno, Sname, Grade, Gender,Average,birth_date)
                    VALUES(Null, "{name}","{gr}","{gender}","{avg}","{birthdate}");"""
        # {} space holder
    sql_command = format_str.format(name=p[0],gr=p[1],gender=p[2],
                                    avg=p[3],birthdate=p[4])
    cursor.execute(sql_command)
connection.commit()
connection.close()
print("Records added")
print("Student Table Created") 
--
# fetch all:
	  
import sqlite3
connection = sqlite3.connect("/home/ragavjordan/Documents/Python10/ABCD.db")
print("Database opened successfully")
cursor = connection.cursor()
cursor.execute("SELECT * from Student") # *- every column value
ans = cursor.fetchall()
for i in ans:
    print(i) 
--
# fetchone
import sqlite3
connection = sqlite3.connect("/home/ragavjordan/Documents/Python10/ABCD.db")
print("Database opened successfully")
cursor = connection.cursor()
cursor.execute("SELECT * from Student") # *- every column value
result = cursor.fetchone() #Data Values 
print(result)
'''while result is not None:
    print(result)
    result = cursor.fetchone() #next line '''
---
# only grade fetchingall
import sqlite3
connection = sqlite3.connect("/home/ragavjordan/Documents/Python10/ABCD.db")
print("Database opened successfully")
cursor = connection.cursor()
cursor.execute("SELECT DISTINCT(Grade) from Student") # *- every column value
result = cursor.fetchone() #Data Values 
print(result)
while result is not None:
    print(result)
    result = cursor.fetchone() #next line 
--
# showing expect AB grade 
import sqlite3
connection = sqlite3.connect("/home/ragavjordan/Documents/Python10/ABCD.db")
print("Database opened successfully")
cursor = connection.cursor()
cursor.execute("SELECT Rollno,sname from student where grade<>'A' and Grade<>'B'")
result = cursor.fetchall()
print(*result,sep='\n')
--
# delete
	  
import sqlite3
connection = sqlite3.connect("/home/ragavjordan/Documents/Python10/ABCD.db")
print("Database opened successfully")
connection.execute("DELETE from Student where Rollno='2'")
connection.commit()
print("Total no. of rows deleted",connection.total_changes)
connection.close()
--

	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  



	  
	 
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
		
		
		
		
		
		