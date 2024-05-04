'''
Regular expressions(RegEx): RegEx is used for validating input
'''
import re 

a="sumanth"
print(re.search("sumanth",a))

b= "Sssumanth"
print(re.search("s+",b))

c= "ssumanth"
print(re.search("s*",c))

d= "sssumanth"
print(re.search("s?",d))

#e="SSS897sumanth"
#print(re.subn("\d", "*", e, 8))
#print(re.split("\s", e, 5))
