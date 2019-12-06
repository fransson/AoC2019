def main():
    dict = {}
    orbits = 0
    with open('input.txt') as f:
        lines = f.read().splitlines()

    #lines = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']
        for line in lines:

            obj1 = line.split(")")[0]
            obj2 = line.split(")")[1]
            if obj1 not in dict.keys():
                dict[obj1] = [(obj2)]
            else:
                dict[obj1].append((obj2))

        for key, value in dict.items():
            count = len(value)
            for x in value:
                count = count + int(checkChildren(dict, x))
            orbits = orbits + count
        print(orbits)



def checkChildren(dict, child):
    counter = 0
    if child in dict.keys():
        counter = counter + len(dict[child])
        for x in dict[child]:
            counter = counter + checkChildren(dict, x)
    else:
        return int(counter)
    return int(counter)


def main2():
    dict = {}
    orbits = 0
    with open('input.txt') as f:
        lines = f.read().splitlines()

    #lines = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']
        for line in lines:

            obj1 = line.split(")")[0]
            obj2 = line.split(")")[1]
            if obj1 not in dict.keys():
                dict[obj1] = [(obj2)]
            else:
                dict[obj1].append((obj2))

        # YOU START ORBIT : 9Z5
        # SAN START ORBIT : DD2
        allorbitsforYOU = {}
        allorbitsforSAN = {}
        allorbitsforYOU = findallparent(dict, "9Z5")
        allorbitsforSAN = findallparent(dict, "DD2")
        commonNodeYOUSTEPS = []
        commonNodeSANSTEPS = []


        for i, y in enumerate(allorbitsforYOU):
            if y in allorbitsforSAN:
                commonNodeYOUSTEPS.append((y, i +1))

        for i, y in enumerate(allorbitsforSAN):
            if y in allorbitsforYOU:
                commonNodeSANSTEPS.append((y, i +1))

        hej = []
        for y, a in enumerate(commonNodeYOUSTEPS):
            for o, b in enumerate(commonNodeSANSTEPS):
                if a[0] == b[0]:
                    hej.append(a[1] + b[1])

        print(min(hej))


def findallparent(dict, start):
    parent = []
    for key, value in dict.items():
        if start in value:
            parent.append(key)
            parent.extend(findallparent(dict, key))
    return parent





if __name__ == '__main__':
    #main()
    main2()