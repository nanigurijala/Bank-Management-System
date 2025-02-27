from register import *
status = False

print('+-------------------------------------------------------+')
print('                 welcome to nani bank                    ')
print('+-------------------------------------------------------+')
while True:
    try:
        register = int(input("1. Signup \n"
                             "2. Signin: "))
        if register == 1 or register == 2:
            if register == 1:
                signup()
            if register == 2:
                user = signin()
                status = True
                break
        else:
            print('Pleases Enter A Valid Number')
            
    except ValueError:
        print('Invalid Input Try Again With Numbers')
        
account_number = db_query(f"SELECT account_number FROM customers WHERE USERNAME = '{user}';")

while status:
    print(f"Welcome {user.capitalize()} Choose Your Banking Service\n")
    try:
        facilities = int(input("1. Balance \n"
                             "2. Cash Deposite \n"
                             "3. Cash Withdraw\n"
                             "4. Fund Transaction\n"
                             "5. Exit\n"))
        if facilities >=1 and facilities<=5:
            if facilities == 1:
                bankobj = Bank(user, account_number[0][0])
                bankobj.balance_enquiry()
                
            elif facilities == 2:
                while True:
                    try:
                        amount = int(input("Enter amount To Deposite: "))
                        bankobj = Bank(user,account_number[0][0])
                        bankobj.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
                
            elif facilities ==3:
                while True:
                    try:
                        amount = int(input("Enter Amount To Withdraw: "))
                        bankobj = Bank(user,account_number[0][0])
                        bankobj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
               
            elif facilities == 4:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number: "))
                        amount = int(input("Enter Amount To Transfer "))
                        bankobj = Bank(user,account_number[0][0])
                        bankobj.fundtransfer(receive,amount)
                        mydb.commit()               
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facilities == 5:
                print("Thank You U1sing Our Bank!")
                status = False
        else:
            print('Pleases Enter A Valid Number')
            continue
    except ValueError:
        print('Invalid Input Try Again With Numbers')
        continue