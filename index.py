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
 
# ********************************************************************************************

# **********switch with match statement in python**********************************************

# http_status = 501

# if http_status == 200 or http_status == 201:
#     print("success")
# elif http_status == 400:
#     print("bad request")
# elif http_status == 404:
#     print("not found")
# elif http_status == 500 or http_status == 500:
#     print("internal or sever error")
# else:
#     print("unknown")
                
# match http_status:
#     case 200 | 201:
#         print("success")
#     case 500 | 501:
#         print("server error")
    # case _:
    #     print("unknown")  
    
#***********************************************************************************

# ************************loop for and while****************************************************************

# for i in range(10):
#     print("in range ..", i) 

# favourites = ["milk","beer","chees","chocollate","juice"]

# for item in favourites:
#     print("in my favourites ..", item) 

# while loop

# favourites = ["milk","beer","chees","chocollate","juice"]

# count = 0

# while count < len(favourites):
#     print("I like this meal",favourites[count])
#     count = count + 1


# print element with thier own index

# count = 0
# favourites = ["milk","beer","chees","chocollate","juice"]

# for idx, item in enumerate(favourites):
#     print(idx, favourites[count])
#     count = count + 1


#Starter Code
# favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

# for dessert in favorites:
#     if dessert == 'Pudding':
#         print('Yes one of my favorite desserts is', dessert) 
# else:
#     print('No sorry, that dessert is not on my list')

# ************************************************************************

# *********nested loop****************************************************

# outer looop


# for i in range(10):
#     # innner loop
#     for j in range(10):
#         print(0,end =" ")
#     print()  
    
#time complexity

# import time

# start_time = time.time()

# for i in range(10):
    # innner loop
#     for j in range(10):
#         print(0,end =" ")
#     print()  
# print(round((time.time()-start_time),2))

#*******************************************************************************

#***********file handling in python*********************************************

# files is used to store data so it is available for future or as a permanent record

# with open("a.txt","w") as file:
#    file.write("this is the first file") 

# display many lines
# with open("b.txt","a") as file:
#     file.writelines(["\nthis first line","\nthis is the second line"])


# add an exceptions

# try:
#     with open("files/b.txt","a") as file:
#         print("\nthis is the first line","\nthis is second line")
# except FileNotFoundError as e:
#     print("file or directory found",e)

# ****************************************************************************************

# ***************handling file in python**************************************************

#  read() functions

 
 
# with open("a.txt","r") as file:
    # data = file.readlines()
    # print(file.read(50))
    # print(file.readlines())
    #  print(file.readline())
    
    # for x in data:
    #     print(x)
    
    # OR
    
    # for x in file:
    #     print(x)
    
    
    # ******************************************************************************
    # *****************procedural and module in python******************************
    
    # procedural and modules in python are used to organize the group of statements and reuse of codes
    #  DRY:don't repeat yourself
    
    
    # ******************************************************************************************
    # algorithm in python
    # palindrome 
    
    # rececar
    
    # [0]==[6]
    # [1]==[5]
    # [2]==[4]
    
    # algorithm for a palindrome
 
# def isParindlome(str):
#         startIndex =0
#         endIndex = len(str) - 1
        
#         for x in str:
#             if str[startIndex] != str[endIndex]:
#                 return False
#         return True

# print(isParindlome("umuvumu"))    


# *******************************************************************************

# ********pure function in python************************************************

# pure fuction include list

# my_list = [1,2,3,4,5,6]

# def add_to_list(list, item):
#     nl = list.copy()
#     nl.append(item)
#     return nl


# new_list = add_to_list(my_list, 7)

# print(my_list)

# print(new_list)


# ****************************************************************************

#************************ recursion im python*********************************

# # factorial in python

# def factorial(number):
#     if number < 0:
#         return 0
#     else:
#         fact = 1
#         for item in range(1,number + 1):
#             fact = fact * item
#         return fact
# print(factorial(5))              

# by using recursive function

# def find_factorial(number):
#     if number == 1:
#         return 1
#     else:
#         return number * find_factorial(number -1)
# print(find_factorial(1))  

# ************************************************************************

# ******************reverse string in python******************************

# first way:
# str[start:stop:step]

# trial = "reversal"
# new_trial = trial[::-1]
# print(new_trial)  

# def string_reverse(str):
#     if len(str)== 0:
#         return str
#     else:
#         return string_reverse(str[1:]) + str[0]

# str = "ambroise"
# reverse = string_reverse(str)
# print(reverse)

# *********************************************************************************
#  ***********************************map and  filter function*********************
menu = ['cloude','peffe','simon','celin','clelly']

def find(chocollate):
    if  chocollate[0] == 'c':
        return chocollate 
# map_chocollate = map(find,menu)
# print(map_chocollate)
# for x in map_chocollate:
#     print(x)



# map_chocollate = filter(find,menu)
# print(map_chocollate)
# for x in map_chocollate:
#     print(x)

# oop in python
# ******************************************************************************************

# ***************************instantiate a custom object*************************************

# class Recipe():
#     def __init__(self,dish,items,time)-> None:
#         self.dish = dish
#         self.items = items
#         self.time = time
        
#     def contents(self):
#         print("The" + self.dish + "has" + str(self.items)+ \
#             "and takes" + str(self.time) + "min to prepare")
 
# pizza = Recipe("pizza",["cheese", "bread","tomato"],45)
# paste = Recipe("paste",["penne", "suace"],55)

