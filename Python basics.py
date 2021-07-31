# this is a comment

# numerical data types
# integer 
# 1890
# 5
# 1
 
# float
# 1. #1.0
# 3.14
# 2.536

# complex
# 1 + 3j

# boolean
# True
# False
# 2 > 4 # False

# strings - Character values, declared in single or double quotes 
# 'Hello World!'
# "1" # not the number 1, instead this represents the character "1"

# collections - a collections of values 
# list - a collection of values in a specific order 
# [1, 2, 3, 'a']

# tuple - a collection of values in a specific order but immutable(can't be changed)
# (2, 5, 8, 'a') 

# set - a collection of values unordered and does not allow duplicates 
# {1, 2, 3}
# {1, 2, 2, 2, 'a'} # this is same as {1, 2, 'a}

# dictionary - a collection of unordered key, value pairs
# {1: 'a', 2: 'b', 3: 'c'}

# operators 

# variables - "case sensitive"

# conditionals - if, else, elif, nested if 

# eg :
 
# folklore_rating = float(input('How do you rate folklore?'))

# print('What to do with folklore?')

# if folklore_rating > 7 :
#    print('lisiten on repeat')
#    print('share on social media')
#    print('obsess about it')
# elif folklore rating > 5:
#    print('Talk to t swift fans')
# else:
#     print('did you make a mistake in the rating?')

# print('<3 t swift')

# conditional

# condition = ''

# if condition:
#    print('executed')
# else: 
#     print('not executed')
# ans: not executed 
# some num or content - executed 

# loops  
# while loop

# i = 1 
# while i < 5:
#    print(i)
#    i += 1 # i = i + 1 
# print('the end')

# output 1
#        2
#        3
#        4
#        the end 

# for loop

# name = ['Subscribe', 'to', 'Akshita', 'K']
# for letter in name :
#    print(letter) # can also write x instead of letter

# nested loops

# adjs = {'shiny','pink','clear'}
# nouns = {'coin','speaker','iphone'}

# for adj in adjs:
#     for noun in nouns:
#        print(adj, noun)

# Output:shiny cion
#        shiny speaker
#        shiny iphone
#        pink coin
#        pink speaker
#        pink iphone
#        clear coin
#        clear speaker 
#        clear iphone

# control flow 

#1. break
#2. continue

# word_list = ['Subscribe', 'to', 'Akshita', 'K']
# for name in word_list:
#    print(name)
#   if name == 'Akshita':
#        break
# print('the end')

# break

# i = 5
# while i < 5:
#    print(i)
#   if i == 3:
#        break
# print('the end')

# output : 1
#          2
#          3
#          the end

# continue

#word_list = ['Subscribe', 'to', 'Akshita', 'K']
#for name in word_list:
#     if name == 'Akshita':
#         continue
#     print(name)
#print('the end')

# functions

# def dexter(mood):
    # code here gets executed when you call the function
#    print(mood)
#    if mood == 'happy':
#        print('bow bow')
#    else:
#        print('*whimper*')

# dexter('sad')

# scope of function, the variable defined within a function will stay inside the paranthesis. In a function the number of\
#  arguments that you pass in has to equal the number of parameters that are defined within in the paranthesis, when you actually create the function.

# default parameters

# def dexter(mood='happy'):
    # code here gets executed when you call the function
#    print(mood)
#    if mood == 'happy':
#        print('bow bow')
#    else:
#        print('*whimper*')
#print('first time')
#dexter()
#print('\nsecond time')
#dexter('sad')

# return 

# def add_one(x):
#    print(x+1)
#    return x + 1

# y = add_one(5) # 6
# print(y)

# define a classe, initialization of object and adding a method in a class(function)

# class Beach:

#        def __init__(self, location, water_color, temperature):
#            self.location = location
#            self.water_color = water_color
#            self.temperature = temperature
#            self.heat_rating = 'hot' if temperature > 80 else 'cool'
#            self.parts = ['water','sand'] # class variable 
    
#        def add_part(self, part):
#            self.parts.append(part)
# def main():
#    cape_cod_beach = Beach('cape_cod', 'dark blue', 70)
#    cancun_beach = Beach('Cancun', 'crystal blue', 90)
#    cape_cod_beach.add_part('rock')
#    la_beach = Beach('LA','turquoise', 85)
#    italy_beach = Beach('Italy','blue', 82)
#    italy_beach.add_part('rock')
#    hot_not_rocky = []
#    for beach in [cape_cod_beach, cancun_beach, la_beach, italy_beach]:
#        if beach.heat_rating == 'hot' and 'rock' not in beach.parts:
#            hot_not_rocky.append(beach)
#
#    return hot_not_rocky

# if __name__ == '__main__':
#    beaches = main()
#    print([beach.location for beach in beaches])

# Inheritance 
# 1. child class
# 2. parent class 
# Multiple inheritance

# class Dog:
#     def __init__(self, name, age, friendliness):
#        self.name = name
#        self.age = age
#        self.friendliness = friendliness
    
#    def likes_walks(self):
#        return True

#    def bark(self):
#        return 'Woof!'

# class Samoyed(Dog):
#    def __init__(self, name, age, friendliness):
#        super().__init__(name, age, friendliness)

#    def bark(self):
#            return 'Arf arf!'

# class Poodle(Dog):
#    def __init__(self, name, age, friendliness):
#        super().__init__(name, age, friendliness)

#    def shedding_amount(self):
#        return 0

# class GoldenRetriever(Dog):
#    def __init__(self, name, age, friendliness):
#        super().__init__(name, age, friendliness)

#    def fetch_ability(self):
#        if self.age < 2:
#            return 8
#        elif self.age < 10:
#            return 10
#        else:
#            return 7

# class GoldenDoodle(Poodle, GoldenRetriever):
#    def __init__(self, name, age, friendliness):
#        super().__init__(name, age, friendliness)

#    def bark(self):
#        return 'AROOOO!'

# sammy = Samoyed('Sammy', 2, 10)
# goldie = GoldenDoodle('Goldie', 1, 10)
# generic_doggo = Dog('Gene', 10, 10)
# print(goldie.bark())
# print(sammy.bark())
# print(generic_doggo.bark())
 

# Polymorphism 

# from oops point of view, the child  class can overwrite the function and setup a new function
