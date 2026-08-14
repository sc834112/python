# Eligibility Checker System

age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

if age >= 17:
    if marks >= 50:
        print("Eligible for Admission")
    else:
        print("Not Eligible: Marks are below 50%")
else:
    print("Not Eligible: Age is below 17 years")