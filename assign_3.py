#Que.1)
in_sen=input("Enter the sentence:")
lt=in_sen.split()
if len(lt)>1 :
    st=set(in_sen.split())
    for word1 in st :
        print(f"Number of occurance of {word1} is:{in_sen.count(word1)}")
elif len(lt)==1:
    st1=set()
    for ch in in_sen.replace(" ", "") :
        st1.add(ch)
    for ltr in st1:
        print(f'''The occurance of letter '{ltr}' is: {in_sen.count(ltr)}''')
else:
    print("You have not entered any sentence.")

#Que.2)
day=int(input('\nEnter the day:'))
month=int(input('Enter the month:'))
year=int(input('Enter the year:'))

if 1<=day<=31 and 1<=month<=12 and 1800<=year<=2025 :
         if month in (1,3,5,7,8,10,12):
             if 1<=day<=30:
                 print(f"The next date: {day+1}/{month}/{year}")
             elif month!=12 :
                 print(f"The next date: 01/{month+1}/{year}")
             else:
                 print(f"The next date: 01/01/{year+1}")
         elif month!=2:
              if 1<=day<=29:
                 print(f"The next date: {day+1}/{month}/{year}")
              else:
                 print(f"The next date: 01/{month+1}/{year}")
         else:
              if 1<=day<=27:
                 print(f"The next date: {day+1}/{month}/{year}")
              elif day==28 and year%4==0:
                 print(f"The next date: {day+1}/{month}/{year}")
              elif day==29 and year%4==0 :
                 print(f"The next date: 01/{month+1}/{year}")
              elif day==28:
                 print(f"The next date: 01/{month+1}/{year}")
              else :
                 print("Invalid date input!!")
else :
    print("Invalid date input!! ")

#Que.3)
lt= [2,4,6,8,9]
lt1=[]
for i in range(len(lt)):
               (a,b)=(lt[i], lt[i]**2)
               lt1.append((a,b))
print(f"\nDesired output:{lt1}\n")

#Que.4)
gr_pt = int(input("Enter the grade points obtained:"))
if gr_pt in range(4,11):
    
    dict1={10:{'gr':'A+', "pr":"Outstanding"},
           9:{'gr':'A', "pr":"Excellent"},
           8:{'gr':'B+', "pr":"Very Good"},
           7:{'gr':'B', "pr":"Good"},
           6:{'gr':'C+', "pr":"Average"},
           5:{'gr':'C', "pr":"Below Average"},
           4:{'gr':'D', "pr":"Poor"}}
    print(f"Your grade is {dict1[gr_pt]['gr']} and {dict1[gr_pt]['pr']}.\n")
else:
    print("No marking for entered grade points.\n")

#Que.5)
s="ABCDEFGHIJK"
k=11
for i in range(6):
    print(' '*i + s[:k])
    k-=2

#Que.6)
print()
dict1={}
while True:
     name=input("Enter the name:").capitalize()
     SID=int(input("Enter the SID:"))
     dict1[SID] = name
     if input('''If you want to feed more details type "Y" else "N":''').upper() =='Y':
         continue
     else:
        print(f"Students details are as follows: (SID, Student name) \n{list(dict1.items())}")
        print(f"\nSorted dictionary by student name:{sorted(dict1.items(), key= lambda v:(v[1]))}")
        print(f'\nSorted dictionary by SID: {sorted(dict1.items())}')
        search_SID=int(input("\nEnter the SID whose name you want to know:"))
        if search_SID in dict1:
            print(f"The name of the student with SID {search_SID} is :{dict1[search_SID]}\n")
        else:
            print("Enter the SID from the data you created.\n")
        break

#Que.7)
t_sum=0
i=0
j=1
k=1
N=int(input("Number of terms in the resultant Fibonacci Series will be:"))
if N>=1:
    while k<=N :
        print(i, end=",")
        t_sum+=i
        s=i+j
        j=i
        i=s
        k+=1
    print(f'\n\nThe sum of the resultant fibonacci series:{t_sum}')
    print(f"The average of the resultant Fibonacci series:{(t_sum/N):.2f}")
else:
    print("Invalid input.\n") 

#Que.8)
set1={1, 2, 3, 4, 5}
set2={2, 4, 6, 8}
set3={1, 5, 9, 13, 17}
print(f"\nset1={set1}\nset2={set2}\nset3={set3}")
print(f"\nSet of all elements that are in set1 and set2 but not in both: {set1^set2}")
set4=(set1|set2|set3)- ((set1&set2)|(set1&set3))  
print(f"\nSet of all elements that are in only one of the three sets set1, set2 and set3 is: {set4}")
print(f"\nSet of elements that are in exactly two of the sets set1, set2 and set3:{(set1|set2|set3)-set4}")
print(f"\nSet of all integers in the range 1 to 10 that are not in set1:{set(range(6,11))}")
print(f"\nSet of all integers in the range 1 to 10 that are not in set1, set2 and set3:{set(range(1,11))-(set1|set2|set3)}")
