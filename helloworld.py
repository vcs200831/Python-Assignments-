# This is my first program
"""
print("Hello,World!")
print("Hello,Shekhar")

"""
from typing import List, Union

"""
x = 1 #int
y = 1.2 #float
z = 2j #complex

print(type(x))
print(type(y))
print(type(z))


#convert from int to float
a = float(x)
print(a)

#convert from float to int
b = int(y)
print(b)

#convert int to complex
c = complex(x)
print(c)

a = 40
b = 60
print(a)
print(b)
x = (a+b)
print(x)
y = (a-b)
print(y)
z = (a*b)
print(z)
p = (a/b)
print(p)
q = (a%b)
print(q)
r = (a**b)  # a^b
print(r)
s = (a//b)
print(s)

"""

# Common Errors in Python
# print "hello"

# l = [1,2,3]
# print(l[3])

# import notmodule

#d = {"1": "a", "2": "b"}
#print(d["3"])

#from math import cube

#it  = iter([1,2,3])
#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))

#"12" + 12

#int (abc)

#20/0

#name = input("enter your name")

# Program to print a statement "Hello,Darkness"
# print ("Hello,Darkness")

#x  = 10
#y = "Shekhar"
#print(x)
#print(y)

#x = 10
#x = 20
#print(x)

#x = int(10)
#y = float(10)
#z = str(10)
#print(x)
#print(y)
#print(z)

#print(type(x))
#print(type(y))
#print(type(z))

#x,y,z = "Mummy","Papa","Beta"
#print(x)
#print(y)
#print(z)

#x=y=z= "Family"
#print(x)
#print(y)
#print(z)


# x  = """ My name is
# V.Chandra Shekhar.
# I belongs to a middle class family.
# """
# print(x)

# x = "Hello,Shekhar"
# print(x[0])
# print(x[-1])
# print(x[5])

# for a in x:
#     print(a)

# print(len(x))
#
# x = "This is a book"
# print("a" in x)

# print(x[2:5])
# print(x[0:8])
# print(x[0:3])
# print(x[:13])
# print(x[:14])
# print(x[0:])
# print(x[-5:])
# print(x.upper()) # upper case
# print(x.lower()) #lower case
# print(x.strip()) #remove white spaces
# print(x.replace("book","chair"))

# x  = "Mummy"
# y  = "Papa"
# print(x+ " "+y)
#
# a = 10
# b = 10
# if a>b:
#     print("a is greater than b")
# elif a==b:
#     print("a and b are equal")
#
# def funccode1():
#     print("Hello,Shekhar")
# funccode1()
#
# def funccode2(x):
#     print(x+  " is the color ")
# funccode2("Red")
#
# def funccode2(x,y):
#     print(x+  " " +y)
# funccode2("Red","T-Shirt")
#
# #If we have two parameter then we have to pass two arguments otherwise we will get the typeerror
#
# numbers=[1,2,3,4,5,6,7,8]
# for a in numbers:
#     print(a)
#     if a==4:
#         break
#
# x = "Shekhar"
# for a in x:
#     print(a)
#     if a=="h":
#         break


# numbers=[1,2,3,4,5,6,7,8]
# for a in numbers:
#     # print(a)
#     if a == 4:
#         continue
#     print(a)
#
# for x in range(10,50):
#     print(x)
#
# i=2
# while i<10:
#     print(i)
#     i=i+1

# i=2
# while i<10:
#     print(i)
#     if i==4:
#        break
#     i=i+1

# i=2
# while i<10:
#     i = i + 1
#     if i==4:
#         continue
#     print(i)


# x='programmer'
# print(len(x))

# list  = ["Mummy", "Papa","Beta"]
# def P(x):
#     print(x*3)
# P(list)

#
# list  = ["Mummy", "Papa","Beta"]
# def P(x):
#     print(x*3)
# def P1(y,list):
#     for items in list:
#         y(items)
# P1(P,list)

# list = ["Shekhar","Mummy","Papa", 50,60.8,True]
# print(list)
# print(list[0])
# print(list[2:])
# print(list[-1])
# print(list[-5:])
# print(list[5:-1])
# print(len(list))
# list[3] = "Family"
# print(list)
# list.append("Sai Baba")
# print(list)
# list.insert(4,"Best Family")
# print(list)

