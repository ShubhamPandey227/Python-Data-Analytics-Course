#using if elif
import os 
while True :
    print ("Select a number : ")
    print ('1. Addition')
    print ('2. Subtraction')
    print ('3. Mutliplication')
    print ('4. Division')
    print ('5. Remainder')
    print ('6. Exit')
    ch = input ('Enter your choice : ')
    if ch == '1' :
        a = int(input('Enter First Number : '))
        b = int(input('Enter Second Number : '))
        print (f'{a} + {b} = {a+b}')
    elif ch == '2' :
        a = int(input('Enter First Number : '))
        b = int(input('Enter Second Number : '))
        print (f'{a} - {b} = {a-b}')
    elif ch == '3':
        a = int(input('Enter First Number : '))
        b = int(input('Enter Second Number : '))
        print (f'{a} * {b} = {a*b}')
    elif ch == '4' :
        a = int(input('Enter First Number : '))
        b = int(input('Enter Second Number : '))
        print (f'{a} / {b} = {a/b}')
    elif ch == '5' :
        a = int(input('Enter First Number : '))
        b = int(input('Enter Second Number : '))
        print (f'{a} % {b} = {a%b}') 
    elif ch == '6' :
        print('Exiting....')    
    else :
        print ("Invalid Choice")
    input ('Press Enter to Continue....')
    os.system('cls') #to clear the screen 
