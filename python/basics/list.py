'''
list - []
tuple - ()
set - {}
dictonary - {key:value}

list: is collectio of diff data, datatype of date can be diffrent
seperated by , in []

its ordered collection - same order always

set - unordered collection
'''


list = [1,"may",3,87,4,3,4]
print(list)
print(list[2:5])

for ele in list:
    print(ele)

#update
list[1] = "sup"
print(list[1])


#delete by index

del list[0]
print(list)

#delete by direct element, remove 1st occurance if duplicate

list.remove(4)
print(list)

# delete by pop method

list.pop()
print(list)

list.pop(1)
print(list)

#append

list.append(8)
print(list)

list.insert(1, "may")
print(list)

list2 = [1,2,3,4]
print(list2)
list2.clear()
print(list2)

print("-------------")

set = {1,"may",3,87,4,3,1,7,88,67,45,66,66}
print(set)