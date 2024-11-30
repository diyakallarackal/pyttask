def multiply_list(num):
    total=1
    for i in num:
        total*=i
    return total

result=multiply_list((4,5,6))
print("The product of all numbers in the list is",result)