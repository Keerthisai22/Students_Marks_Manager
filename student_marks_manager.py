marks=[]
n=int(input("Enter the number of subject="))
for i in range(n):
    m=int(input(f"Enter the marks{i+1}="))
    marks.append(m)
print("\n---------------STUDENT MARKS-----------------")
print("Total=",sum(marks))
print("Average=",sum(marks)/n)
print("Maximum=",max(marks))
print("Minimum=",min(marks))
