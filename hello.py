#! /usr/bin/env python3

times = 4
place = "world"
try:
    for x in range(0,times):
        progress = x / (times - 1)
        if (x < (times -1)):
            print("Hello" + place + "!")
        else:
            print("Goodbye" + place + "!")
except:
    print("Done!")

print(type(times))
print(type(place))
print(type(progress))