# print(pizza.items)
# print(paste.items) 


#instance of class

# class Payslips:
#     def __init__(self,name,payment,amount) -> None:
#         self.name = name
#         self.payment = payment
#         self.amount = amount
#     def pay(self):
#         self.payment ="yes"
#     def status(self):
#         if self.payment == "yes":
#             return self.name + " is paid " + str(self.amount) 
#         else:
#             return self.name + " is not paid yet " + str(self.amount)
# ambroise = Payslips("Ambroise","no", 10000) 
# muhayimana = Payslips("Muhayimana","no", 30000) 
# print(ambroise.status(),"\n",muhayimana.status()) 

# ambroise.pay()
# print("after payment") 

# print(ambroise.status(),"\n",muhayimana.status()) 

#*******************************************************************************************************
 
# inheritance in class

# class Employees:
#     def __init__(self,name,last)-> None:
#         self.name = name
#         self.last = last

# class Supervisors(Employees): 
#     def __init__(self, name, last,password) -> None:
#         super().__init__(name, last) 
#         self.password = password

# class Chefs(Employees):
#     def leave_request(self,days):
#         return "May I take "  + str(days) + " days"

# muhayimana = Supervisors("Muhayimana","M","apple")
# ambroise = Chefs("Ambroise","A") 
# shakur =Chefs("Shakur","S ")  

# print(ambroise.leave_request(3))
# print(muhayimana.password) 
# print(ambroise.name)             

# ***********************************************************************************************************            #    
               
#*************************************abstract classs*************************************    
           
           
# ****************************************************************************************************

# ************module in python*******************************

# import sys

# locations = sys.path
# print(locations)
# for i in locations:
#     print(i)


# import calendar

# leapdays  = calendar.leapdays(2000,2050)

# print(leapdays)

# isitleap = calendar.isleap(2040)

# print(isitleap)

# ***********************************************************************************

# *********************reload function module*******************************


# **************************************************************************************
#********************************** PyTest in python**********************************************************************
# a testing framework allowing users to write test codes that use the Python programming language



# *************************************************************************************************************************

# ****************questions and answer about file handling in python****************************************



# 1. Complete the `read_file()` function to read in the sampletext.txt file using the `open` function and return the entire contents of the file. 

# 2. Complete the `read_file_into_line()` function so that it returns a data structure of all the contents of the file in a line-by-line sequential order.

# 3. Fill in the `write_first_line_to_file()` that accepts two arguments. This should write only the first line of the file contents into the given output file.   

#     - **Argument 1:** The contents of a file to be written
#     - **Argument 2:** The name of an output file.
# <br><br>


# 4. Complete the `read_even_numbered_lines()` to return a list of the even-numbered lines of a file (2, 4, 6, etc.) 

# 5. Fill in the `read_file_in_reverse()` function to return a list of the lines of a file in reverse order. 


# by follow the above instruction answer below question

# def read_file(file_name):
    """ Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ### WRITE SOLUTION HERE
    
    # raise NotImplementedError()

# def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE

#     raise NotImplementedError()

# def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE

#     raise NotImplementedError()


# def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    ### WRITE SOLUTION HERE

#     raise NotImplementedError()

# def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE

    # raise NotImplementedError()

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
# def main():
#     file_contents = read_file("sampletext.txt")
    # print(read_file_into_list("sampletext.txt"))
    # write_first_line_to_file(file_contents, "online.txt")
    # print(read_even_numbered_lines("sampletext.txt"))
    # print(read_file_in_reverse("sampletext.txt"))

# if __name__ == "__main__":
#     main()


# def read_file(file_name):


""" Reads in a file.

    1. Open and read the given file into a variable using the File read() function
    2. Print the contents of the file
    3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
#     with open(file_name, 'r') as f:
#         contents = f.read()
#         print(contents)
#         return contents


# def read_file_into_list(file_name):

""" Reads in a file and stores each line as an element in a list

    1. Open the given file
    2. Read the file line by line and append each line to a list
    3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
#     with open(file_name, 'r') as f:
#         lines = f.readlines()
#         return lines


# def write_first_line_to_file(file_contents, output_filename):
""" Writes the first line of a string to a file.

    1. Get the first line of file_contents
    2. Use the File write() function to write the first line into a file
       with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
#     with open(output_filename, 'w') as f:
#         f.write(file_contents.split('\n')[0])


# def read_even_numbered_lines(file_name):
""" Reads in the even numbered lines of a file

    1. Open and read the given file into a variable
    2. Read the file line-by-line and add the even-numbered lines to a list
    3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
#     with open(file_name, 'r') as f:
#         lines = f.readlines()
#         even_lines = [lines[i] for i in range(1, len(lines), 2)]
#         return even_lines


# def read_file_in_reverse(file_name):
""" Reads a file and returns a list of the lines in reverse order

    1. Open and read the given file into a variable
    2. Read the file line-by-line and store the lines in a list in reverse order
    3. Print the list
    4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
#     with open(file_name, 'r') as f:
#         lines = f.readlines()
#         lines.reverse()
#         print(lines)
#         return lines


# def main():
#     file_contents = read_file("sampletext.txt")
    # print(read_file_into_list("sampletext.txt"))
    # write_first_line_to_file(file_contents, "online.txt")
    # print(read_even_numbered_lines("sampletext.txt"))
    # print(read_file_in_reverse("sampletext.txt"))


# if __name__ == "__main__":
#     main()

