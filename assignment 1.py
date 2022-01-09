#ASSIGNMENT-1
#Que.1
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
num3=float(input("Enter the third number:"))
avg=(num1 + num2 + num3)/3
print("The average of the three numbers:")
print( avg)

#Que.2
std_deduction=10000
dep_deduction=3000
g_income=float(input("Enter the gross income:"))    # The Gross income of the person
dependents=int(input("Enter the no of dependents:"))# Number of dependents of the person
tax_income=float(g_income - std_deduction - (dep_deduction*dependents))
tax=tax_income*0.2
print("The person's income tax is:")
print(float(tax))

#Que.3
SID=21103023
name="Saurabh Pandey"
gender='M'
course="Computer Science And Engineering"
CGPA=8.5
student=[SID, name, gender, course, CGPA]
print(student)

#Que.4
marks=[]
marks.extend([34, 56, 90, 98, 59])    #marks of the five students
marks.sort()                            #marks arranged
print("Marks in sorted manner of the students:")
print(marks)

#Que.5
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# a) part
color.pop(3)    #Black is removed
print(color)

# b) part
color[3:4]=['Purple']   #Black and Pink are replaced by Purple
print(color)
