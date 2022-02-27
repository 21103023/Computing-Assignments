#Que.1)
def toh(n, sr, ax, dt):
    if n>0:
        toh(n-1, sr, dt, ax)
        print("Move disk", n, "from source", sr, "to destination", dt)
        toh(n-1, ax, sr, dt)
    
print(toh(3, 'A', 'B', 'C'))        #Here we are moving all the discs from source peg A to destination peg C

#Que.2)
#By recursion
def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)
N=int(input("Enter the number of lines of pascal triangle you want:\t"))  
def pascal(n):
    if n>=0:
        print(" "*(n), end="")
        def line(r):
           if r>=0:
               print(fact(N-1-n)//(fact(r)*fact(N-1-n-r)), end=' ')
               line(r-1)
           else:
               print()
        line(N-1-n)
        pascal(n-1)
if N>0 :
    pascal(N-1)   
else:
    print("Invalid input") 
print("\n")

#By loops
if N>0:    
    for i in range(N):
        print(" "*(N-i-1), end="")
        if i==0 :
            print('1', end='')
        elif i>0 :
            for j in range(i+1):
                print(fact(i)//(fact(j)*fact(i-j)), end=' ')
        print()        
else:
    print("Invalid input")

#Que.3)
I_no=float(input("\nEnter the first number:"))
II_no=float(input("Enter the second number:"))

if II_no!=0 :
    #a)
    print("\nFunction is callable.")
    qut, rem=divmod(I_no, II_no)
    print(f"Quotient obtained={qut}\nReminder obtained={rem:.2f}")
    #b)
    if qut==0 :
        
        if rem==0 :
            print("Both value are zero.")
        else:
            print("Quotient is zero.")
            print("Reminder is non-zero.")
    else:
        
        if rem!=0 :
            print("Both values are non-zero.")
        else :
            print("Quotient is non-zero")
            print("Reminder is zero.")
    #c)
    lt=(qut, rem)+(4, 5, 6)
    print(lt)
    lt1=[]
    for i in lt:
        if i>4 :
            lt1.append(i)
    print("\nThe values which are greater than 4 are:", lt1)
    #d)
    print("\nConversion to set datatype:", set(lt1))
    #e)
    st=frozenset(lt1)
    print("\nMaking  the set immutable:", st)
    #f)
    print("\nThe maximum value from set is:", max(st))
    print("The hash value for the maximum value:", hash(max(st)))
else:
    print("Function is not callable.")

#Que.4)
class Student:
    def __init__(self, name, rollno):
        self.name=name
        self.rollno=rollno
        print("\nInstructor is called for assigning.")

    def __del__(self):
        print("Destructor is called and object deleted.\n")

st1=Student('saurabh', 23)
del st1


#Que.5)
class Details:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def show(self):
        print(f"{self.name}\t{self.salary}")
        
# storing details of employees
emp1=Details('Mehak', 40000)
emp2=Details('Ashok', 50000)
emp3=Details('Viren', 60000)
print("Name\tSalary")
emp1.show()
emp2.show()
emp3.show()

# updating salary
emp1.salary=70000
print("\nThe updated table")
print("Name\tSalary")
emp1.show()
emp2.show()
emp3.show()

#deleting the record of Viren
del emp3
print("\nRecord of Viren deleted.")

#que.6)
george=input('\nThe word spoken by George:\t').lower()
barbie=input('The word spoken by Barbie:\t').lower()
chk=list(george.replace(' ', ''))
chk1=list(barbie.replace(' ', ''))
if sorted(chk)==sorted(chk1):
    print("True friendship.")
else:
    print("Friendship is fake.")

