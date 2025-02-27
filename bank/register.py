# user registration signup and signin
import random
from customer import *
from database import *
from bankService import *
def signup():
    username = input("Create Username: ")
    temp = db_query(f"SELECT USERNAME FROM customers WHERE username = '{username}';")
    if temp:
        print('Username Already Exists')
        signup()
    else:
        if username =='':
            print('enter a valid name')
            signup()
        print('username is availble please proceed')
        password = input('enter your password: ')
        name = input('enter your name: ')
        age = input('enter your age: ')
        city = input('enter your city: ')
        
        
        while True:
            account_number = random.randint(10000000,99999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("Your Account Number",account_number)
                break
    customerObj = Customer(username,password,name,age,city,account_number)
    customerObj.createUser()
    bankObj = Bank(username,account_number)
    bankObj.create_transaction_table()
#--signup function end
#--start signin function

def signin():
    username = input('Enter Username: ')
    temp = db_query(f"SELECT USERNAME FROM customers WHERE username = '{username}';")
    if temp:
        while True:
            password = input(f'Welcome {username.capitalize()} Enter Your Password: ')
            temp = db_query(f"SELECT password FROM customers WHERE username = '{username}'; ")
            # print(temp[0][0])
            if temp[0][0] == password:
                print('Signin Succesfully!')
                return username
            else:
                print('Wrong Password Try Again')
                continue
    else:
        print('User Not Found !')
        signup()