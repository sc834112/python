# Student Score Filter and Update Program

grades = [85, 90, 78, 92, 88]

print("Original grades:", grades)

index = int(input("Enter the index position to update: "))
new_grade = int(input("Enter the new grade: "))

if 0 <= index < len(grades):
    grades[index] = new_grade
    print("Corrected grades list:", grades)
else:
    print("Invalid index position!")