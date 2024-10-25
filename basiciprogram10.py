""""
Author=Diya Pradeep
Date=25/10/2024
Description=Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
"""
temp=int(input("Enter the temperature:"))
scale=input("Is this in (C)elsius or (F)aherheit?")
if scale=="C":
    result_c= (9/5*temp) + 32
    print(temp,"Celsius is",result_c ,"Fahrenheit.")
else:
    result_f=5/9*(temp-32)
    print(temp,"Fahrenheit is",result_f,"Celsius.")
