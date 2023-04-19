def wind_speed(distance, time):
    speed = distance / time
    if speed > 30:
        print("Сильный ветер!")
    else:
        return speed

print(wind_speed(500, 10)) # 50.0
