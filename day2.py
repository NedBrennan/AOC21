import day2Import as i
array = i.array


def day2_1(array) :
    
    horizontal = 0
    vertical = 0
    
    for change in array :
        
        direction = change[0]
        value = int(change[-1])

        if direction == "f" :
            horizontal += value
        elif direction == "u" :
            vertical -= value
        else :
            vertical += value

    print("Solution (solved): ", vertical * horizontal)


def day2_2(array) :
        
    horizontal = 0
    vertical = 0
    aim = 0
    
    for change in array :
        
        direction = change[0]
        value = int(change[-1])

        if direction == "f" :
            horizontal += value
            vertical += (value * aim)
        elif direction == "u" :
            aim -= value
        else :
            aim += value

    print("Solution (solved): ", horizontal * vertical)

day2_1(array)
day2_2(array)