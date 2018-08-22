#Q.1- Reverse the whole list using list methods.
l=[1,2,3,4,5]
l.reverse()
print("reverse list",l)

#Q.2- Print all the uppercase letters from a string.
s=input("enter the sting to check upper case \n")
for x in s:
    if x.isupper():
        print(x)
#else:
    #print("no uppercase found")
        
#Q.3- Split the user input on comma's and store the values in a list as integers.

i=input("enter the input ")
list=[]
list1=i.split(",")
print(list1)
for n in list1:
    a=int(n)
    list.append(a)
print(list)
print(type(list))
        
#Q.4- Check whether a string is palindromic or not.
    
l=input("enter the number to check palindrom ")
l2=l[::-1]
if l==l2:
    print ('palindrome')
else:
    print('Not palindrome')

    
#Q.5- Make a deepcopy of a list and write the difference
        #between shallow copy and deep copy.

import copy as c
list1 = [1, 2, [3,5], 4]
list2 = c.deepcopy(list1)
print ("Before deep copying")
print("list1 = ",list1)
print("list2 = ",list2)
list2[2][1] = 125
print ("After deep copying in list2")
print(list2)
print ("After deep copying in list1")
print(list1)
print('\r')

#diff between deep and shallow copy:
#1. In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.
#  In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.
#2.In python, this is implemented using “deepcopy()” function.
#   In python, this is implemented using “copy()” function.
