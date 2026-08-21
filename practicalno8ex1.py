# Name Sanitizer Script

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Remove extra spaces and convert to title case
first_name = first_name.strip().title()
last_name = last_name.strip().title()

# Combine first and last name
full_name = first_name + " " + last_name

print("Clean Full Name:", full_name)