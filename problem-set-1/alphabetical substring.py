'''
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
'''

a=[]
string=""
i=0
check = list(s)
for letter in list(s[0:len(s)-1]):
    if check[i]<=check[i+1]:
        string = string+check[i]
    else:
        a.append(string+check[i])
        string=""
    i+=1
a.append(string+check[i])
max_string = max(len(str(x)) for x in a)
for sub in a:
    if len(sub)==max_string:
        print "Longest substring in alphabetical order is:{}".format(sub)
        break
