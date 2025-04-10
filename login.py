import pandas as pd
import admin as ad
import user as us

def admin_login():
    try:
        admin_username = input("Enter Admin username : ")
        admin_password = input("Enter Admin Password : ")

        df = pd.read_csv("admin_credentials.csv")
        data_list = df.values.tolist()

        flag = 0
        for i,j in data_list:
            if admin_username==i and admin_password==j:
                print("Successfully Login")
                print()
                flag = 1
                break
        
        if flag == 1:
            ad.admin_choice()      

    except ValueError as e:
        print("Error : ",e)
    except Exception as E:
        print("Error : ",E)

def user_login():
    try:
        user_username = input("Enter your username : ")
        user_password = input("Enter your Password : ")
        df = pd.read_csv("user_credentials.csv")
        data_lst = df.values.tolist()

        flag = 0
        for i,j in data_lst:
            if user_username == i and user_password == j:
                print("Successfully Login")
                print()
                flag = 1
                break
            else:
                continue
        if flag == 1:
            us.user_choices(user_username,user_password)
        else:
            print("\nyour account doesn't exist...\nplease create a new account first\n")

    except ValueError as e:
        print("Error : ",e)
    except Exception as E:
        print("Error : ",E)

def new_user_login():
    try:
        dic = {}
        new_username = input("Enter new Username : ")
        new_password = input("Enter new Password : ")
        lst = [new_username,new_password]
        df = pd.read_csv("user_credentials.csv")
        data_lst = df.values.tolist()
        if lst in data_lst:
            print("\nYour Acoount is already registered")
            print("To perform any activities , login to your account \n")
            print()
            user_login()    

        else:
            dic[new_username]=new_password
            csv_file = "user_credentials.csv"
            data = pd.DataFrame(list(dic.items()), columns=["Username", "Password"])
            data.to_csv(csv_file, mode='a' ,index=False, header=False)
            print("\nYou have been signed up successfully!\nNow Login to your account\n")
            user_login()
    
    except ValueError as e:
        print("Error : ",e)
    except Exception as E:
        print("Error : ",E)

if __name__ == "__main__":
    user_login()
    pass