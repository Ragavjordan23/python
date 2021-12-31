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
rint(today != tomorrow)
