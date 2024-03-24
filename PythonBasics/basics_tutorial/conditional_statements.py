'''
Created on 10-Mar-2024
Conditional statements
1.if statement
2.if else statement
3.series if else statement
4.nesed if else statement

-Logical operators in conditional statements
@author: Intel
'''
age=int(input("Please enter your age:"))
'''
if age>=13:
    print("Allow inside")
else:
    print("push them out") 
'''
'''
if age>18:
    print("You are an adult") 
elif age>=13:
    print("You are a teenager")
else:
    print("You are a child")
'''  
'''      
if age>13:
    if age>18:
        if age>60:
            print("You are a senior citizen")
        else:    
            print("You are an adult")
    else:
        print("You are a teenager")
else: 
    print("You are a child")              
print("Program stopped")
'''
if age>=13 and age<=18:
    print("You are a teenager")
else:
    print("You are not a teenager")    

