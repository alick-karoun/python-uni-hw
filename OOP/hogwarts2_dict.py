def getStudentdict():
    student={}
    name=input("name: ")
    house=input("House: ")
    return {"name": name, "house": house}

def main():
    student = getStudentdict()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")
    


if __name__== "__main__":
    main()
