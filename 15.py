""" 
Name = 'Kushal'
if Name == 'Sachin':
    print (f"Hello {Name},Welcome to our website")
else:
    print ('Sorry, You are not known to us')
saving=int(input("Enter your pocket money:"))
if saving>3000:
    print("Dating with Sita")
elif saving>2000:
    print("Dating with Gita")
else:
    print("Sutta with friends")
Num=int(input("Enter your number"))
if Num % 3|5:
    print("fizz fuzz")
elif Num / 3==0:
    print("fiz")
elif Num / 5==0:
    print("fuzz")
Monthlist=('JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUG','SEP','OCT','NOV','DEC')
value=Monthlist[0]
print(value)
#shift+alt+a=docstring banxa
print('148'>'BANANA')
num=7
Num=8
operator= '+'
sum = num operator Num
print(sum)
 """
#rock,paper,sissor

player1=(input("Enter your move:"))
player2=(input("Enter your move:"))

if player1=="rock" and player2=="scissor":
    print("Player1 has won")
elif player1=="rock" and player2=="paper":
    print("Player2 has won")
elif player1=="scissor" and player2=="paper":
    print("player1 has won")
    
else:
    print("Draw")


