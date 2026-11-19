class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house
        

    def __str__(self): #if we dont have this, the objects address will be printed out
        return f"{self.name} from {self.house}"

    @property #Getter
    def house(self):
        return self._house
    
    @house.setter #Setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("missing name")
        self._name=name


def get_student():
    name=input("Name: ")
    house=input("House: ")
    return Student(name,house)


def main():
    student=get_student()
    student._house="Number Four, Privet Drive"
    print(student)
main()
