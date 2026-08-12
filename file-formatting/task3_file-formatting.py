# Task 3: File Formatting 
# The file student_record_v1.txt has 25 lines with no structure
# lines 1 to 5 = student IDs
# lines 6 to 10 = first names 
# lines 11 to 15 = last names
# lines 16 to 20 = campuses
# lines 21 to 25 = modes of study 
# This program reads that file, makes an email for each student,
# and writes a tidy version into student_record_v2.txt


# Open the original file and read every line into a list
file = open("student_record_v1.txt", "r")
all_lines = file.readlines()
file.close()

# Remove the newline character "\n" from the end of each line 
lines = []
for line in all_lines:
    line = line.strip()
    if line != "":
        lines.append(line)


# Split the list into 5 categories using slicing. 
# line[0:5] means "take items 0, 1, 2, 3, and 4"
student_ids = lines[0:5]
first_names = lines[5:10]
last_names = lines[10:15]
campuses = lines[15:20]
study_modes = lines[20:25]


# Make an email for each student 
# The format is firstname_lastname@yoobeecolleges.com in lower case
emails = [f"{first.lower()}_{last.lower()}@yoobeecolleges.com" for first, last in zip(first_names, last_names)]


# Put all the information for each student on one line 
formatted_data = []
for i in range(5):
    student_info = f"ID: {student_ids[i]}, Name: {first_names[i]} {last_names[i]}, Campus: {campuses[i]}, Mode: {study_modes[i]}, Email: {emails[i]}"
    formatted_data.append(student_info)

# Write the new lines into the second file 
# "w" means write, and it creates the file if it does not exist yet
with open("student_record_v2.txt", "w") as file:
    for line in formatted_data:
        file.write(line + "\n")


# Show the result on the screen so I can check it worked
print("student_record_v2.txt has been created:")
print()
for student_info in formatted_data: 
    print(student_info)