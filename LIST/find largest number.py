list0 = [0]
list1 = [4,3,2,1]
list2 = [2,4,6,8]
list3 = [10,25,30,5]


if list1:
    print(max(list1),min(list1))
else:
    print("list is empty")





if list2:
    print(max(list2),min(list2))
else:
    print("list is empty")


if list3:
    print(max(list3),min(list3))
else:
    print("list is empty")

# Python program to find largest
# number in a list


list1.sort()
print(list1[-1])

if list0:
    print(max(list1), max(list2), max(list3))
