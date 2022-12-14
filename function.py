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
#append
a = [1,2,3,4,5]
a.append([6,9])  #esma chai list nai gayera basxa
print(a)
#extend
a = [1,2,3,4,5]
a.extend([6,9])  #esma chai single element gayera basxa
print(a)
#insert
a= [1,2,3,4,5,6,]
a[0]='hi'
print(a)     #esma chai jata halna mann lagyo tesma halna milxa

#del=indexing gareko element delete hunxa 
a=[1,2,3,4,5]  
del a[2]
print (a)
#remove=jun number remove garnu xa tei remove hunxa indexing hudaina
a=[1,2,3,4]
a.remove(3)
print(a)
#pop=khali xodyo bhane last element delete hunxa   
a=[1,2,3,4]
a.pop(2)
print (a)

#sort = ascending order ma haldinxa
a=[1,6,8,4,5,8,9]  
a.sort()
print(a)

#REVERSE = list ko reverse nikalxa
a=[1,3,45,67,89,90]
a.reverse()
print(a)

#tuple
a=(1,2,3,4,5)  #tuple lai list ma convert gareko ani list ma add gareko
tp = list((a))
tp.extend([6])
print(tp)


a=(1,2,3,4,1,1,1,1)
b = len(a)
count=[]
for i in range(b):
    if a[i]==1:
        count.append(i)
print(count)


