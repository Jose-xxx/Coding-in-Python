#!/bin/python3

#print string
print("strings and things:")
print('hola, world!')
print('''hello, this a multi-line 
string!''')
print('this is' + ' a string')

print('\n') #new line

#maths
print ("math time!:")
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PENDAS
print(50 ** 2) #exponents
print(50 & 6) #modulo
print(50 // 6) #number without leftovers

print('/n') #new line

#variables and methods
print('Fun with vairables and methods:')
quote = 'all is fair in love and war'
print(len(quote)) #length
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title

name = "Jose"
age = 31 #int int(31)
shoesize = 11.5 #float float(3.7)

print(int(age))
print(int(31.1)) #does not round

print("my name is " + name + " and I am " + str(age) + ' years old.')

print('\n') #new line

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print("\n") #new line

#functions
print('now, some funtions:')
def who_am_i():
	name = 'Jose'
	age = 29
	print("my name is " + name + " and I am " + str(age) + ' years old.')

who_am_i()

#adding in parameters
def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(101)

#add in multiple parameters
def add(x,y):
	print(x + y)
	
add(7,9)
add(305,207)

#using return
def multiply(x,y):
	return x * y

print(multiply(7,7))

def square_root(x):
	return x ** .5
	
print(square_root(64))

print('\n') #new line

def n_l():		#this a funtion for creating space/ a new line
	print('\n') 

print('-space-')

n_l() #new line

print('space again')
n_l()
#boolean expressions (true or false)
print('boolean expresions:')
bool1 = True
bool2 = 3*3 == 9 #math exprssion needs ==
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = 'true'
print(type(bool5))

#relational and boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)

test_and = (7 > 5) and (8 < 7)
test_or = (7 > 5) or (5 < 7)
test_not = not True

print(test_and)

n_l() #new line

#conditional statement
print('conditional statements:')
def soda(money):
	if money >= 2:
		return "you've got yourself a soda!"
	else:
		return 'no soda for you!'
		
print(soda(3))
print(soda(1))

def liquor(age,money):
	if (age >= 21) and (money >= 5):
		return "we're getting lit!"
	elif (age >= 21) and (money < 5):
		return "Not enough money, sir/ma'am!"
	elif (age < 21) and (money >= 5):
		return	"Nice try, under-aged person!"
	else:
		return "You're too poor and too young"
		
print(liquor(21,5))
print(liquor(21,4))
print(liquor(20,4))
print(liquor(45,10))

n_l() #new line

#lists
print("list have brakcets:")

movies = ["Constantine", "The Hangover", "X-men", "Predator"]

print(movies[0])
print(movies[0:2])
print(movies[1:]) #up to but not including
print(movies[:1]) #slice and we stop at 1 (technially 0)
print(movies[-1]) #-1 pull last item on list
print(len(movies))

movies.append("Jaws") #adds item to the end of list
print(movies)

movies.pop() #pop removes item from end of the list
print(movies)

movies.pop(1) #pop with number, removes selected item
print(movies)

movies = ["Constantine", "The Hangover", "X-men", "Predator"]
person = ["Jose", "Lee", "Louie", "Hank"]
combined = zip(movies, person) #zip combines lists
print(list(combined))

n_l()
#Tuples
#does not change is static
#does not have brackets, immutuable(?)
print("tuples have parentheses and cannot change")
grades = ("A", "B", "C", "D", "F")
print(grades[1]) 
n_l()

print("for loops - start to finish of iterate:")
fruits = ["apple", "banana", "orange"]
for x in fruits:
	print(x)

print("while loops - execute as long as true:")
i = 1
while i <= 10:
	print(i)
	i += 1
	









	
	














				






























