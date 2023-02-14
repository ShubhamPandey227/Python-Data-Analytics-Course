import os 
while True :
    print ("Select a number : ")
    print ('1. Addition')
    print ('2. Subtraction')
    print ('3. Mutliplication')
    print ('4. Division')
    print ('5. Remainder')
    print ('6. Exit')
    match(input ('Enter your choice : ')) :
        case '1' :
            a = int(input('Enter First Number : '))
            b = int(input('Enter Second Number : '))
            print (f'{a} + {b} = {a+b}')
        case '2' :
            a = int(input('Enter First Number : '))
            b = int(input('Enter Second Number : '))
            print(f'{a} - {b} = {a-b}')
        case '3':
            a = int(input('Enter First Number : '))
            b = int(input('Enter Second Number : '))
            print (f'{a} * {b} = {a*b}')
        case '4' :
            a = int(input('Enter First Number : '))
            b = int(input('Enter Second Number : '))
            print (f'{a} / {b} = {a/b}')
        case '5' :
            a = int(input('Enter First Number : '))
            b = int(input('Enter Second Number : '))
            print (f'{a} % {b} = {a%b}') 
        case '6' :
            print('Exiting....')
        case _ :
                print('Empty')    
    input ('Press Enter to Continue....')
    os.system('cls') #to clear the screen 
