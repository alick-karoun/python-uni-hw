def camel_case(text):
    camel= text.split()
    return camel[0].lower() + ''.join(word.capitalize() for word in camel[1:])

print(camel_case("hello world "))

print("-------------------")

#coke machine

def change_calc():
    amount_due = 50

    while amount_due > 0:
        print("Amount Due:", amount_due)
        given = int(input("Insert Coin: "))

        if given in [25, 10, 5]:
            amount_due -= given

    print("Change Owed:", -amount_due)
change_calc()

print("-------------------")

#twtter
text = (input("Input: "))
if text.lower() == "twitter":
    str(print("Output: Twtter"))
elif text.lower() == "whats your name":
    str(print("Output: Whats yr nm?"))