""""
Author=Diya Pradeep
Date=28-10-2024
Description=Write a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit.
"""
while True:
    print("\n1,\tConvert Celsius to Fahrenheit")
    print("2,\tConvert Fahrenheit to Celsius")
    print("3,\tExit the program")
    choice=int(input("Enter your choice:"))
    if choice==1:
        celsius=int(input("Enter temperature:"))
        fahrenheit_temp = (celsius * 9 / 5) + 32
        print(celsius,"Celsius in fahrenheit is ", fahrenheit_temp)
    if choice ==2:
        fahrenheit=int(input("Enter temperature:"))
        celsius_temp= (fahrenheit - 32) * 5 / 9
        print(fahrenheit,"Fahrenheit in celsius is ", celsius_temp)
    if choice==3:
        break
    else:
        print("Invalid Entry")

