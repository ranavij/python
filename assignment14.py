#Q.1) Write a python program to print the cube of each value of a list using list comprehension.
lst = [1,2,3,4]
lst_sq=[i**2 for i in lst]
print(lst_sq)

#Q.2)Write a python program to get all the prime numbers in a specific range using list comprehension.
a = int(input("Enter the range: "))
lst = [i for i in range(1,a) if all(i%y!=0 for y in range(2,i))]
print(lst)

#Q.3)Write the main differences between List Comprehension and Generator Expression.
#A List Comprehension is like the plain range function, executes immediately and returns a list.
#A Generator Expression returns and object that can be iterated over.
#The comparision is not perfect because in an object returned by the generator expression we cannot access an element by index.
#The difference between the two kinds of expressions is that the List comprehension is enclosed in square brackets [] while the Generator expression is enclosed in plain parentheses ()

#Q.4)Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
Celsius = [39.2, 36.5, 37.3, 37.8]
far=list(map(lambda x:(x*1.8)+32,Celsius))
print(far)

#Q.5)Apply an anonymous function to square all the elements of a list using map and lambda.
lst = [5,12,15,3,13]
lst_sq = list(map(lambda i: i*i,lst))
print(lst_sq)

#Q.6) Filter out all the primes from a list.
def isprime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
        else:
            return True


lst = [15,26,33,13,53,97,22]
a = list(filter(isprime, lst))
print(a)

#Q.7)Write a python program to multiply all the elements of a list using reduce.
lst = [5,50,15,20]
from functools import *

a = reduce(lambda x,y:x*y,lst)
print(a)
