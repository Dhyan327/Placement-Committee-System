from prettytable import PrettyTable
import pandas as pd

def registration_form(User_username,User_password):
    print("> Placement Committe Registration form <".center(50,"~"))
    print()

    try:
        print("Personal Details ~~> ")
        user_name = User_username
        user_password = User_password
        first_name = input("Enter First Name : ")
        last_name = input("Enter Last Name : ")
        age = str(input("Enter Age : "))
        if age == "" or age.isalpha() or int(age)<0:
            age = ""

        enroll_num = str(input("Enter Enrollment Number : "))
        mobile_num = str(input("Enter Mobile Number : "))
        if mobile_num.isalpha() or len(mobile_num)!=10:
            mobile_num = ""

        city = input("Enter City : ")
        state = input("Enter State : ")
        country = input("Enter Country : ")
        zip_code = input("Enter Zip Code : ")
        print()

        print("Educational Details ~~> ")
        school = input("Enter School Name : ")
        _10thmarks = input("Enter 10th Percentage : ")
        if _10thmarks == "" or _10thmarks.isalpha() or int(_10thmarks)<0 or int(_10thmarks)>100:
            _10thmarks = ""

        _12thmarks = str(input("Enter 12th Percentage: "))
        if _12thmarks == "" or _12thmarks.isalpha() or int(_12thmarks)<0 or int(_12thmarks)>100:
            _12thmarks = ""

        college = input("Enter College Name : ")
        cgpa = str(input("Enter your CGPA : "))
        if cgpa == "" or cgpa.isalpha() or float(cgpa)<0.00 or float(cgpa)>10.00:
            cgpa = ""

        personal_table = PrettyTable(["Field", "Value"])
        educational_table = PrettyTable(["Field", "Value"])

        dic1 = {"Username":User_username,"Password":User_password,"First Name":first_name,"Last Name":last_name,"Age":age,"Enrollment Number":enroll_num,
                "Mobile Number":mobile_num,"City":city,"State":state,"Country":country,"Zip Code":zip_code}
        dic2 = {"School Name":school,"10th Mark":_10thmarks,"12th Mark":_12thmarks,"College Name":college,"CGPA":cgpa}

        for i in dic1:
            personal_table.add_row([i,dic1[i]])
        for i in dic2:
            educational_table.add_row([i,dic2[i]])

        print("\nPersonal Details:")
        print(personal_table)
        print("\nEducational Details:")
        print(educational_table)

        dic3 = {**dic1,**dic2}
        csv_file="raw_data.csv"
        data=pd.DataFrame(list(dic3.values()),columns=["Values"])
        data = data.T
        data.to_csv(csv_file, mode='a', header=False, index=False)
        
    except Exception as e:
        print("Error : ",e)

if __name__ == "__main__":
    # registration_form()
    pass