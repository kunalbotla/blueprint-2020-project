# takes the input/data of the user 
c = input("What did you consume?" + " A. Drive your car?" + " B. Did you eat food? (Type the letter w/ dot)")
if c == "A." :
    m = int(input("How many miles?"))
    g = m * 411
    print(g + "grams of carbon dioxide")

elif c == "B." : 
    input("What kind of food did you eat?")
else: 
    print("We currently do not support this option.")

