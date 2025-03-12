student={"name": "Omar", "age": 29, "specialization": ["AI", "Big Data"]}
print(type(student))
print(student["age"])
print(student.keys())  # name, age, specialization
print(student.values()) # Omar, 29, [AI, Big Data]
print(student.items())  # both
#print(student["advisor"]) #error
student2={"name": "Omar", "age": 31, "specialization": "Computer Science", "advisor":"Hanaa Talei"}
print(student2["advisor"])
