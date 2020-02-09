from datetime import datetime
now = datetime.now()
hour = now.hour
military = hour + 12
from datetime import date
today = date.today()
day = today.day
month = today.month
x = 9
day_plus = int(day) + 0
difference = day_plus - x
while day < 12:
# different notification that will appear on user's phone each day in the morning
  if hour < 12:
  if hour == 6:
  elif difference == 0:
    print("Climate change may end the world in 2030.")
    print("Make sure to bring your reusable water bottle to school or work today.")
    a = input("Did you bring your reusable water bottle to school or work today?")
    if a == "yes":
      print("Great job!")
  elif difference == 1:
    print("Scientists predict that if the increase in greenhouse gas emissions continues unabated, temperatures will rise by as much as 10 degrees Fahrenheit by the end of this century.")
    print("Try not to use plastic today.")
    
    b = input("Did you not use plastic today?")
      if b == "yes":
        print("That's great!")
  elif difference == 2:
    print("The ocean absorbs approximately 26% of the CO2 added to the atmosphere from human activities each year.")
    print("Try to find a efficient way for transportation today.")
    
    c = input("Did you find an efficient way for transportation today?")
    if c == "yes":
        print("You are the best!")
  elif difference == 3:
    print("Global warming may also lead to extreme weather other than cold or heat extremes.")
    print("Use less heating and natural gas today")
    
    d = input("Did you use less heating and natural gas today?")
    if d == "yes":
        print("Thank you!")
  if hour > 12:
  if hour == 18: