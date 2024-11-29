def check_triangle():
    list=[]
    s1=int(input("Enter first side:"))
    s2=int(input("Enter second side:"))
    s3=int(input("Enter third side:"))
    list.append(s1)
    list.append(s2)
    list.append(s3)
    list.sort()
    if list[2]**2==list[0]**2+list[1]**2:
        print("It is a right triangle")
    else:
        print("It is not a right triangle")

check_triangle()


