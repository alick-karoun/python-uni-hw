def square(n):
    return n*n
def main():
    x=int(input("Enter ur number "))
    print("x squared is", square(x))

if __name__ == "__main__":    #if we are coding with more than one file we must write this if we want to use the square function in another function, so the main is not used during import
    main()