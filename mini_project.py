student_record = {
    "name": "manish piplode",
    "roll number": "10012",
    "marks": 98,
    "grade": "B",
}

student_record["marks"] = student_record["marks"] + 10

if student_record["marks"] > 90:
    student_record["grade"] = "A"
    
elif student_record['marks'] >= 75:
    student_record["grade"] = "B"

else:
    student_record["grade"] = "C"

if student_record["marks"] >= 40:
    student_record["result"] = "Pass"
else:
    student_record["result"] = "Fail"

for key, value in student_record.items():
    print(key, ":", value)
    
print(student_record["result"])    
print(student_record["grade"])    
print(f"{student_record['name']}, {student_record['roll number']}, {student_record['marks']}, {student_record['grade']}")