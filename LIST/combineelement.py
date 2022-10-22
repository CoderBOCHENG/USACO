list1 = [1,2,3,4]
list2 = [2,4,6,8]
list3 = [4,3,2,1]
list4 = [5,6,7,8]

common_elem = []
for elem in list1:
    if elem in list3:
        common_elem.append(elem)
print(common_elem)


common_elem = []
for elem in list4:
    if elem in list2:
        common_elem.append(elem)
print(common_elem)
