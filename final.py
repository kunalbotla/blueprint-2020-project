#input program
x = "A"

# takes the input/data of the user 
c = input("What did you consume?" + " A. Drive your car?" + " B. Did you eat food?")
if c == "A" :
    m = int(input("How many miles?"))
    g = m * 411
    print(g , "grams of carbon dioxide")

elif c == "B" : 
    x = input("What kind of food did you eat? A. Vegetables B. Meat")
    if (x == "A") : 
        y = int(input("How many kilos?"))
        z = y * 2000
        print(z , "grams of carbon dioxide")
    elif (x == "B") :
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







#final program
from datetime import datetime
now = datetime.now()
hour = now.hour
from datetime import date
today = date.today()
day = today.day
month = today.month
points = 0
x = 9
day_plus = int(day) 
difference = day_plus - x
def convert24(str1): 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2]    
    elif str1[-2:] == "AM": 
        return str1[:-2]   
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
    else: 
        return str(int(str1[:2]) + 12) + str1[2:8]        
x = convert24("06:00:00 AM")
y = convert24("04:00:00 PM")
# different notification that will appear on user's phone each day in the morning. Using AI, we can figure out when typically the person checks his phone in the morning and in the night.
if hour == x[1]:
  animals = 0
  if difference == 0:
    print("Climate change may end the world in 2030.")
    print("Make sure to bring your reusable water bottle to school or work today.")
    points 
  elif difference == 1:
    print("Scientists predict that if the increase in greenhouse gas emissions continues unabated, temperatures will rise by as much as 10 degrees Fahrenheit by the end of this century.")
    print("Try not to use plastic today.")
  elif difference == 2:
    print("The ocean absorbs approximately 26% of the CO2 added to the atmosphere from human activities each year.")
    print("Try to find a efficient way for transportation today.")
  elif difference == 3:
    print("Global warming may also lead to extreme weather other than cold or heat extremes.")
    print("Use less heating and natural gas today")
if int(hour) == int(y[0:2]):
  animals = 1
  if difference == 0:
    a = input("Did you bring your reusable water bottle to school or work today?")
    if a == "yes":
      print("Great job!")
      points += 100
  elif difference == 1:
    b = input("Did you not use plastic today?")
    if b == "yes":
      print("That's great!")
      points += 100
  elif difference == 2:
    c = input("Did you find an efficient way for transportation today?")
    if c == "yes":
      print("You are the best!")
      points += 100
  elif difference == 3:
    d = input("Did you use less heating and natural gas today?")
    if d == "yes":
      print("Thank you!")
      points += 100
print("Score:" , points)
#https://www.geeksforgeeks.org/python-program-convert-time-12-hour-24-hour-format/
# points will be connected to a sponsore which will give a reward when the user reaches a certain amount of points(for motivation)