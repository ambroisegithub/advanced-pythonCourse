# print("hello world")


#*********************** python function syntax
# def <function name>(parameter):
#     <task completion>
# function example
# def sum(x,y):
#     return x + y
# add two number using function in python
# def sum (a,b):
#     return a + b
# print("sum =",sum(10,3))

# **************************************************************************


# ************calculation in python
# width= 13
# length= 10
# print("area of rectengle is =",2*(width*length))
# def rectengleArea(width, length):
#     return (width*length)*2
# print("rectengleArea =",rectengleArea(30,10))

# **********************************************************************************


# **************four scope in python
# built-in Scope
# global scope:
# enclosing Scope
# local Scope
# LEGB
# myglobalScope =30
# def fn1():
    
#     enclosedScope=20
    
#     def fn2():
        
#         mylocalScope=20
#         print("myglobalScope =",myglobalScope)
#         print("enclosedScope =",enclosedScope)
#         print("mylocalScope =",mylocalScope)
        
        
#     fn2()
    
# fn1()
# list in python
# list1 = [1,2,3,4,5]

# list2=["a","b","c","d","e","f","g"] 
# print(list2[3])

# *****************************************************************************


#********************* list:is collection of element that sorted with the given order
# removing braces and comma(*listname)
# print(*list1)
# print(list1)
# print(list2, sep="  ")
# print(len(list1))
# add an element to the end of the list
# list1.insert(len(list1),6)
# print(list1, sep=" ")
# list1.append(7) 
# print(list1,sep=" ")
# list1.extend([8,9,10,11,12,13])
# print(list1,sep=" ")
# remove element at last index
# list1.pop()
# print(list1,sep=" ")
# specify the element you want to remove
# list1.pop(6)
# print(list1,sep=" ")
# also you can specify index of element you want to remove
# del list1[0]
# print(list1,sep=" ")
# demostration of list using for loop or print all value of list
# for x in list1:
#     print("value :",x)

# *********************************************************************************************************



# *********tupple in python:tuple is static list
# my_tuples =(1,"string",4.5,True) 
# my_tuple1 =(1,"string",4.5,True) 
# print(my_tuples)           
# print(my_tuple1) 
# print(my_tuples.count)
# print(type(my_tuples)) 
# print(my_tuples.count) 
# print(my_tuples.index("string"))
# for x in my_tuples:
#     print(x)


# **************************************************************

# *********************set in python***********************************


# set1 = {1,2,3,4,5,6,7,8,9,9} #here the set does don't change when we have duplicate elements

# set2 = {1,2,3,4,5,6,7,8,9}
# set3 ={"a","b","c","d","e","f"} 

# print(set1)
# print(set2)

# some methods used in set2 are

# add some content to set1

# set1.add(10)

# remove some content

# set2.remove(1)
# set1.discard("b") 

#swap with last element
# print(set1)

# print(set2)

# print(set3)

# combine two sets

# set4 =set1.union(set3)

# print(set4)

# for x in set4:
#     print(x) 
#intersection between two sets
# print(set1.intersection(set2)) 
# print(set1 & (set2)) 
# print(set1.difference(set2)) 

#******************************************************************************

#********** dictionary in python*********************************************
# key:value
# sample_dictionary = {1:'coffee',2:'Tea',3:'juice'}
# print(sample_dictionary)
# print(sample_dictionary[1])

# delete element from dictionary


# del sample_dictionary[3]
# print(sample_dictionary)

# dictionary operation  functions

# dict2 = type(sample_dictionary)

# dict3 = {}
# print(dict2)
# print(type(dict3))

# add element to dictionary

# sample_dictionary[3]='milk'

# print(sample_dictionary)

# replace element with other

# sample_dictionary[1]='cheez'

# print(sample_dictionary)

# for loop we use key and value to

# for key, value in sample_dictionary.items():
#     print(str(key) + " : " + value)


# *********************************************************************


# ****************************Args and kwargs***********************************

#args 

# def sum1(*args):
#     sum = 0
#     for x in args: 
#         sum +=x
#     return sum    
# print("sum = ",sum1(1,3,4,5,6) )

# kwargs


# def sum1(**kwargs):
#     sum = 0
#     for k, v in kwargs.items(): 
#         sum +=v
#     return round(sum,2)    
# print("sum = ",sum1(coffe=1.333, cake=3.222, milk=33.33) )


# *******************************************************************************************


# *********python input***************************

# input in python string

# str1 = input("please enter your first name :")
# str2 = input("please enter your second name :")

# print("heloo " + str1  + ' ' + str2)

# input in python integer


# number1 = input("please enter your first number :")
# number1 = input("please enter your second number :")

# print( int(number1)  + int(number1))

# exercise 1


#type casting in python 


# name = str(input('What is your name? '))

# print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

# age = int(input('What is your age? '))

# print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# height = float(input('What is your height in meters? '))

# print(f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# loyalty = bool(input('Are you part of our loyalty program? '))

# print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")


# exercise 2

# The below script will ask for 3 inputs. Each input will be based
# on the price of the items - the price is determined by you. The output
# should print the total of the 3 inputs rounded to 2 decimal places e.g
#
#   1 coffee @ $ 2.00
#   1 sandwich @ $ 4.99
#   1 cake @ $ 2.75
#
#   Your total bill is $ 9.74

# Modify the line below
# coffee = float(input('1 coffee @: $ '))

# Modify the line below
# sandwich = float(input('1 sandwich @: $ '))

# Modify the line below
# cake = float(input('1 cake @: $ '))

# bill_total = coffee + sandwich + cake

# print('Your total bill is $', round(bill_total,2))

# *****************************************************************
# **********math and logical operation*****************************


# math

# print(2-1)
# print(2+1)
# print(2/1)
# print(2*1)

# logical operation

# or

# a = True
# b = False
# if a or b :
#     print("one from both are false")


#and 

# a = True
# b = True
# if a and b :
#     print("All are true")
    
    
#not

# a = True
# b = False
# if not(a) and not(b) :
#     print("All are true")

# ******************************************************

# ***********control flow in pyhon***********************

# if else 

# totlalPay = 900
# discount = 10

# if totlalPay > 900:
#     print("the price is greater 1000")
#     totlalPay = totlalPay-discount
# else:
#     print("the price is less 1000")    
# print("the total pay is " + str(totlalPay))  


# nested if statement


# totalPay = 1200
# discount = 10
# newpay = totalPay - discount
# if totalPay > 500 and totalPay < 1000:
#     print("the price is greater is well")
# elif totalPay >100 and totalPay <500:
#     print("the price is not well") 
# else:
#     print("unstable price") 
          
# print("the total pay is " + str(newpay))    
    
 
# loyalty_customer = True
# total_bill = 124

# if loyalty_customer and total_bill > 100:
    #give 20% discount
#     total_bill = total_bill - (float(total_bill)/ 100) * 20
# elif total_bill > 100:
    #give 10% discount
#     total_bill = total_bill - (float(total_bill)/ 100) * 10
# else:
    #sorry no discount, 5% service charge applied.
#     print('Sorry, no discount ...')

# print('Total Bill: ', float(total_bill))
 
