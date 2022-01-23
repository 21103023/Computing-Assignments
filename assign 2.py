#Que.1)
string= "Phython is a case sensitive language"
#a)
print(f"The length of the string is: {len(string)}\n")

#b)
print(f"The string in reverse order: '{string[::-1]}'\n")

#c)
sub_str= string[11:-9]
print(sub_str+ "\n")

#d)
print(string.replace("a case sensitive", "object oriented") +"\n")

#e)
print(f"The index  of substring 'a' is: {string.find('a')}\n")

#f)
print(f"The String with whitespace removed: '{string.replace(' ', '')}'\n")

#Que.2)
name= "Saurabh Pandey"
SID= 21103023
dep_name= 'CSE'
cgpa= 9.2
print(f"Hey, {name} Here!")
print(f"My SID is {SID}")
print(f"I am from {dep_name} deparment and my CGPA is {cgpa}\n")

#Que.3)
a=56
b=10
print(f"a={a}, b={b}")
print(f"a&b = {a&b}")
print(f"a|b = {a|b}")
print(f"a^b = {a^b}")
print(f"a<<2 = {a<<2}")
print(f"b<<2 = {b<<2}")
print(f"a>>2 = {a>>2}")
print(f"b>>2 = {b>>2}\n")

#Que.4)
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
num3=float(input("Enter the third number:"))
print("The greatest among above three numbers is:")
if num1>=num2 and num1>=num3:
    print(num1)
elif num2>=num1 and num2>=num3:
    print(num2)
else:
    print(num3)

#Que.5)
in_str= input("Enter your sentence:\n")

print(" Is the word 'name' present in the entered string:")

if in_str.lower().find('name')==-1:     #Checking for the word "name"
    print("No\n")
else:
    print("Yes\n")

#Que.6)
len1=float(input("Enter the first side length:"))
len2=float(input("Enter the second side length:"))
len3=float(input("Enter the third side length:"))

print("Is a triangle possible with above entered sides:")

if (len1+len2)>len3 and (len2+len3)>len1 and (len3+len1)>len2:
     print("Yes")
else:
    print("No")

