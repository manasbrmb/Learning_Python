import time
xtime = time.strftime('%H:%M:%S')
timestamp = int(time.strftime('%H'))
name=input("Enter your name :")
print ("current time",xtime)
if timestamp>22:
    print ("good night",name)
elif timestamp>17 and timestamp<22:
    print("Good Evening",name)
elif timestamp>4:
    print ("Good Morning")

else: ("Hows your day")
print("task done")
