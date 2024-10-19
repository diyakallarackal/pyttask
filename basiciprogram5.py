""""
Author:Diya Pradeep
Date:19-10-2024
Description:Simple desktop calculator using Python. Only the five basic arithmetic operators.
"""
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
sum_num=num1+num2
sub_num=num1-num2
mult_num=num1*num2
div_num=num1/num2
mod_num=num1%num2
result = (num1 + num2) * num3 / 2
print("The sum of num1 and num2 is: ",sum_num)
print("The difference when num2 is subtracted from num1 is: ",sub_num)
print("The product of num1 and num2 is: ",mult_num)
print("The quotient when num1 is divided by num2 is: ",div_num)
print("The remainder when num1 is divided by num2 is: ",mod_num)
print("The result of (num1 + num2) * num3 / 2 is: ", result)
