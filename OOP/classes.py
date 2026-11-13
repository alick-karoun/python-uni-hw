class Student:
    def __init__(self,name,house, patronus = None): #dunder method, this is an initializer
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindo", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self): #we pass self so we use the attributes without having to write everything
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack russell terrier":
                return "🐶"
            case _: #anything else
                return "🪄"


def getStudentdict():
    name=input("Name: ")
    house=input("House: ")
    patronus=input("Patronus: ") or None
    return Student(name, house, patronus)

def main():
    student = getStudentdict()
    print("Expecto Patronum!")
    print(student.charm())
    

if __name__== "__main__":
    main()
