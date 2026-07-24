students = {
    1: {"name": "Gaurav", "course": "Data Science", "city": "Mumbai"},
    2: {"name": "Tanmay", "course": "Financial Markets", "city": "Banglore"},
    3: {"name": "Rohan", "course": "Psychology", "city": "Pune"},
    4: {"name": "Vidit", "course": "Commerce", "city": "Gujrat"},
    5: {"name": "Rahul", "course": "AI", "city": "Delhi"}
}

for student in students.values() :
    print (student['name'])


print(f"Welcome {student['name']}")
