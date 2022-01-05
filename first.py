#Operator Chaining
age1 = 10
age2 = 12
age3 = 14
print(age1<age2<age3) # output: True
print(10==20==30)  # output: False

#identity operator
no1 = 10
no2 = 10
print(no1 is no2) # output: True
print(no1 == no2) # output: True

#Escape Characters

print("Hi\t GoodMorning") 
print("Hi\n GoodMorning")

#output: 
# Hi   GoodMorning
# Hi
#      GoodMorning

print('I\'m good') # output: I'm good

print(10//5) # o/p: 2
print(2**3) # o/p: 8
print(3**2) # o/p: 9
	  
mark = 65
mark = mark + 5
mark+=5
mark%=5
	  
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
print(today == tomorrow)
print(today != tomorrow)

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

#Using # input find Highest & Lowest marks
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

# looping Statement
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
