def may(a):
    a=a+1
    return a

print(may(8))

print("-------------------")
'''
1. function with non parameter and non retunr
2. function wuth paramter and non retunrn
3. function with non paramter and return
4. function with paramter and return both

'''

#1
def welcome():
    print("welcome to ai llm")
    
print("-------------------")

#2

def may():
    a =17
    b=1
    c=a+b
    return c
print(may())

print("-------------------")
#3

def login(uid, pw):
    print("enter uid", uid)
    print("enter pw", pw)
    print("login")
login("maysup","1718")

#4

def checkstatus(expected, actual):
    return expected == actual

result = checkstatus(100,101)
print(result)

# * is wild card symbol

def display(*a):
    print(a)

display(1, 2, 3, 4, 5)

