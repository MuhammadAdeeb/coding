number = input("What is the number you will like to convert? ")
number = int(number)  # number inputted that needs to be converted to binary
og = number

# 6-9: Used if number entered is negative
negNum = 0
if number < 0:
    negNum = number
    number = abs(number)

done = False
n = 2     # Used to figure out bits: 2^n
bits = 0  # number of binary bits: Ex: 1010 has 4 bits

answer = ''  # Binary answer

if number == 0 or number == 1:  # if input decimal number is 0 or 1, answer = '0' or '1' accordingly

    if number == 0:
        answer = answer + '0'
    else:
        answer = answer + '1'
else:

    # This while loop is to figure out how many bits are required by the number in binary
    while done is False:
        if 2**n > number:  # 2^4 > 10...tells you bits = 4:
            bits = n
            done = True    # To exit while loop cuz don't need it anymore
        else:  # increment n until 2^n is greater than number(input)
            n += 1

    n -= 1
    x = 1

    # While loop: To create the binary answer:
    while x < (bits + 1):
        if 2**n <= number:  # if 2^n <= number than this 2^^n is True (1)
            answer = answer + '1'
            number = number - 2**n  # Ex: 10 -> 1 _ _ _  so subtract 8(2^3) from 2 to figure out the rest of the 3 bits
        else:
            answer = answer + '0'

        x += 1
        n -= 1

# Following code is to convert the binary (answer) to two's complement for negative numbers
# Works incorrectly: 10 = 01011 when it should be 10110
answerTwo = answer
if negNum != 0:

    sog = '0' + answerTwo  # add 0 to beginning of the answer

    temp = 5
    size = len(sog)

    current = size - 1
    aList = []

    # append each char in sog('0' + answer) to aList individually
    for i in sog:
        aList.append(i)

    # change the last char to its opposite:
    if aList[current] == '1':
        aList[current] = '0'
        temp = 2
    else:
        aList[current] = '1'
        temp = 0

    current -= 1
    while current != -1:
        if temp == 2:
            if aList[current] == '1':
                aList[current] = '0'
                current -= 1
            else:
                aList[current] = '1'
                temp = 0
        else:
            break

    final = ''
    for i in aList:
        final = final + i
    print("{} in binary is {}".format(negNum, final))

if negNum == 0:
    print("{} in binary is {}".format(og, answer))

