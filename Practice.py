# Write code to represent logic of a program that allows the user to enter value
# The program multiples the value by 10 and output the results
#keep asking to enter a value




while True:
    value = int(input("Enter the value (or enter '0' to quit):  "   ))


    if value == 0:
        break
       
    result = value * 5


    print("Result:", result)



