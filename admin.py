import pandas as pd
from prettytable import PrettyTable
import csv
import matplotlib.pyplot as plt
import os

def admin_choice():
    csv_file = "raw_data.csv"
    global df,df2,df3
    df = pd.read_csv(csv_file)

    df2 = pd.read_csv(csv_file)
    df2.dropna(inplace=True)
    df2.drop_duplicates(subset="Username", keep="first", inplace=True)
    df2.to_csv("final_data.csv",index=False)

    df3 = pd.read_csv("data_plot.csv",usecols=["CGPA","Package[LPA]"])
    df4 = pd.read_csv("final_data.csv")

    while True:
        print('Enter "1" for Seeing Raw Data ')
        print('Enter "2" for Seeing Manipulated Data ')
        print('Enter "3" for Sorting Data ')
        print('Enter "4" for Seeing Graphical View Of Data ')
        print('Enter "5" for Exporting Data to Excel ')
        print('Enter "6" for Log Out ')
        ch = input("Enter your choice : ")
        print()
        if ch == "1":
            data_raw()
        elif ch == "2":
            filtered_data()
        elif ch == "3":
            data_sort()
        elif ch == "4":
            data_plotting()
        elif ch == "5":
            df4.to_excel("data_file.xlsx",index=False)
            print("Data Exported Successfully")
            print()
        elif ch == "6":
            print("Logged Out Successfully")
            print()
            break
        else:
            print("Please Enter a valid choice!")
            print()

def data_raw():
    lst = [n for n in df]
    Table = PrettyTable(lst)
    with open("raw_data.csv","r") as file:
        table_values = csv.DictReader(file)
        data = [n for n in table_values]

    for  i in data:
        lst1 = []
        for j in i.values():
            lst1.append(j)
        Table.add_row(lst1)
    print('> this is the raw data <' .center(50,"~"))
    print(Table)
    print()
    input('Press "Enter" to Continue! ')

def filtered_data():
    pt = PrettyTable()
    pt.field_names = df2.columns

    for _, row in df2.iterrows():
        pt.add_row(row)

    print("> This is the Final data without any Duplicate or Null Value <".center(50,"~"))
    print(pt)
    print()       
    input('Press "Enter" to Continue! ')

def data_sort():
    a = [n for n in df2]
    f=input("Enter the column Name to sort the data : ")

    if f in a:  
        s=df2.sort_values(by=[f],ascending=False)
        df_s = pd.DataFrame(s)
        table = PrettyTable()
        table.field_names = df2.columns
        for _,row in df_s.iterrows():
            table.add_row(row)
        print(table)
        print()
        input('Press "Enter" to Continue! ')
    else:
        print("Invalid Column Name")
        print()

def data_plotting():
    df3 = pd.read_csv("data_plot.csv")
    
    while True:
        print('Enter "1" for Student - Package graph')
        print('Enter "2" for Company - No. of Students graphs')
        print('Enter "3" for Student - CGPA graph')
        print('Enter "4" for Student - CGPA - Package graph')         
        print('Enter "5" to exit Graphical View')
        choice = input("Enter your Choice : ")

        if choice == "1":
            df3.plot(kind='bar', color="#EF7215", x="First Name", y="Package[LPA]", figsize=(17,8))
            plt.xticks(rotation='horizontal')
            plt.ylabel("CGPA")
            plt.grid(True)
            plt.legend()
            save_plot()

        elif choice == "2":
            explode = (.06,)*7
            df3.groupby(["Company"]).count().plot(kind="pie", y="Username", autopct = "%1.0f%%", explode = explode, figsize=(20,10)) 
            plt.legend(loc=1)
            save_plot()

        elif choice == "3":
            df3.plot(kind='bar', x="First Name", y="CGPA", figsize=(20,8))
            plt.xticks(rotation='horizontal')
            plt.ylabel("Package[LPA]")
            plt.legend()
            plt.grid(True)
            save_plot()

        elif choice == "4":
            df3.set_index('First Name').plot(kind='bar', figsize=(20,8))
            plt.xticks(rotation='horizontal')
            plt.grid(True)
            save_plot()

        
        elif choice == "5":
            print("Exited from Graphical View!")
            print()
            break

        else:
            print("Please Enter a Valid choice!")

def save_plot():
    save = input("Do you want to save this plot? (yes/no): ")
    if save.lower() == "yes":
        file_type = input('Enter type of file that you want (jpg / jpeg / png / pdf): ')
        file_name = "plot"
        counter = 1
        while os.path.exists(f"{file_name}_{counter}.{file_type.lower()}"):
            counter += 1
        final_file = f"{file_name}_{counter}.{file_type.lower()}"
        plt.savefig(final_file)
        print("Your Plot has been Saved as", final_file)
    else:
        print("Plot not saved.")
    print()
    plt.show()


if __name__ == "__main__":
    admin_choice()
    pass