def phone_number(ph_num):
    count=len(ph_num)
    if count==10:
        if ph_num[0] in ["7","8","9"]:
            print("The Phone Number",ph_num,"is valid")
        else:
            print("The Phone Number",ph_num,"is invalid")
    else:
        print("Invalid Phone Number")

ph_num=input("Enter phone no:")
phone_number(ph_num)
