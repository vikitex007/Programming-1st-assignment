#Q.No.1
a = input("Enter value for a:") #taking value from user for a and b
b = input("Enter value for b:") 
x=int(a) #user le deko value integer hunako lagi int thapeko
y=int(b)
if a==b:
    print('1')
elif a>b:
    print('2')
else:
    print('3')
'''
#Q.No.2
if A == B or c == d:      
    print("Hello") 
#Q.No.3
if A == B and c == d:
    print('Hello')
'''
#Q.No.4
x = float(input("Enter a number:"))  #user bata input leko float number ni huna sakxa so float haleko
if x > 0:
    print('Positive Number')    
elif x==0:
    print('Zero')
else:
    print('Negative Number')

#Q.No.5
Number = int(input("Enter your number:"))
if Number % 2 == 0 :
    print("Even Number")
else :
    print("Odd number")
#Q.no.6
sub1 = float(input("Enter your Engish marks:"))
sub2 = float(input("Enter your Math marks:"))
sub3 = float(input("Enter your programming marks:"))
sub4 = float(input("Enter your Software design marks:"))
Totalmarks = (sub1 + sub2 + sub3 + sub4)
print("Your total marks is:",Totalmarks)
per = (Totalmarks)/400*100
print("your percentage is:",per)
if per >70 and per <= 100:
    print("Distinction")
elif per >60 and per <=69 :
    print("First")
elif per >= 40 and per <= 59:
    print("Second")
elif per < 40:
    print("Fail")
else:
    print("invalid number")
#Q.No.7
print ('APPLE' > 'apple') #false 
#Q.no.8

def personal_details():
    name, age = "Sachin", 20
    address = "Matatirtha, Chandragiri"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
personal_details()
#Q.no.9
Rad = float(input("Enter radius of circle:"))
formula = (22/7)*Rad**2
print("The area of circle is:",formula)
#Q.no.12

a=int(input("Enter your number:"))
b=int(input("Enter your number:"))
c=int(input("Enter your number:"))
if a>c and c>b:
    print("The smallest number is:",b)
elif a>b and b>c:
    print("The smallest number is:",c)
elif c>b and b>a:
    print("The smallest number is:",a)
else:
    print("Invalid  number")
#q.no.14
List = [1,2,3,4,5]
print (5 in List)
#Q.no.15
Num = int(input("Enter number from 1 to 12:"))
if Num == 1:
    print("January")
elif Num == 2:
    print("February")
elif Num == 3:
    print("March")
elif Num == 4:
    print("April")
elif Num == 5:
    print("May")
elif Num == 6:
    print("June")
elif Num == 7:
    print("July")
elif Num == 8:
    print("August")
elif Num == 9:
    print("September")
elif Num == 10:
    print("October")
elif Num == 11:
    print("November")
elif Num == 12:
    print("December")
else:
    print("Invalid number")
#Q.no.16
x = 5
print (x)
x+=3
print(x)
#Q.no.17

 #Q.NO.18
Ram = int(input("Enter your age:"))
Shyam = int(input("Enter your age:"))
Gita = int(input("Enter your age:"))

if Ram > Shyam and  Ram > Gita:
    print("Ram is oldest")
elif Shyam > Ram and Shyam > Gita:
    print("Shyam is oldest")
else:
    print("Gita is oldest")
if Ram < Shyam and Ram < Gita:
    print("Ram is youngest")
elif Shyam < Ram and Shyam < Gita:
    print("Shyam is youngest")
else:
    print("Gita is youngest")

#Q.No.19
Age = int(input("Enter your age:"))
if Age >= 18:
    print("You are eligible for voting \nThank you!")
else :
    print("Sorry, you are not eligible for voting \nThank you")

#Q.No.20
Num = int(input("Enter your number:"))
if Num % 7==0 :
    print("Your number is divisible by 7")
else:
    print("Your number is not divisible by 7")

#Q.no.21

city = input ("Enter your city name:")
if city == 'Delhi':
    print ("Your monument is: Red Fort ")
elif city == 'Agra':
     print ("Your monument is: Taj Mahal ")
elif city == 'Jaipur':
     print ("Your monument is: Jal Mahal ")
else:
    print("Enter a valid city")

#Q.no.22
Num = int(input("Enter your number:"))
if Num % 2==0 and Num % 3 == 0:
    print("Your number is divisible by both 2 and 3")
else :
    print("Your number is not divisible by 2 and 3")
