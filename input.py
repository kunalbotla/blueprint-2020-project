x = "A"

# takes the input/data of the user 
c = input("What did you consume?" + " A. Drive your car?" + " B. Did you eat food? (Type the letter w/ dot)")
if c == "A." :
    m = int(input("How many miles?"))
    g = m * 411
    print(g , "grams of carbon dioxide")

elif c == "B." : 
    x = input("What kind of food did you eat? A. Vegetables B. Meat (Type the letter w/ dot)")
    if (x == "A.") : 
        y = int(input("How many kilos?"))
        z = y * 2000
        print(z , "grams of carbon dioxide")
elif (x == "B.") :
        y = int(input("How many kilos?"))
        z = y * 18300
        print(z , "grams of carbon dioxide")
else: 
    print("We currently do not support this option.")

