'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''

test='bob'
i=0
count=0
for letter in s[0:len(s)-(len(test)-1)]:
    if(s[i:i+len(test)]==test):
        count+=1
    i+=1
print 'Number of times {} occurs is:: {}'.format(test,count)
