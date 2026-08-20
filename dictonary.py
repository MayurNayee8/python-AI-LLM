dicto = {"name": "sup", "name2": "may", 1: 34, 2: 33}
print(dicto)
print(dicto["name"])
print(dicto.get(1))

print(dicto["name2"])
print(dicto.get(2))


print(dicto.keys())
print(dicto.values())

print(dicto.items())


# input - "abcdbcdabcd" - write a program to print the result as 
# output - a3b3c3d3 how many time each letter display

for ele in dicto:
    print(ele)

for ele2 in dicto:
    print(ele2, dicto[ele2])

for value in dicto.values():
    print(value)

for item in dicto.items():
    print(item)

for key, value in dicto.items():
    print(key, value)

dicto["name3"] = "love"
dicto[2] = 34 #update value as key already there
print(dicto)

dicto2 = {"sf" : "edd", 1: 44, "we": "maysup", 2: 45}
print(dicto2)

# del to delete

del dicto2["sf"]
print(dicto2)

dicto2.pop(1)
print(dicto2)

dicto2.popitem()
print(dicto2)