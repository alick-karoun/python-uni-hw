names=[]

# for _ in range(3):
#     user_input=input("Enter ur name: ")
#     names.append(user_input)

# for i in sorted(names): 
#     print(f"hello {i}")


name=input("Your name: ")

#---------------------------
#USING JUST OPEN

# file= open("names.txt", "w") #write mode, only one name
# file = open("names.txt", "a")
# file.write(f"{name} \n") #write inside the file
# file.close()

#---------------------------
#USING WITH (CONEXT MANAGER)

with open("names.txt", "a") as file:
    file.write(f"{name}\n")    #closes automatically


with open("names.txt") as file:  #read mode
    lines = file.readlines()     #read lines
# for line in lines:
#     print("hello", line.rstrip()) #removes the extra line
    
    
#----------------------------
#APPEND NAMES TO A LIST FOR SORTING

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}")
