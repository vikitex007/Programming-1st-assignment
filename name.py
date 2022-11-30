#for S
for row in range (7):
    for col in range(4):
        if ((col==0)and (row==1 or row ==2 or row==6))or((col==1)and(row==0 or row==3 or row ==6))or ((col==2)and (row==0 or row==3 or row==6))or((col==3)and (row==4 or row==5 or row==0)):
            print('*',end="  ")
        else:
            print(end='   ')
    print()


#for A

for row in range(6):
    for col in range(5):
        if ((col==0)and (row!=0 and row!=1))or((col==1)and (row==1 or row==3))or((col==2)and(row==0 or row==3))or((col==3)and (row==1 or row ==3))or ((col==4)and(row!=0 and row!=1)):
            print('*',end='  ')
        else :
            print(end= '   ')
    print()

#for C
for row in range(6):
    for col in range(4):
        if ((col==0)and(row!=0 and row!=5))or((col==1)and(row==0 or row==5))or((col==2)and(row==0 or row==5))or((col==3)and(row==0 or row==5)):
            print('*',end='   ')
        else:
            print(end='   ')
    print()

#for H 
for row in range(7):
    for col in range(5):
        if((col==0))or((col==1)and (row==3))or ((col==2)and (row==3))or((col==3) and (row==3)) or (col==4):
            print('*',end='  ')
        else:
            print(end='   ')
    print()

#for I
for row in range(7):
    for col in range(5):
        if((col==0)and (row==0 or row==6))or((col==1)and (row==0 or row==6))or(col==2)or((col==3)and (row==0 or row==6))or((col==4)and (row==0 or row==6)):
            print('*',end='  ')
        else:
            print(end='   ')
    print()
#for N
for row in range(5):
    for col in range(5):
        if (col==0)or ((col==1)and(row==1))or((col==2)and(row==2))or((col==3)and(row==3)) or (col==4) :
            print('*',end='  ')
        else:
            print(end='   ')
    print()
    
