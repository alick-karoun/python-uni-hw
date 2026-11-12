class Student:
    ...

def getStudentdict():
    name=input("Name: ")
    house=input("House: ")
    student = Student(name, house)
    return student

def main():
    student = getStudentdict()
    print(f"{student.name} from {student.house}")
    

if __name__== "__main__":
    main()
