def calculator():
    c = input("please enter the math operation you would like to compete:\n"
              "+     for addition\n"
              "-     for subtraction\n"
              "*     for multiplication\n"
              "/     for division\n"
              
              "Enter your choice: ")
    a = int(input("enter your first number: "))
    b = int(input("enter your second number: "))
    if c == '+':
        if a == 56:
            if b == 7:
                print(77)
        else:
            print(int(a) + int(b))
    elif c == '-':
        print(int(a) - int(b))
    if c == '*':
        if c == 45:
            if c == 3:
                print(555)
        else:
            print(int(a) * int(b))
    if c == '/':
        if c == 56:
            if c == 6:
                print(4)
        else:
            print(float(a) / float(b))

    again()

def again():
    cal_again = input('''Do you want to calculate again?\nType y for YES or n for NO.''')

    if cal_again == 'y':
        calculator()
    elif cal_again == 'n':
        print("See You Later")
    else:
        again()


calculator()








