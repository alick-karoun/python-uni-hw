#list
students_list = ["Hermoine", "Harry", "Ron"]

#print the length of the list
for i in range(len(students_list)):
    print(i+1, students_list[i])

print("--------------")

#dictionary
students_dict=[
    {"name" : "Hermoine", "house":"Gryffindor", "patronus":"Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house":"Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus":None},
]



#prints keys and values seperately 
#for key alone just print student 
for student in students_dict:
    print(student["name"], student["house"], student["patronus"],sep=", ")