# tuple = ("Shekhar","Mummy","Papa", 50,60.8,True)
# print(tuple)
# print(len(tuple))
# print(tuple[4])
# print(tuple[0:])
# print(tuple[-1])
# print(tuple[-5:])

# a = ("Shekhar","Mummy","Papa", 50,60.8,True)
# y= list(a)
# y[5] = "Smart Family"
# print(tuple(y))

# dict = {
#     "name": "shekhar" ,
#     "age" : 20 ,
#     "sex" : "male" ,
#     "vehicle" :"maruti suzuki" ,
#      "dob" : "26-6-2001",
#     "name" : "sonu"
# }
# print(dict)
# print(len(dict))
# x=dict["vehicle"]
# print(x)
# y=dict["age"]
# print(y)
# x=dict.get("name")
# print(x)
# dict["name"] = "shekhu"
# print(dict)
# dict.update({"vehicle":"skoda"})
# print(dict)
# dict["color"] = "Red"
# print(dict)
# dict.pop("color")
# print(dict)

# fruits=["apples","mangoes","oranges","kiwi","cherry","guava","watermelon"]
# newfruits=[]
# for x in fruits:
#     if "a" in x:
#         newfruits.append(x)
# print(newfruits)

# fruits=["apples","mangoes","oranges","kiwi","cherry","guava","watermelon"]
# newfruits=[x for x in fruits if "a" in x]
# print(newfruits)
#
# newfruits=[x for x in fruits if "i" in x]
# print(newfruits)
#
# newfruits=[x for x in range(10) if x<4]
# print(newfruits)

# newfruits =[x for x in fruits if x!="watermelon"]
# print(newfruits)
#
# newfruits=[x.upper() for x in fruits]
# print(newfruits)

# newfruits=[x  if x !="oranges" else "strawberry"  for x in fruits]
# print(newfruits)

# f=open("trial.txt","r")
# print(f.read())
# print(f.read(20))
# print(f.readline())
# print(f.readline(5))
# print(f.readline(5))

# for x in f:
#     print(x)
#
# f.close()

# f=open("trial.txt","a")
# f.write("my name is shekhar")
# f.close()
#
# f=open("trial.txt","r")
# print(f.read())

# f=open("trial.txt","w")
# f.write(" I am a software engineer")
# f.close()
#
# f=open("trial.txt","r")
# print(f.read())

# f=open("New.txt","x")


# import os
# # os.remove("New.txt")
#
# if os.path.exists("New.txt"):
#     os.remove("New.txt")
# else:
#     print("file not found")


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def methods(self):
#         print("Hi,My name is "+ self.name)
#
#
#
# P1 = Person("Shekhar",20)
# P2 = Person("Sonu",25)
# P1.methods()
# P2.methods()
# del P1
# print(P1.name)
# print(P1.age)


# num = int(input("Enter a number to check odd or even: "))
# def find_Evenodd(num):
#     if (num % 2 == 0):
#         print(num, " is an even")
#     else:
#         print(num, " is an odd")
# find_Evenodd(num)



# def prime(n):
#     count = 0
#     for i in range(1,n+1):
#         if n%i==0:
#             count=count+1
#     if count == 2:
#         return 1
#     else:
#         return 0
# n = int(input("Enter a number to check prime or not:"))
# z=prime(n)
#
# if(z==1):
#     print("prime number")
# else:
#     print("not a prime number")


# n=int(input("Enter a number:"))
# x=0
# y=1
# z=0
#
# while(z<=n):
#     print(z)
#     x=y
#     y=z
#     z=x+y

# x=lambda a:a+40
# print(x(10))
# x=lambda a,b,c:a+b+c+100
# print(x(10,10,10))
#
# def f1(n):
#     return lambda a:a*n
# doub=f1(2)
# trip=f1(3)
#
# print(doub(10))
# print(trip(11))
#
#
# def prime(x):
#     for n in range(2,x):
#         if x%n==0:
#             return False
#         else:
#             return True
#
# filtered=filter(prime,range(10))
# print("prime numbers are", list(filtered))
#
# def square(x):
#     return x*x
# numbers=[1,2,3,4,5]
# listsquare=map(square,numbers)
# print(list(listsquare))

