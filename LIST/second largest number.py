list1 = [1,2,3,4]
list2 = [2,4,6,8]
list3 = [4,3,2,1]
list4 = [5,6,7,8]



new_list1 = set(list1)
new_list1.remove(max(new_list1))
print(max(new_list1))


new_list2 = set(list2)
new_list2.remove(max(new_list2))
print(max(new_list2))



print("second smllest number below")


new_list3 = set(list1)
new_list3.remove(min(new_list3))
print(min(new_list3))



new_list4 = set(list2)
new_list4.remove(min(new_list4))
print(min(new_list4))




new_list5 = set(list3)
new_list5.remove(min(new_list5))
print(min(new_list5))


new_list6 = set(list4)
new_list6.remove(min(new_list6))
print(min(new_list6))
