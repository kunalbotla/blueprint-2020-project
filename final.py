#input program
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



#calc program
aqi = 0.0
pm = 0.0
smokeDay = 0.0
smokeWeek = 0.0
smokeMonth = 0.0

print("what is the air quality index where you are? (enter in aqi)")
aqi = input()
print("")


if float(aqi) <= 50:
    pm = 12
elif float(aqi) <= 100:
    pm = 35.5
elif float(aqi) <= 150:
    pm = 55.5
elif float(aqi) <= 200:
    pm = 150.5
elif float(aqi) <= 300:
    pm = 250.5
elif float(aqi) <= 400:
    pm = 350.5
else:
    print("too high to calc")

print("your PM2.5 (Particulate <2.5 microns) (in µg/m3) is:")
print(pm)
print("")

smokeDay = pm / 22
print("this means that every day you smoke effectivly:")
print(smokeDay, "cigarettes")

print("")

smokeWeek = 7 * smokeDay
print("this means that every week you smoke effectivly:")
print(smokeWeek, "cigarettes")

print("")

smokeMonth = 30 * smokeDay
print("this means that every month you smoke effectivly:")
print(smokeMonth,  "cigarettes")

print("")

print("note: numbers are not 100% accurate")