# py -m pip --version
# py -m pip install camelcase
# py -m pip install --upgrade pip


# import camelcase
# x=camelcase.CamelCase()
# a="hi my name is shekhar"
# print(x.hump(a))

# import xlrd
# loc = ("D:\\New folder\\Passive_Candidates_05-02-2019.xlsx")
# wb=xlrd.open_workbook(loc)
# sheet=wb.sheet_by_index(0)
# print(sheet.cell_value(0,0))
# print(sheet.ncols)
# print(sheet.nrows)
# for i in range(sheet.ncols):
#     print(sheet.cell_value(0,i))
# print(sheet.row_values(1))



# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="shekhar@1234",
#    # database="pythonprogramming",
#     database="sakila",
# )
# print(mydb)
#
#
# mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE PythonProgramming")
#
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)
#
# mycursor=mydb.cursor()
# mycursor.execute("CREATE TABLE Customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)
#
# mycursor.execute("SELECT * FROM actor")
# # myresult=mycursor.fetchall()
# myresult=mycursor.fetchone()
# for x in myresult:
#     print(x)
# #dev.mysql.com - mysql documents


# tuple1=("car","bike","train")
# myit=iter(tuple1)
# print(next(myit))
# print(next(myit))
# print(next(myit))
#
# for x in tuple1:
#     print(x)


# class MyNumber:
#     def __iter__(self):
#         self.a=1
#         return self
#
#     def __next__(self):
#         x=self.a
#         self.a +=1
#         return x
#
# myclass=MyNumber()
# myiter=iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# import pickle
#
# mydict={"1":"a","2":"b"}
# pickle_file=open(pocklefile.txt,"wb")
# pickle.dump(mydict,pickle_file)
# pickle_file=open(pocklefile.txt,"rb")
# new_dict=pickle.load(pickle_file)
# print(new_dict)

# PythonJSON
# Get a list of name as an input from the user and make the first letters in caps and print each word as a list

# x = input("Enter a string")
# y = x.title()
# print("The output is ",y)

""""
Write a Python code to configure the MySQL Connector in your system
and Insert data to MySQL Table after which you Fetch 
and Display data from Table.

"""

# Write a Python code to reverse the given integer and print the integer
# i=int(input("Enter a number"))
# rev=0
# while(i>0):
#     rev=(rev*10) + i%10
#     i=i//10
# print("Reverse=",rev)

"""
Write a Python code to read an integer in a file e.g 123 
and convert it to words e.g One hundred and twenty three
and write the result back to the same file such that your 
file will have "123 One hundred and twenty three " in it
"""


def convertToDigit(n, suffix):
    # if `n` is zero
    if n == 0:
        return EMPTY

    # split `n` if it is more than 19
    if n > 19:
        return Y[n // 10] + X[n % 10] + suffix
    else:
        return X[n] + suffix

def convert(n):
    # add digits at ten million and hundred million place
    result = convertToDigit((n // 1000000000) % 100, "Billion, ")

    # add digits at ten million and hundred million place
    result += convertToDigit((n // 10000000) % 100, "Crore, ")

    # add digits at hundred thousand and one million place
    result += convertToDigit(((n // 100000) % 100), "Lakh, ")

    # add digits at thousand and tens thousand place
    result += convertToDigit(((n // 1000) % 100), "Thousand ")

    # add digit at hundred place
    result += convertToDigit(((n // 100) % 10), "Hundred ")

    if n > 100 and n % 100:
        result += "and "

    # add digits at ones and tens place
    result += convertToDigit((n % 100), "")

    return result


if __name__ == '__main__':
    EMPTY = ""

    X = [EMPTY, "One ", "Two ", "Three ", "Four ", "Five ", "Six ",
         "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
         "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
         "Seventeen ", "Eighteen ", "Nineteen "]

    Y = [EMPTY, EMPTY, "Twenty ", "Thirty ", "Forty ", "Fifty ",
         "Sixty ", "Seventy ", "Eighty ", "Ninety "]

    print(convert( 123))
