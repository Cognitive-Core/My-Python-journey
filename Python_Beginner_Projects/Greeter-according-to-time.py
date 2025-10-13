import time

current_time = time.strftime("%H:%M:%S")

hour = int(time.strftime("%H"))

minute = int(time.strftime("%M"))

second = int(time.strftime("%S"))

if hour < 12 :
    print("Good Morning")
elif hour >= 12 and hour < 18 :
    print("Good Afternoon") 
elif hour == 18 and minute >= 1 and minute <= 59:
    print("Good evening")
else :
    print("Good night")


