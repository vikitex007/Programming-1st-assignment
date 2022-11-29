#for loop

for sachin in range(1,20): 
    print(f'Hello stranger {sachin}')

sachin ="Softwarica"
for j in sachin:
    print(j)

a = "python"
b = len(a)
for i in range(b):
    print(i,'=',a[i]) 

#multiplication of given number
num = 3
for i in range(1,10):
    print(num,'x',i,'=',num*i) 

##multiplication of number
multiply = 1
a = 123456789
b = str(a)
for i in b:
    multiply = multiply * int(i)
print(multiply) 
#prime number
num = int(input("Enter your number:"))
if num > 1 :
    for i in range (2,num):
        if a%i == 0:
            print('not a prime number')
            break
    else:
        print('prime number')

else:
    print('It is not prime number')
 
#reversename
a = "123122425"
reversestring = ""
for i in  a:
    reversestring=i+reversestring
print(reversestring)

#factorial
a=5
factorial=1
for i in range (1,a+1):
    factorial=factorial*i
print(factorial)
 
#find nummber of alphabet and digit
a= "hellomf7777"
digit = 0
letter = 0
for i in a :
    if i. isdigit():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
    else:
        pass
print(digit)
print(letter)
#mobile banking 
usrname = "Sachin"
password = 1234
for i in range(3):
    username1 = input('Enter valid name')
    password1 = int(input("Enter valid password"))
    if usrname==username1 and password==password1:
        print('logged in')
        break
    else:
        print('Invalid credintials')
else:
    print('3 attempts finished')
#atm machine
total_price = 0
card_type = "visa"
is_same_bank = True
is_expired=False

def read_card():
    print("Fetching Card Details from bank ....")
    card_details = [1200,True,False]
    total_price = card_details[0]
    is_same_bank=card_details[1]
    is_expired= card_details[2]
    if is_expired:
        print("Sorry, this card can not be accepted here")
    else:
        perform_tansaction(total_price,is_same_bank)


def perform_tansaction(total_amt, is_same_bank):
    charge = 0
    if not is_same_bank:
        charge = 5
        if required_amt > total_amt:
            return "Not enough balance"
        else:
            print(f"Ant withdrwn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")
    else:
        if required_amt > total_amt:
            return "Not enough balance"
        else:
            print(f"Ant withdrwn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")


print("Please insert your atm card:")
input()
print("Card inserted!!")
required_amt = int(input("Please enter a amount:"))
read_card() 



#multiplication table of a given num
'''a=int(input("enter the num"))
for i in range(1,11):
    print (a,'x',i,'=',a*i)'''


'''
a=int(input("enter a number"))
for i in range(10,0,-1):
    print(a,"*",i,"=",(a*i))'''

'''
a=int(input("enter a num"))
for i in range(1,a):
    print(a-i)'''



'''mul=1
sum=0
a=int(input("input enter a num"))
b=str(a)

for i in b:
    sum=sum+ int(i)
    mul=mul* int(i) 
print(sum)
print(mul)
'''


#prime numm
'''a=int(input("enter a num"))
if a>1:
    for i in range (2,a):
        if a%i==0:
            print("not a prime")
            break
    else:
            print("prime num")
    '''
#reverse if a string
'''a="python"
reverse_string=""
for i in a:
    reverse_string=i+reverse_string
print(reverse_string)'''
        

  
'''a=int(input("enter a num"))
mul=1
for i in range(1,a+1):
    mul=mul*(i)
print (mul)'''

#pallindrooe

'''a=input("enter a word  ")
reverse_string=""
for i in a:
    reverse_string=i+reverse_string
if reverse_string==a:
    print("it is a pallinddrome")
else:
    print("not a pallindrome")'''
    
##
'''a="hello123"
digit=0
letter=0
for i in a:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
print(digit)
print(letter)
        '''


    
'''username = "kripesh"
password = "2244"

for i in range(3):
    user= input("Enter your username : ")
    pin= input("Enter your pin number : ")

    if user==username and pin== password: 
        print("logged in")
        break

    else:
        print("Invalid pin")'''



'''for i in range(2):
    print("outer loop",i)
    for j in range(3):
        print("inner loop",j)
print("rest of the code")
'''

'''for i in range(1,11):
   for j in range (1,11):
    print(i,"x",j,"=",i*j)'''
#print softwarica 10 times.
'''for i in range(10):
    print("softwarica")'''

#sum of a list:
'''a=[1,2,3,4,5]
sum=0
for i in list(a):
    sum = sum+(i)
print (sum)'''



#print each charater using indexing
'''a="python"
b=len(a)
for i in range(b):
    print(i,"=",a)
    '''
    
#program to display each element of a list
'''l=[1,2,3,4,5]
for i in list(l):
    print(i)'''

#multiplication table of a given num
'''a=int(input("enter the num  "))
for i in range(1,11):
    print (a,'x',i,'=',a*i)
'''
#reverse of a list
'''l=[1,2,3,4,5] 
b=len(l)
c=[]
for i in range(b,0,-1):
    c=c+[i]
print (c)'''

#program to count the total digits inn a num
'''a=int(input("enter a num   "))
n=0
b=(str(a))
for i in b:
    n=n+1
print (n)'''

#given no is prime or not
'''a=int(input("enter a num   "))
if a>1:
    for i in range (2,a):
        if a%i==0:
            print("not a prime")
            break
    else:
            print("prime num")''' 


#count no of even and odd no from a series of a num
'''e=0
o=0
for i in range(10):
    if i%2==0:
        e=e+1
    else:
        o=o+1
print("there are ",e,"even numbers")
print("there are ",o,"odd numbers")
'''


#acceps a string and calculates the num of digits and numm
'''a="hello123"
digit=0
letter=0
for i in a:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
print(digit)
print(letter)'''



#user and pssword
'''username="kp"
password="123"
c=3
for i in range(3,0,-1):
    u=input("enter username")
    p=input("enter password")
    if i==username and p==password:
        print("logging in")
        break
    else:
        print(f"{i-1} chances remaining")'''



#to see given number is odd or not
'''a=int(input("enter a num  "))
if a%2==0:
    print("even")
else:
    print("odd")
'''

#given num is pallindrome or not
'''b=int(input("enter a num  "))
reverse=""
a=str(b)
for i in a:
    reverse=i+reverse
if reverse==a:
    print("pallindrome")
else:
    print("not a pallindrome")'''
    