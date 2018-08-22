print('list\n')
#Q.1- Create a list with user defined inputs.
l=[]
n=int(input("Enter how much integers you want in the list\n"))
print("Enter the elements")
for i in range(n):
    a=int(input())
    l.append(a)
print(l)


'''Q.2- Add the following list to above created list:
[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]'''
list1=['google','apple','facebook','microsoft','tesla']
l.extend(list1)
print(l)


#Q.3- Count the number of time an object occurs in a list.
l=[1,2,3,4,10,5,5,6,7,8,9,1,2,6,7,2]
print(l.count(2))


#Q.4- create a list with numbers and sort it in ascending order.
l1=[]
r=int(input("Enter how much integers you want in the list\n"))
print("Enter the elements")
for i in range(r):
    a=int(input())
    l1.append(a)
l1.sort()
print(l1)


'''Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order.
Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]'''
A=[1,0,2818,691,991]
B=[1,841,5,451,686]
A.sort()
B.sort()
A.extend(B)
print("Merged is:",A)
A.sort()
print("Sorted merged list is:",A)

'''Q.6- Count even and odd numbers in that list.'''
num=[23,24,18,33,49,86,69]
counto=0
counte=0
for i in num:
    if(i%2==0):
        counte+=1
    else:
        counto+=1
print("The list is: ",num)
print("The odd count is: " , counto)
print("The even count is: ",counte,"\n\n")

'''TUPLES
Q.1-Print a tuple in reverse order.
this part is not taught in class
Q.2-Find largest and smallest elements of a tuples.
this part is not taught in class'''

        #STRINGS
print('string\n')
#Q.1- Convert a string to uppercase.

s='hello world'
print(s.upper())


#Q.2- Print true if the string contains all numeric characters.

s1='1223334'
print(s1.isdigit())
print(s.isdigit())

#Q.3- Replace the word "World" with your name in the string "Hello World".

s=s.replace('world','raman')
print(s)

