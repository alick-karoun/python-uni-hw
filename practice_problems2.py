#problem11
Celcius=float(input("Temp in Celsius: "))
Fah=Celcius*9/5+32
print(f"Celsius: {Celcius}, Fahrenheit: {Fah}")

#problem12
rectangle_length=float(input("Length: "))
rectangle_width=float(input("Width: "))
area=rectangle_length*rectangle_width
perimeter=2*(rectangle_width*rectangle_length)
print(f" Area: {area}\n Perimeter: {perimeter}")

#problem13
year=int(input("Year: "))
if year%4==0 or 