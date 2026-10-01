def print_brick(height):
    print("#\n"*height, end="") #print 3 bricks without for loops

def print_brick_horizontal(height):
    print("#"*height, end="") #print 3 bricks without for loops

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

def print_square2(sizee):
    for _ in range(sizee):
        print("#" * sizee)

def main():
    #print_brick(3)
    #print_brick_horizontal(3)
    print_square(4)
    print_square2(6)
main()

