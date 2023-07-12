def task1 (): 
    print("Convert hours to minutes")
    numb = input()
    print(numb * 60)
    return numb

def task2 ():
    print("Type 1 for hours to minutes or 2 for minutes to hours")
    d = input()
    number = 0
    if d == 1:
        print("How many hours?")
        number = input()
        print(number * 60)
    elif d == 2:
        print("How many minutes?")
        number = input()
        print(number / 60)

    return number

def task3 ():
    print("Type any word and I'll tell you how many characters it is")
    word = input()
    print(len(word))

    return word

task3()