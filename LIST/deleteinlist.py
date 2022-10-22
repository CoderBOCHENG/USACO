list1 = []
list2 = [5,10,15,20]
list3=["ben","tom","tim","bob"]
elem = 2
if not list2:
    print("Empty List")
elif list2.count(elem) == 0:
    print("Empty List")
else:
    for i in range(list2.count(elem)):
        list2.remove(elem)
print(list2)
