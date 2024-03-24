'''
Created on 14-Mar-2024
Looping statements: to execute any code repeatedly 
1.While loop: executes code repeatedly until condition fulfilled(as long as condition is satisfied)
  a.initialization of conditional variable
  b.Define loop with the condition
  c.Increment/decrement section
2.For loop: executes a code repeatedly based on the sequence or range provided

Loop control statements:
1.break
2.continue(skip)            
            

           

@author: Intel
'''
'''
count=1
while count<=5:
    print("Hello, world!")
    count=count+1
'''
'''
count=1
while count<=5:
    #print("count<=5)
    print(count) 
    if count==150:
        break
    count=count+1   
'''

'''    
for count in range(5):
    print("Hello, world!")
'''  
  
'''    
for i in range(1, 20, 2):
    print(i)
'''

'''
for i in "sumanth":
    print(i)
'''

''' 
for i in "sumanth":
    print(i)
    if i=="n":
       break    
'''
'''
for i in "sumanth":
    if i=="n":
        continue
    print(i)
   # if i=="n":
   #    break 
'''
'''
count=1
while count<=200:
    if count==100:
        count=count+1
        continue
    print(count)
    count=count+1
'''   
''' 
*
**
***
****
*****

   * 
  *** 
 *****
*******

*******
******
*****
****
***
**
*

*******
 *****
  ***
   *
   
*
**
***
****
*****  
******
*****
****
***
**
*

*****
****
***
**
*
*
**
***
****
*****

'''
   
'''
for i in range(5): # row
    for j in range (i+1): # column
        print("*", end="")
    print()   
'''
'''
for i in range(5):
    for j in range(5-i):
        print("*", end="")
    print()
'''

       
     
   
 
    


