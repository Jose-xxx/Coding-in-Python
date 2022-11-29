#!/bin/python3

#importing   
print("Importing is important:")

import sys #systems function and parameters

from datetime import datetime
print(datetime.now())
 
from datetime import datetime as dt #importing with an alias/aka
print(dt.now())

def n_line():      #a funtion for creating space in the output
	print('\n')

n_line()	

print("after 'new line' function is defined")

#advanced strings

print("advanced strings:")
my_name = "Jose"
print(my_name[0]) #first initial
print(my_name[-1]) #last letter

sentence = "This is a sentence."

print(sentence[:4]) 	#first word
print(sentence[-9:-1]) #last word
print(sentence[-0])    #random check

n_line()

print(sentence.split()) #split the sentence by delimiter (space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))

n_line()

#funfact- if you play the video in .75 speed, Heath sounds tipsy. lol

quoteception = "I said, 'give me all the money'"
print(quoteception)

quoteception = "I said, \"give me all the money\""
print(quoteception)

print("A" in "Apple") #boolean returns "True"
letter = "a"
word = "Apple"
print(letter in word) #returns false because "a" is lowercase

print(letter.lower() in word.lower()) #improved - case insensitive

word_two = "Bingo"
print(letter.lower() in word.lower()) and not (letter.lower() in word_two.lower())

too_much_space = "                hello          " #new variable

#when using underscore, you are creating a variable

print(too_much_space.strip())

full_name = "ose xyz" #stings are immutable
print(full_name.replace("ose", "Jose"))
print(full_name.find("xyz")) #where my last name occurs in string
				#where that "x" lines up

movie = "The Matrix"
car = "Audi A7"
print("My favourite movie is {}.".format(movie)) #using a placeholder {}

print("Favorite car is an {}".format(car))
print("Favorite car is an {}".format(too_much_space))

def favorite_book(title, author):
	fav = "My favorite book is \"{}\", which is written by {}.".format(title, author)  #{} is the place holder
	return fav

print(favorite_book("Storm Front","Jim Butcher"))

#done with strings
n_line()

#dictionaries 
print("Dictionaries are keys and values:")
#[] for list () pulls {} Dictionaries 

juices = {"Fruit Punch" : 3, "Lemon": 6, "Peach": 4, "Apple": 2} #juice is key and price is value 
print(juices)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louie", "Ted"], "HR": ["Rick", "Morty"]}
print(employees)

employees["Legal"] = ["James Bond"] #add new key: value pair
print(employees)

employees.update({"Sales": ["Devin", "Chris"]})
print(employees)

#just realized code is read top to bottom, so even you update a variable, it will not show til after its used again in the output


juices["Fruit Punch"] = 4 #update price of fruit punch
print(juices)
 
print(juices.get("Lemon")) #getting price of one juice
print(juices.get("Melon"))  #getting price of non-listed juice
print(juices["Lemon"])	   #returns price too


#list and dictionaries
movies = ["Constantine", "The Hangover", "X-men", "Predator"]
person = ["Jose", "Lee", "Louie", "Hank"]
combined = zip(movies, person) #zip combines lists
movie_dictionary = {key: value for key, value in combined}

print(movie_dictionary)











































