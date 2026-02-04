'''
Finding and fixing of errors is called Debugging
bug-->error
Types of errors:
1.Syntax Error  -->occurs when there is a mistake in the syntax of the code
2.Logical Error -->occurs when the code runs without error but produces incorrect results
3.Runtime Error -->occurs during the execution of the program

Debugging techniques:
1.Print()-->run the code line by line 
2.Using od pdb-->
3.try-except 

pdb-->python debugger
Purpose:
1.Pause the execution of code at certain point
2.Execute code line by line
3.Examine the values of variables at different stages of execution 

pdb commands:
n-->to get output in next line
p-->to print the value of variable
l-->to see the code
c-->to continue the execution until next breakpoint
s-->to step into a function
r-->to return from a function
h-->to see the help mat
q-->to quit the debugger


'''
''''
try:
    a=int(input("Enter a:"))
    print(10/a)
except ZeroDivisionError:
    print("can not divisible by zero")
except ValueError:
    print("invalid input")
'''

import pdb
def add(a,b):
    pdb.set_trace()
    return a+b
a=int(input("Enter a:"))
b=int(input("Enter b:"))      
print(add(a,b))