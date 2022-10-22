list1 = [ 2,3,5,7,8,10]
list2 = [ 1,3,4,6,7,9]

add_list = []
for i in range(0,len(list1)):
    add_list.append(list1[i] + list2[i])
print(str(add_list))





substract_list = []
for i in range(0,len(list1)):
    substract_list.append(list1[i] - list2[i])
print(str(substract_list))



divide_list = []
for i in range(0,len(list1)):
    divide_list.append(list1[i] / list2[i])
print(str(divide_list))




times_list = []
for i in range(0,len(list1)):
    times_list.append(list1[i] * list2[i])
print(str(times_list))
