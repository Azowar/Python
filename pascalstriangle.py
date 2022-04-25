def pascaltriangle(rows):
    array = [1]
    array2 = []
    spaces = rows - 1
    numbercount = 1
    for whatrow in range(rows):
        for _ in range(spaces):
            print(" ", end="")
        if whatrow % 2 == 0:
            for number in range(len(array)):
                if number == 0:
                    array2.append(1)
                try:
                    array2.append(array[number] + array[number + 1])
                except:
                    array2.append(array[number] + 0)
            for i in array:
                print(i, "", end="")
            array.clear()
        if whatrow % 2 == 1:
            for number2 in range(len(array2)):
                if number2 == 0:
                    array.append(1)
                try:
                    array.append(array2[number2] + array2[number2 + 1])
                except:
                    array.append(array2[number2] + 0)
            for x in array2:
                print(x, "", end="")
            array2.clear()
        print("")
        numbercount += 1
        spaces-=1

pascaltriangle(10)