def factorial(num):
    if num==0:
        return 1
    else:
        return(num*factorial(num-1))

num=int(input("Enter number:"))
result=factorial(num)
print(f"Factorial of {num} is {result}")

