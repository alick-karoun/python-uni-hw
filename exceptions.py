#try, except, else
try:
    x=int(input("Whats x"))
except ValueError:
    print("x has to be an integer")

#with while

# while True:
#     try:
#         x=int(input("Whars ur x "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")

#function
def main():
    x=get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("give me ur x "))
        except ValueError:
            print("integer pls")

main()