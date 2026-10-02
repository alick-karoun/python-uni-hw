def fuel_gauge():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            
            if x > y:
                continue
                
            percentage = round((x / y) * 100)
            
            if percentage <= 1:
                print("E")
            elif percentage == 100:
                print("F")
            else:
                print(f"{percentage}%")
                
            break  #meghry

        except (ZeroDivisionError, ValueError):
            pass


def main():
    fuel_gauge()


main()