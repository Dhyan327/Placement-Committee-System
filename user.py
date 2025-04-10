import pandas as pd
import random as rd
import registration_form as rf
import time as t


def user_choices(user_username,user_password):
        
    while True:
        df1 = pd.read_csv("raw_data.csv")
        df1.dropna(inplace=True)
        df1.drop_duplicates(inplace=True)
        df2 = pd.read_csv("final_data.csv",usecols=["Username","CGPA","First Name"])
        raw_lst = []
        final_lst=[]
        final_us = []

        df3 = pd.read_csv("data_plot.csv")

        for i in df1.index:
            raw_lst.append(df1.loc[i,"Username"])

        for j in df2.index:
            final_lst.append(df2.loc[j,"Username"])

        for z in df3.index:
            final_us.append(df3.loc[z,"Username"])
    
        print('Now, what do you want to do? \nEnter "1" for Registering your data \nEnter "2" to check your result \nEnter "3" to Log-Out')
        choice = input('Enter your Choice : ')
        print()
        if choice == "1":
            rf.registration_form(user_username,user_password)

        elif choice == "2":
            print("First , let us check your eligibility to give this test")
            t.sleep(2)
        
            if user_username not in final_us:
                if user_username in raw_lst:
                    if user_username in final_lst:
                        print("\nYou are eligible for the test\nlet's start the test then....")
                        print()

                        global placement_details
                        placement_details = []
                        for i in df2.index:
                            if df2.loc[i,"Username"]==user_username:
                                placement_details.append(df2.loc[i,"First Name"])
                                placement_details.append(df2.loc[i,"Username"])
                                placement_details.append(df2.loc[i,"CGPA"])

                        user_test()
                        data = pd.DataFrame(placement_details)
                        data = data.T
                        data.to_csv("data_plot.csv",mode="a",index=False,header=False)
                        t.sleep(2)
                        print()

                    else:
                        t.sleep(3)
                        print("\nYour data is still being processed\nPlease try after some time\n")
                else:
                    t.sleep(3)
                    print("\nYou are Not Eligible for the Test!")
                    print()
            else:
                print("\nYou have already given the test!")
                print()
                t.sleep(2)
                    
        elif choice == "3":
            print("\nLogged Out Successfully!")
            print()
            t.sleep(2)
            break
        else:
            print("\nPlease Enter a valid Choice!")
            print()
        
def user_test():
    company_name = ["Google", "Microsoft", "Nvidia", "Infosys", "IBM", "Oracle", "Intel"]
    p1 = rd.randint(15, 20)
    p2 = rd.randint(10, 15)
    p3 = rd.randint(7, 10)
    P = rd.random()
    package1 = round((p1 + P), 2)
    package2 = round((p2 + P), 2)
    package3 = round((p3 + P), 2)
    company = rd.choice(company_name)
    t.sleep(3)
    test = [['Which function is used to sort any data collection methods?', 'sorted()', ['sorted()', 'sort()', 'order()', 'arrange()']],
            ['What is the output of : (2+3)!', '120', ['120', '15', '6', '32']],
            ['Is lambda a higher order function?', 'yes', ['yes', 'no']],
            ['Does Python have Pointers?', 'no', ['no', 'yes']],
            ['Is Python an Object Oriented Language?', 'yes', ['yes', 'no']]]
    count = 0
    for i in range(3):
        trial = []
        test_idx = rd.randint(0, len(test) - 1)
        test2 = test.pop(test_idx)
        
        rd.shuffle(test2[2])
        
        print(test2[0])
        for idx, option in enumerate(test2[2], start=1):
            print(f"{idx}. {option}")
        answer = input("Enter your answer (by option number): ")
        print()
        if answer.isdigit():
            answer = int(answer)
            if 1 <= answer <= len(test2[2]):
                if test2[2][answer - 1] == test2[1]:
                    count += 2
            else:
                print("Invalid Choice!")
                print()
        else:
            print("Invalid Choice!")
            print()

    print("Wait for some time...\nWe are evaluating your result")
    print()
    if count == 6:
        t.sleep(3)
        print(f'You have been placed in {company} with a package of {package1} LPA')
        placement_details.append(company)
        placement_details.append(package1)
    elif count == 4:
        t.sleep(3)
        print(f'You have been placed in {company} with a package of {package2} LPA')
        placement_details.append(company)
        placement_details.append(package2)
    elif count == 2:
        t.sleep(3)
        print(f'You have been placed in {company} with a package of {package3} LPA')
        placement_details.append(company)
        placement_details.append(package3)
    else:
        t.sleep(3)
        print("You failed the test\nBetter luck next time")
        placement_details.append("Null")
        placement_details.append(0)

if __name__ == "__main__":
    user_choices("Dhyan","Dhyan327")
    pass