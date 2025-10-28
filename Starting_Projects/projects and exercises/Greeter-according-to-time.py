import time

current_time = time.strftime("%H:%M:%S")

print("current time is :", current_time)

hour = int(time.strftime("%H"))

minute = int(time.strftime("%M"))

second = int(time.strftime("%S"))

if hour < 12 :
    print("Good Morning")
elif hour >= 12 and hour < 18 :
    print("Good Afternoon") 
elif hour >= 18 and hour < 21:
    print("Good evening")
else :
    print("good night")


