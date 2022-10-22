list1 = ["a","a","a","b","b","c"]
list2 =[1,2,3,4,5,5,4,3,2,1,2,33,1,1,1,4,5,5]
list3 =[1,2,2,3,3,3,4,4,4,4,5,5,5,5,"a",'b","c"]



freq_dict1 = {}
for elem in list1:
    if elem not in freq_dict1:
        freq_dict1[elem] = 1
    else:
        freq_dict1[elem] +=1
print(freq_dict1)






freq_dict2 = {}
for elem in list2:
    if elem not in freq_dict2:
        freq_dict2[elem] = 1
    else:
        freq_dict2[elem] +=1
print(freq_dict2)







freq_dict3 = {}
for elem in list3:
    if elem not in freq_dict3:
        freq_dict3[elem] = 1
    else:
        freq_dict3[elem] +=1
print(freq_dict3)


freq_dict4 = {}
list4 = list1+list2+list3
for elem in list4:
    if elem not in freq_dict4:
        freq_dict4[elem] = 1
    else:
        freq_dict4[elem] += 1
print(freq_dict4)
