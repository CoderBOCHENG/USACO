list1 = [1,1,2,2,2,3,3,4,5,5,5,6,6]
list2 = ["a","a","a","b","b","c","c","c","d","d"]
list3 = [1,2,3,4,5]
list4 = ["tom","tom","ben","mike"]


'''
list1 = list( dict.fromkeys(list1) )
print(list1)


list2 = list( dict.fromkeys(list2) )
print(list2)


list3 = list( dict.fromkeys(list3) )
print(list3)


list4 = list( dict.fromkeys(list4) )
print(list4)
'''


no_duplicates = list(set(list1))
print(no_duplicates)




no_duplicates = list(set(list2))
print(no_duplicates)




no_duplicates = list(set(list3))
print(no_duplicates)



no_duplicates = list(set(list4))
print(no_duplicates)

