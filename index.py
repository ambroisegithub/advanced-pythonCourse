# print("hello world")
# python function syntax
# def <function name>(parameter):
#     <task completion>
# function example
# def sum(x,y):
#     return x + y
# add two number using function in python
# def sum (a,b):
#     return a + b
# print("sum =",sum(10,3))
# calculation in python
# width= 13
# length= 10
# print("area of rectengle is =",2*(width*length))
# def rectengleArea(width, length):
#     return (width*length)*2
# print("rectengleArea =",rectengleArea(30,10))
# four scope in python
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
list1 = [1,2,3,4,5]

list2=["a","b","c","d","e","f","g"] 
print(list2[3])
# list:is collection of element that sorted with the given order
# removing braces and comma(*listname)
# print(*list1)
print(list1)
print(list2, sep="  ")
print(len(list1))
# add an element to the end of the list
list1.insert(len(list1),6)
print(list1, sep=" ")
list1.append(7) 
print(list1,sep=" ")
list1.extend([8,9,10,11,12,13])
print(list1,sep=" ")
# remove element at last index
list1.pop()
print(list1,sep=" ")
# specify the element you want to remove
list1.pop(6)
print(list1,sep=" ")
# also you can specify index of element you want to remove
del list1[0]
print(list1,sep=" ")
# demostration of list using for loop or print all value of list
for x in list1:
    print("value :",x)
            