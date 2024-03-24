'''
Created on 21-Mar-2024
list:
1. We can create an empty list
2. List is heterogenous (opp. homogenous)
3. Accessing elements from the list:
   a. By using Index
   b. By using Slicing operator
   c. By using Loops
   
   Index: Position value of any element present in the list
   
   from left to right -->0, 1, 2....
   from right to left -->-1, -2, -3.....
   
   syntax: list name[] -->common for all data structures
   
4. list is mutable
5. list store duplicate value
6. Insert order is preserved- list will not sort elements by 
   
   syntax: list name[] -->common for all data structures
@author: Intel 
'''
from itertools import repeat
'''
a=[] # we can create an empty list
print("a", type(a))
print("a", a)

b=[1, 2, 3, "Sumanth", "Sravani", 3.5, True, 3.5j]# list is heterogenous
print("b", b)

c=list(range(2, 21, 2)) # tuple, set
print("c list before modifying", c)
# print(c[6])
# print(c[-6])
c[6]=15
print("c list after modifying", c)

d=[1, 2, 3, 3, 4, 5, 6, 6]
print("d", d)

e=[5, 7, 5, 6, 4, 1, 3, 2, 8]
print("e", e)

for i in e:
    print(i)
'''
c=list(range(2, 21, 2)) 
print("c-->", c)
d=[1, 2, 3, 4]
print("d-->", d)


c.append(56) # append value
print("c after appending 56-->", c)  
print(c)


c.append(d) 
print("c after appending 56-->", c)  
print(c)

print(c[10])
print(c[11])

c.extend(d)
print("c after extending with d-->")
print(c)

# c.clear(
# print(c)

e=c.copy()
print("e-->", e)

print(c.index(4, 2))

c.insert(9, 100)
print(c)

print(c.pop(8))
print(c)

print(c.pop())
print(c)

c.remove(56)
print(c)

c.reverse()
print(c)

#c.sort()
#print(c)

print(c.count(100))

print(len(c))




    
      