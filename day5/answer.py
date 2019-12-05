
def main():
    with open('input.txt') as f:
        a = f.readline().split(",")
        arr = [int(e) for e in a]
        #arr = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        opPos = 0
        while True:

            opParam = arr[opPos] #1002
            opInstruct = abs(opParam) % 100
            #print(arr)
            if opInstruct == 1:
                param1mode = get_digit(opParam, 2)
                param2mode = get_digit(opParam, 3)
                if param1mode == 0:
                    c = arr[opPos + 1]
                    add1 = arr[c]
                elif param1mode == 1:
                    add1 = arr[opPos + 1]
                if param2mode == 0:
                    c = arr[opPos + 2]
                    add2 = arr[c]
                elif param2mode == 1:
                    add2 = arr[opPos + 2]
                store = arr[opPos + 3]
                arr[store] = add1 + add2
                opPos = opPos + 4
            if opInstruct == 2:
                param1mode = get_digit(opParam, 2)
                param2mode = get_digit(opParam, 3)
                if param1mode == 0:
                    c = arr[opPos + 1]
                    mult1 = arr[c]
                elif param1mode == 1:
                    mult1 = arr[opPos + 1]
                if param2mode == 0:
                    c = arr[opPos + 2]
                    mult2 = arr[c]
                elif param2mode == 1:
                    mult2 = arr[opPos + 2]

                store = arr[opPos + 3]
                arr[store] = mult1 * mult2
                opPos = opPos + 4
            if opInstruct == 3:

                val = input("write start value: ")
                c = arr[opPos+1]
                arr[c] = int(val)
                opPos = opPos + 2

            if opInstruct == 4:
                c = arr[opPos+1]
                print(str(arr[c]))
                opPos = opPos + 2

            if opInstruct == 5:
                param1mode = get_digit(opParam, 2)
                param2mode = get_digit(opParam, 3)
                if param1mode == 0:
                    c = arr[opPos + 1]
                    firstparam = arr[c]
                elif param1mode == 1:
                    firstparam = arr[opPos +1]
                if param2mode == 0:
                    c = arr[opPos + 2]
                    secparam = arr[c]
                elif param2mode == 1:
                    secparam = arr[opPos +2]


                if firstparam != 0:
                    opPos = secparam
                else:
                    opPos = opPos + 3

            if opInstruct == 6:
                param1mode = get_digit(opParam, 2)
                param2mode = get_digit(opParam, 3)
                if param1mode == 0:
                    c = arr[opPos + 1]
                    firstparam = arr[c]
                elif param1mode == 1:
                    firstparam = arr[opPos + 1]
                if param2mode == 0:
                    c = arr[opPos +2]
                    secparam = arr[c]
                elif param2mode == 1:
                    secparam = arr[opPos + 2]


                if firstparam == 0:
                    opPos = secparam
                else:
                    opPos = opPos +3

            if opInstruct == 7:

                param1mode = get_digit(opParam, 2)
                param2mode = get_digit(opParam, 3)
                if param1mode == 0:
                    c = arr[opPos +1]
                    firstparam = arr[c]
                elif param1mode == 1:
                    firstparam = arr[opPos + 1]
                if param2mode == 0:
                    c = arr[opPos + 2]
                    secparam = arr[c]
                elif param2mode == 1:
                    secparam = arr[opPos + 2]

                if firstparam < secparam:
                    thirdparam = arr[opPos + 3]
                    arr[thirdparam] = 1
                else:
                    thirdparam = arr[opPos + 3]
                    arr[thirdparam] = 0
                opPos = opPos + 4

            if opInstruct == 8:
                param1mode = get_digit(opParam, 2)
                param2mode = get_digit(opParam, 3)

                if param1mode == 0:
                    c = arr[opPos + 1]
                    firstparam = arr[c]
                elif param1mode == 1:
                    firstparam = arr[opPos +1]
                if param2mode == 0:
                    c = arr[opPos +2]
                    secparam = arr[c]
                elif param2mode == 1:
                    secparam = arr[opPos +2]


                thirdparam = arr[opPos +3]
                if firstparam == secparam:
                    arr[thirdparam] = 1
                else:
                    arr[thirdparam] = 0
                opPos = opPos + 4

            if opInstruct == 99:
                #print(arr[0])
                break

def get_digit(number, n):
    return number // 10**n % 10

if __name__ == '__main__':
    main()