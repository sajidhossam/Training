while True:
    while True:
        try:
            num1 = int(input('Enter The First Number: '))
            break
        except:
            print('Invalid Input. Please Enter A Number')
            
    while True:
        try:
            num2 = int(input('Enter The Second Number: '))
            break   
        except:
            print('Invalid Input. Please Enter A Number')
            

    op = input('Enter The Operation: ')
    while op not in ['/', '*', '-', '+']:
        print('invalid Operation. Please try again')
        op = input('Enter the operation: ')

    if op == '+':
        print('The Result is: ',num1 + num2)
    elif op == '-':
        print('The Result is: ',num1 - num2)
    elif op == '*':
        print('The Result is: ',num1 * num2)
    elif op == '/':
        print('The Result is: ',abs(num1/num2))
    else:
        Print('Wrong Operation')

    response = input('Another Operation? (y/n) ')
    while response.lower() not in ['y', 'n']:
        print('Invalid Input. Please Enter y or n')
        response = input('Another Operation? (y/n) ')
        
    if response.lower() == 'n':
        break


