import time

current_time = time.strftime("%H:%M:%S")

hour = int(time.strftime("%H"))

if hour < 12 :
    print("Good Morning")
elif hour >= 12 and hour < 18 :
    print("Good afternoon") 
elif hour == 18 :
    print("Good evening")
else :
    print("Good night")


