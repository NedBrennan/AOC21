import day1Import as dayImport


def depthFinder(depthArray) :

    last = False
    count = 0


    for depth in depthArray :
        if last :
            if last < depth :
                count += 1
        else :
            last = depth
            print('first')

        last = depth

    
    print(count)

def depthFinder2(depthArray) :

    last = False
    count = 0
    pos = 0

    for depth in depthArray :

        try :
            next = depthArray[pos] + depthArray[pos + 1] + depthArray[pos + 2]

            if last :
                if next > last :
                    count += 1
                    print(next, "greater than", last)
            else :
                last = next
                print('first')

            last = next
            pos += 1

        except :
            pos += 1
            print('end')
    
    print(count)

depthFinder2(dayImport.array)