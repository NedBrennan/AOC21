import day3Import as i
array = i.array


def day3_1(array) :

    history = [0] * 12

    for num in array :
        loc = 0

        for n in num :
            if n == "0" :
                history[loc] -= 1
            elif n == "1" :
                history[loc] += 1
            loc += 1
    history = history[::-1]
    loc = 0
    gamma = 0
    epsilon = 0

    for num in history :
        print(loc)

        if num > 0 :
            gamma += (2 ** loc)
            print(2 ** loc, loc)
            loc += 1
        else :
            epsilon += (2 ** loc)
            print(2 ** loc, loc)
            loc += 1


    print("Solution (solved):", gamma * epsilon)

def day3_2(array, pos, char) :

    arrayOne = []
    arrayTwo = []

    for num in array :
        
        if num[pos] == "1" :
            arrayOne.append(num)
        else :
            arrayTwo.append(num)

    if char == "one" :
        if len(arrayOne) > len(arrayTwo) :
            day3_2(arrayOne, pos + 1, char)
        elif len(arrayOne) < len(arrayTwo) :
            day3_2(arrayTwo, pos + 1, char)
        else :
            day3_2(arrayOne, pos + 1, char)
    else :
        if len(arrayOne) > len(arrayTwo) :
            day3_2(arrayTwo, pos + 1, char)
        elif len(arrayOne) < len(arrayTwo) :
            day3_2(arrayOne, pos + 1, char)
        else :
            day3_2(arrayTwo, pos + 1, char)



oxygen = day3_2(array, 0, "1", 0)
co2 = day3_2(array, 0, "0", 0)

print(oxygen ** co2)