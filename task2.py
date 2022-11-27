#Q.no.1
cp = int(input("Enter the c.p of bike:"))
if cp > 100000 :
    tax = (15/100)* cp
    print("The value of tax is:",tax)
elif cp > 50000 and cp <= 100000:
    tax = (10/100)* cp
    print("The value of tax is:",tax)
elif cp <= 50000:
    tax = (5/100)* cp
    print ("The value of tax is:",tax)
else :
    print("Invalid number")

#Q.No.2
Age1 = int(input("Enter your age:"))
Age2 = int(input("Enter your age:"))
Age3 = int(input("Enter your age:"))
Age4 = int(input("Enter your age:"))
 
if Age1 < Age2 and Age1 < Age3 and Age1 < Age4:
    print ("The youngest one is,",Age1)
elif Age2 < Age1 and Age2 < Age3 and Age2 < Age4:
    print("The youngrst one is,",Age2)
elif Age3 < Age1 and Age3 < Age2 and Age3 < Age4:
    print("The youngest one is,",Age3)
elif Age4 < Age1 and Age4 < Age2 and Age4 < Age3:
    print("The youngest one is,",Age4)
else :
    print("Invalid age")
#Q.no.3
Age1 = int(input("Enter your age:"))
Age2 = int(input("Enter your age:"))
Age3 = int(input("Enter your age:"))
Age4 = int(input("Enter your age:"))

if Age1 > Age2 and Age1 > Age3 and Age1 > Age4:
    print ("The oldest one is,",Age1)
elif Age2 > Age1 and Age2 > Age3 and Age2 > Age4:
    print("The oldest one is,",Age2)
elif Age3 > Age1 and Age3 > Age2 and Age3 > Age4:
    print("The oldest one is,",Age3)
elif Age4 > Age1 and Age4 > Age2 and Age4 > Age3:
    print("The oldest one is,",Age4)
else :
    print("Invalid age")

#q.no.4
mark = float(input('Enter your mark:'))
if mark < 25:
    print("Your grade is,D")
elif mark >= 25 and mark < 45 :
    print ("Your grade is, C")
elif mark >= 45 and mark < 50 :
    print ("Your grade is, B")
elif mark >= 50 and mark < 60 :
    print ("Your grade is, B+")
elif mark >= 60 and mark < 80 :
    print ("Your grade is, A")
elif mark > 80 and mark <=100:
    print("Your grade is, A+")
else:
    print("invalid marks")

#q.no.5
service = int(input("Enter your year of service:"))
salary = int(input("Enter your salary:"))
if service > 10:
    bonus = (10/100)*salary
    print ("Your bonus is,",bonus)
elif service >=6 and service <=10:
    bonus = (8/100)*salary
    print ("Your bonus is,",bonus)
elif service < 6:
    bonus = (5/100)*salary
    print ("Your bonus is,",bonus)
else:
    print("Invalid number")

