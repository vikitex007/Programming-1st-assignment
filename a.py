a= "hello"
print(a)

a=b=c=d=100
a,b,c=1,2,3
print(d)

print (r"python \n is a programming language")

name="pyhton"
print (name[3])

week=52
days=7
year=week*days

print('The total number of days in a year is:',year)

def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__)


a = 20
b = 10
if ( a== b ):
    print (" a is equal to b ")
else:
    print ("a is not equal to b")

if ( a!= b):
    print (" a is not equal to b")
else:
    print (" a is equal to b")

if ( a < b):
    print("a is less than b")
else:
    print("a is not less than b")

if ( a > b ):
    print ("a is greater than b")
else:
    print (" a is not greater than b")

a=100
b='100'
print(a is b)

xx="dhairya"
print("dhi" not in xx)

a=30
b=50
c= a & b
print(c)


a=50.3+6
print (type(a))


data={1:'Samir',2:'himani',3:'binit'}
print(type(data))
print(data[3])

print(type(True))

a={a,100,"helo"}
print(type(a))

a=[a,100,"helo"]
print(type(a))


a=(a,100,"helo")
print(type(a))

print('hello' , end= " fucking " )
print('world')


print ("me","you",sep=" & ")

print("Hello {blc}, your balance is {0},".format("Adam", blc=200))

a=100
b=200
c=300
print(f"hello{a} high {b} kcha{c}")


print(f"{0.2:.607}")
print(f"{0.333:.6f}")

a=123
b=float(a)
print(b)




num1= int(input("enter first number :"))
num2= int(input("enter second number : "))
res = num1 -num2
print("sum of "+str(num1)+" and "+str(num2), " is "+str(res))

import pdb
bike = "Ducati"
bike_price = 6000000

car = "bugatti"
car_price = 20000000

pdb.set_trace()
name = input("Enter your name: ")
choose = int(input("press 1 for ducati and 2 for buggati: "))
print(f"hello {name}")

if choose==1:
    print(f"{bike} will cost you {bike_price}")
    
elif choose==2:
    print(f"{car+2000} will cost you {car_price+2000}")

else:
    print("press only 1 or 2")


data = {1,2,3, 'python'}
print(type(data))


a=100
b=20
c=15

print(f"My weight is {a}kg,My age is {b},My college is {c}km far")
