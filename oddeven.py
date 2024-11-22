'''
Name:Diya Pradeep
Date:22-11-2024
Description:Input two list ,merge these lists into a third iast such that in the merged list ,all even number occur first followed by odd  numbers. Both the even and odd numbers should be in sorted order.
'''
list1=[9,13,19,16,14]
list2=[27,24,29,37]
list3=list1+list2
even_list=[]
odd_list=[]
for i in list3:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
merged_list=even_list+odd_list
print("First List:",list1)
print("Second List:",list2)
print("Merged List:",merged_list)

