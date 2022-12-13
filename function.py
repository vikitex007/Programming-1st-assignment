""" def add(X,y,z):
    print(X+y+z)

if __name__ == '__main__' :
   add(5,6,3)
 """

 

""" m = int(input('Enter your math marks:'))
e = int(input('Enter your english marks:'))
n = int(input('Enter your nepali marks:'))
s = int(input('Enter your science marks:'))
so = int(input('Enter your social marks:'))
totalmark=500
#for sum
def calcutlatesum():
    sum=m+n+e+s+so
    return sum
print('your total marks is',calcutlatesum())
#for percentage
def calculateper():   
    per=((m+n+e+s+so)/500)*100
    return per
print('your percent is',calculateper())

#for result
def result():
    if calculateper() <40:
        print('Failed')
    elif(m<40 or n<40 or e<40 or s<40 or so<40):
        print('fail')
    else:
        print('pass')
    print(result())     """

""" #return 
def multiply(a*b):
   a = 20
   b = 30 """


""" list = [1,2,3,4]
def sum():
    total=0
    for i in list:
        total+=i
    return total
print(sum()) """
#largest number
""" a=10
b=20
c=30
def largest():
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
        return c
print(largest()) """

#second largest
""" a = int(input('enter your number:'))
b = int(input('enter your number:'))
c = int(input('enter your number:'))
def seconlargest():
    if (a>b and a<c) or (a>c and a<b):
        return a
    if (b>a and b<c) or (b>c and b<a):
        return b
    if (c>a and c<b) or (c>b or c<a):
        return c
print(seconlargest()) """
#check if number is perfect square or not
""" import math
a=3444
root=math.sqrt(a)
if int(root)**2 == a:
    print('perfect square')
else:
    print('not perfect square')
      """

""" import random 
li = [1,2,3,4,5,6,7,8,9]
random.shuffle(li)
print(li) """

""" import time
timing=time.time()
a=10
b=20
c=a+b
print(c)
print(time.time()-timing)

a=(1,2,3,4,d)
b=[1,2,3,4,5]
c={1,2,3,4,5}
print(type(a))
print(type(b))
print(type(c)) """

