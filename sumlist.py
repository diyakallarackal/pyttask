def sum_list(num):
    total=0
    for i in num:
        total+=i
    return total

result=sum_list((4,5,6))
print("The sum of all numbers in the list is",result)