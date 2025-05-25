# Looping over Dictionary
student = {"name": "Bishal", "age": 18, "field": "CS"}

print("loop type 1")
for key in student:
    print(f"{key}: {student[key]}")

print("\nloop type 2")
for key,value in student.items():
    print(f"{key}: {value}")

print("\nloop type 3")
for key in student.keys():
    print(f"{key}: {student[key]}")

# Looping over JSON
data = [
    {"name": "Bishal", "skills": ["Python", "ML"]},
    {"name": "Rita", "skills": ["Java", "Web"]}
]

for person in data:
    print()
    for key,value in person.items():
        if(key == 'skills'):
            for skill in person['skills']:
                print(f"skill: {skill}")

data = [
    {"name": "Bishal", "skills": ["Python", "ML"]},
    {"name": "Rita", "skills": ["Java", "Web"]}
]

for person in data:
    print(person["name"])
    for skill in person["skills"]:
        print(f"  - {skill}")

student = {
    "name": "Bishal",
    "marks": {
        "math": 90,
        "science": 92
    }
}

for subject, score in student["marks"].items():
    print(f"{subject}: {score}")


# for key in std.keys():
#     print(f"{key}: {std[key]}")
    
#     for mark in std['marks']:
#         print(f" {mark} ")
