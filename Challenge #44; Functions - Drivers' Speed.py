'''
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”
'''
limit = 70
speed = int(input("Speed(Km): "))
def demerit_point_sys():
    demerit_point = (speed - limit) / 5
    if demerit_point <= 12:
        print("Points:" + str(demerit_point))
    else:
        print("Liscence Suspened")
def speed_test(speed):
    if speed < 70:
        print("Okay")
    elif speed >= limit:
          demerit_point_sys()
speed_test(speed)