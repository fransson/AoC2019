def main():
    with open('input.txt') as f:
        a = f.readline().split(",")
        arr = [int(e) for e in a]
        #arr = [1101, 100, -1, 4, 0]
        counter = 0
        multiplier = 4
        opPos = 0
        while True:
            #opPos = counter * multiplier
            opParam = arr[opPos] #1002
            opInstruct = abs(opParam) % 100

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
                multiplier = 4
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
                multiplier = 4
                opPos = opPos + 4


            if opInstruct == 3:
                val = 1
                arr[opPos+1] = val
                multiplier = 2
                opPos = opPos + 2


            if opInstruct == 4:
                print(str(arr[opPos+1]))
                multiplier = 2
                opPos = opPos + 2
                
            if opInstruct == 99:
                break
            counter = counter + 1

def get_digit(number, n):
    return number // 10**n % 10

if __name__ == '__main__':
    main()