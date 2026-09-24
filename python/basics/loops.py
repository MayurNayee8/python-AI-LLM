'''

for i in range(1,10):
 print(i)
'''
'''
for i in range(1,10,2):
  print(i)

for n in range(17):
   print(n)

list = [1,2,3,4,5]
for i in range(len(list)):
    print(i)

list2 = [1,"sup","may","python"]
for ele in list2:
    print(ele)

'''    



print("_________________")

for m in range(5):
 if m==3:
    break
 print(m)

print("_________________")

i=1
while i<6:
 print(i)
 i = i+1

print("_________________")

attempt = 0
username = "maysup"

while attempt<=3:
   if (username =="maysup"):
      print("welcome"+ username)
      break;
else: 
     print("Wrong username")

print("_________________")

str = '''this is python string
write a program to print only vowel part of the string'''

vowel = "aeiouAEIOU"


# if char is aeiou : print char

for char in str:
   if char in vowel:
      print(char, end="")
      
print()

print("_________________")

str = '''this is python string
write a program to print only vowel part of the string'''

vowel = "aeiouAEIOU"
i = 0
while i < len(str):
    char = str[i]   # Get the character at the current position
    
    if char in vowel:       # Check if it is a vowel
        print(char, end="")  # Print it without jumping to a new line
        
    i += 1     


   