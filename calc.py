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
