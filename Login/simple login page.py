print('Create an account!')

username = input('enter your username: ')
password = input('Enter your passowrd: ')

print('Let\'s Login!!!')
username2 = input('Enter your username: ')
password2 = input('Enter your username: ')

if password2 == password and username2 == username:
    print('Login done')
else:
    print('someting went wrong try again.')