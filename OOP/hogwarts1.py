
def getStudent():
    name=  input("Name: ")
    house= input("House: ")
    #return (name, house) #tuple, immutable, you cant change unlike lists
    return [name, house]

def main():
    student = getStudent()
    if student[0] =="Padma":
        student[1]= "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

    
if __name__== "__main__":
    main()
