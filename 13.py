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

x="python"
y="py"
print(x is not y)

a='hello'
print("he" in a)


a = 60
b = 13
c = 0
c = a & b;
print ("value of c is ", c)
c = a | b;
print ("Value of c is",c)
c = a^b;
print ("Value of c is",c)
c = ~a;
print ("Value of c is",c)
c = a << 2;
print ("Value of c is",c) 
 
hex(60)


a=282.45
b=565757
c='bbbb'
print(type(a))
print(type(b))
print(type(c))

name = input()
n=eval(input("what is your name "))
mobile = input("enter your mobile number")
print(name)
print(n)
print(mobile)

import keyword
print (keyword.kwlist)