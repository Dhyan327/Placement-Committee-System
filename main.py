import login
import time

print()
print("> Welcome to Placement Committe <".center(50,"~"))
print()

def made_by():
    msg = ''' 
            Thanks for evaluating our Project.
            Have a Nice day! \U0001f600

            Placement Committe Project made by    : Maniyar Dhyan
            Enrollment No.                        : 236490316113
            College Name                          : Sir Bhavsinhji Polytechnic Institute
            Term                                  : Summer-2024
             
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.007)

while True:
    print('Enter "1" for Admin Login ')
    print('Enter "2" for User Login ')
    print('Enter "3" for Creating New Account ')
    print('Enter "4" for Terminating Software ')
    choice = input("Enter your choice : ")
    print()

    if choice == "1":
        login.admin_login()
    elif choice == "2":
        login.user_login()
    elif choice == "3":
        login.new_user_login()
    elif  choice == "4":
        made_by()
        break
    else:
        print("Please Enter a Valid choice!")
        print()
