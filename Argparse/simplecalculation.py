import argparse

parser = argparse.ArgumentParser(description='Finding the sum. Type python3 filename.py yourname --result anywordyourlike')
parser.add_argument('name',help='your name')
parser.add_argument('--result','--ru',help='Enter the first number and second number to find the summation.')
#or parser.add_argument('--result','--ru',help='Enter the first number and second number to find the summation',dest='result')
args=parser.parse_args()
if args.result:
    firstnumber = int(input("Enter the first number"))
    secondnumber = int(input("Enter the second number"))
    result = firstnumber + secondnumber
    number = int(input("Enter the option 1 for addition 2 for subtratiocn 3 for division 4 for multiplication"))
    if number == 1:
        print("The summation of the two numbers is ",firstnumber + secondnumber)
    elif number == 2:
        print("The subtration of the two numbers is ",firstnumber - secondnumber)
    elif number == 3:
        print("The division of the two number is ",firstnumber / secondnumber)
    elif number == 4:
        print("The multiplication of the two number is ",firstnumber * secondnumber)
else:
    print(f"Hello, {args.name}!")


"""
INSTRUCTION
once your hit the run button
In the terminal type python3 yourfilename.py anish --result anyword
After this do as it shows in the instruction
"""
