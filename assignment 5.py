##ASSIGNMENT-5

#Question-1

year = int(input("Enter year:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("Leap Year")
else:
    print("Isn't a leap year")

#Question=2

length = int(input("Enter length "))
breadth = int(input("Enter breadth "))
if(length==breadth):
    print("It's a Square")
else:
    print("It's a Rectangle")

#Question-3

age1 = int(input("enter age of first person: "))
age2 = int(input("enter age of second person: "))
age3 = int(input("enter age of third person: "))
print("yungest person",min(age1,age2,age3))
print("oldest person",max(age1,age2,age3))


#Question-4

age = int(input("Enter Age: "))
sex = input("Enter sex(M or F): ")
m = input("Enter marital status ( Y or N): ")

if(sex == 'F'):
    print("She will work only in urban areas. ")
elif(sex == 'M' and age>19 and age<41):
    print("He can work Anywhere")
elif(sex == 'M' and age>39 and age<61) :
    print("He will work only in urban areas. ")
else:
    print("ERROR")

print("marital status ",m)

#Question-5

cost = int(input("Enter the cost "))
if(cost >= 1000):
    cost = cost-(0.1*cost)
    print("Now you have two pay %   rupees After discount "%(cost))
else:
    print(cost)


##--LOOPS

#question-1

for i in range(0,10):
    n=int(input("Enter integer: "))
    print(n)

#question-2

while(True):
    print("This is a infinite loop")

#question-3

n = int(input("enter the size: "))
l = []
for i in range(0, n):
    x = int(input())
    l.append(x)
list1 = []
for i in l:
    list1.append(i*i)
print("normal list ",l)
print ("squared list ",list1)


##Question-4

i=[]
s=[]
f=[]
l=[1,2,3,4,'a','b','c','d',9.00,1.00,8.786]
for i in l:
    if(type(i) is str):
        s.append(i)
    elif(type(i) is float ):
        f.append(i)
    elif(type(i) is int):
        i.append(i)
print("List of integer type is ",i)
print("List of float type is ",f)
print("List of string type is",s)

##Question--5
l=[]
for i in range(1,101):
    count=0
    for j in range(2, int(i/2)):
        if (i%j==0):
            count+=1
    if(count==0):
        l.append(i)
print(l)

##Question--6

for i in range(0, 5):
    for j in range(0, i+1):
        print("* ", end="")
    print()

##Question--7

n = int(input("enter the range "))
x=[]
for i in range(0,n):
    lst = int(input())
    x.append(lst)
t = int(input("Enter the number to search "))
pos = -1
for i in range(0,n):
    if x[i] == t:
        pos = i
        x.pop(pos)
        break
if pos == -1:
    print("Item not found.")
else:
    print("Item deleted.")
print (x)

