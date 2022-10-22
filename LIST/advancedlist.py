list1=[2,4,6,8,10]
list2=[1,2,3,4,5,6,7,8,9,10]
list3=[1,3,5,7,9]
list4=[]
list5=["a","b","c","d"]
list6=["c","d","e","f"]
list7=["ben","tim","bob","jim"]
list8=["tim","ben","tom","mike"]




difference1 = []
for elem in list2:
    if elem not in list1:
        difference1.append(elem)
print(difference1)



difference2 = []
for elem in list2:
    if elem not in list3:
        difference2.append(elem)
print(difference2)






difference3 = []
for elem in list8:
    if elem not in list7:
        difference3.append(elem)
print(difference3)



difference4 = []
for elem in list1:
    if elem not in list2:
        difference4.append(elem)
else:
    print("Empty List")

print(difference4)
