

import math
number_1=int(input("enter your the first number."))
number_2=int(input("enter your the second number."))
operation=input(''' please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
f for factorial
''')
if operation=='+':
    output_number = number_1 + number_2
    print(f"{number_1}+{number_2}={output_number}")
    #print(number_1,"+",number_2,"=",output_number)
elif operation=='-':
    output_number = number_1 - number_2
    print(f"{number_1}-{number_2}={output_number}")
elif operation=='*':
    output_number = number_1 * number_2
    print(f"{number_1}*{number_2}={output_number}")
elif operation=='/':
    output_number = number_1 / number_2
    print(f"{number_1}/{number_2}={output_number}")
elif operation == 'f':
    output_number1=math.factorial(number_1)
    output_number2=math.factorial(number_2)
   # print("{}!={} {}!={}".format(number_1,output_number1,number_2,output_number2))
    print(number_1,"!","=",output_number1,"",number_2,"!","=",output_number2)      
else:
    print('you have not typed a valid operator,please run the program again.')
