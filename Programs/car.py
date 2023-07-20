command = ''
i = 1
speed = 1
road = '_____________________________________________________________________'
car = '{@@#}'
car_on_road = road[:1] + car + road[2:]
is_start = False
is_stop = True

while True:
    command = input('> ').lower()
    if command == 'help':
        print("""
start - to start the car
stop  - to stop the car
drive - to drive the car
speed - to speed up the car
exit  - to exit the car
        """)
    elif command == 'start':
        if not is_start:
            is_start = True
            is_stop = False
            print('Engine on broom!')
            print(car_on_road)
        else:
            print('The engine is currently on')
    elif command == 'stop':
        if not is_stop:
            is_start = False
            is_stop = True
            print('Engine off')
            print(car_on_road)
        else:
            print('The engine is currently off')
    elif command == 'speed':
        if not is_stop:
            speed = speed + 1
            print('Speed up ' + str(speed))
        else:
            print('Start the engine')
    elif command == 'speed input':
        if not is_stop:
            speed = int(input('Input a speed: '))
        else:
            print('Start the engine')
    elif command == 'drive':
        if not is_stop:
            if not i >= len(road):
                i = i + speed
                car_on_road = road[:i] + car + road[i + 1:]
                print(car_on_road)
            else:
                print('This is the end')
        else:
            print('Start the engine')
    elif command == 'exit':
        break
    else:
        print('Invalid command try again')
