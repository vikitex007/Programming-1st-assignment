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