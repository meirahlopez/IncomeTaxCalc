# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Income Tax Calculator
# create varibles for dependent and gross then calc income
#compute tax
#show the answer

gross= float(input("Enter the gross income: "))
dependent= int(input("Enter the number of dependents: "))
both= gross-10000-(dependent*3000)
tax=(both*20)/100
print("The income tax is: ", tax)