#Q.no.23 
a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
print("1.+ , 2.- , 3.* , 4./")
operator = int(input("choose operator :"))

if (operator == 1):
    print ("Addition of {} and {} is {}".format(a,b,a+b))
elif (operator == 2):
    print ("Substraction of {} and {} is {}".format(a,b,a-b))
elif (operator == 3):
    print ("Multiplication of {} and {} is {}".format(a,b,a*b))
elif (operator == 4):
    print ("Division of {} and {} is {}".format(a,b,a/b))
else:
    print("operator error")

#Q.no.24
'''
if test expression:
    statement(s)
Here,the program evaluates the test expression and will execute statement(s) only if the test expression is True.

If the test expression is False, the statement(s) is not executed.

In Python, the body of the if statement is indicated by the indentation. The body starts with an indentation and the first unindented line marks the end.

Python interprets non-zero values as True. None and 0 are interpreted as False
'''
#Q.no.25
num = int(input("Enter your number:"))
if num % 5 == 0:
    print("Hello")
else:
    print("Bye")
#Q.no.26
print("Select number from 1 to 7")
num=int(input("Enter your number:"))
if num == 1:
    print("Sunday")
elif num == 2:
    print("Monday")
elif num == 3:
    print("Tuesday")
elif num == 4:
    print("Wednesday")
elif num == 5:
    print("Thursday")
elif num == 6:
    print("Friday")
elif num == 7:
    print("Saturday")
else:
    print("invalid number")
#Q.no.27
'''
the logical operator are:
A>B & C>D
'''
#Q.no.28
num=int(input("Enter your number:"))
if (num>100 and num<999):
    print("It is three digit number")
else:
    print("It is not three digit number")
#Q.no.29
age=float(input("Enter your age:"))
if age >= 60:
    print("You are senior citizen.")
else :
    print("You are not senoir citizen.")

#Q.no.30
num1= int(input("Enter you number:"))
num2= int(input("Enter you number:"))
if num1 > num2:
    print("Num2 is lowest")
else:
    print("num1 is lowest")

#Q.No.31

""" elif is the correct statement in python """

#Q.no.32
a = int(input("Enter total number of working days:"))
b = int(input("Enter number of days absent:"))
per = (a-b)/a*100
print ("Your attendence is",per)
if per < 75:
    print("You are not eligible for exam")
else :
    print("You are eligible for exam")

#Q.no.33
per = float(input("Enter your percentage:"))
if per < 40:
    print("Failed")
elif per >=40 and per < 55 :
    print("Fair")
elif per >=55 and per < 65 :
    print("Good")
elif per >= 65 and per <=100:
    print("Excellent")
else:
    print("Invalid percentage")

#Q.no.34
Age=int(input("Enter your age:"))
sex=input("Enter your sex(M/F):")
days=int(input("Enter number of days"))
if Age >=18 and Age < 30 and sex.upper()=='M':
    amt = days*700
    print("Total wages is:",amt)
elif Age >=18 and age < 30 and sex.upper() == 'F':
    amt = days*750
    print("Total wages is:",amt)
elif Age >= 30 and age <= 40 and sex.upper() == 'M':
    amt = days*800
    print("Total wages is:",amt)
elif Age >= 30 and age <= 40 and sex.upper() == 'F':
    amt = days*850
    print("Total wages is:",amt)   
else :
    print("Enter appropriate age")
  

#Q.no.35
Num1 = int(input("Enter your number:"))
Num2 = int(input("Enter your number:"))
Num3 = int(input("Enter your number:"))
if Num1 > Num2 and Num2 > Num3:
    print("Number is the second largest number")
elif Num1 > Num3 and Num3 > Num2:
    print("Number2 is the second largesst number")
elif Num3 > Num1 and Num1 > Num2:
    print("Number is the second largest number")
else:
    print("Invalid number")

#Q.no.36
days = int(input("Enter the days you have borrowed the book:"))
if days <= 5:
    print("Two rupees per day")
elif days >= 6 and days <=10:
    print("Three rupees per day")
elif days >=11 and days <=15:
    print("Four rupees per day")
elif days > 15:
    print("Five rupees per day")
else :
    print("Invalid Days.")
     
#Q.no.37
a = True
b = True
c = True
d = True
print (c) 
print (d)
print (not a)
print(not b)
print(not c)
print(not d)
print(a and b)
print(a or b)
print(a and b or c)
print(not a or b or c)
print(not a or not b or not c)
print(not(not a or not b or not c))

