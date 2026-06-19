marks = int(input("Enter the marks: "))
attendance = int(input("Enter the attendance percentage: "))

if marks >= 80 and attendance >= 75:
    print("Excellent student.")
elif marks >= 50 and attendance >= 60:
    print("Average student.") 
else:
    print("Needs improvement.")