aqi = 0.0
pm = 0.0
smoke = 0.0

print("what is the air quality index where you are? (enter in aqi)")
aqi = input ()
print("")

if float(aqi) <= 12:
    pm = 50
elif float(aqi) <= 35.5:
    pm = 100
elif float(aqi) <= 150:
    pm = 55.5
elif float (aqi) <= 200:
    pm = 150.5
elif float (aqi) <= 300:
    pm = 250.5
elif float (aqi) <= 400:
    pm = 350.5
else:
    print("too high to calc")

print("your PM2.5 (Particulate <2.5 microns) (in µg/m3) is:")
print(pm)
print("")

smoke = pm/22
print("this means that every day you are exposed to effectivly:")
print(smoke)
print("cigarettes")
