# Задание №3 - сделано
v = int(input('Speed: '))
t = int(input('Time: '))
speed_is_more_than_zero = v*t%100
speed_is_less_than_zero = v*t%100
if v >= 0:
    print(speed_is_more_than_zero)
else:
    print(speed_is_less_than_zero)