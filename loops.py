#meow three times with while
i=0
while i <3:
    print("meow")
    i+=1

print("---------")


#for loop and lists
print("for loop and list")

for _ in range(3): # _ instead of i (means garbage in a way) to save memory and make code readable
    print("meoww")
#or
print("meowwwww\n"*3,end="")

print("---------")


#continue & break
while True:
    n=int(input("Whats n? "))
    if n>0:
        break

for _ in range(n):
    print("meoww")

print("---------")


#with functions
def meow(f):
    for _ in range(f):
        print("meow with function")

def get_number():
    while True:
        t=int(input("How many meows? "))
        if t>=1:
            return t
        
def main():
    meow(get_number())
main()

print("---------")

