def main1():
    with open('input.txt') as f:
        list = f.read().splitlines()
        wire1 = list[0].split(",")
        wire2 = list[1].split(",")

        wire1visited = []
        wire2visited = []

        wire1X = 40000
        wire1Y = 40000
        wire2X = 40000
        wire2Y = 40000

        for x,y in enumerate(wire1):
            direction = y[:1]
            len = int(y[1:])
            if direction == "R":
                for i in range(len):
                    wire1X = wire1X +1
                    wire1visited.append((wire1X, wire1Y))
            elif direction == "L":
                for i in range(len):
                    wire1X = wire1X - 1
                    wire1visited.append((wire1X, wire1Y))

            elif direction == "U":
                for i in range(len):
                    wire1Y = wire1Y + 1
                    wire1visited.append((wire1X, wire1Y))

            elif direction == "D":
                for i in range(len):
                    wire1Y = wire1Y - 1
                    wire1visited.append((wire1X, wire1Y))

        for x, y in enumerate(wire2):
            direction = y[:1]
            len = int(y[1:])
            if direction == "R":
                for i in range(len):
                    wire2X = wire2X + 1
                    wire2visited.append((wire2X, wire2Y))
            elif direction == "L":
                for i in range(len):
                    wire2X = wire2X - 1
                    wire2visited.append((wire2X, wire2Y))

            elif direction == "U":
                for i in range(len):
                    wire2Y = wire2Y + 1
                    wire2visited.append((wire2X, wire2Y))

            elif direction == "D":
                for i in range(len):
                    wire2Y = wire2Y - 1
                    wire2visited.append((wire2X, wire2Y))

        intersections = set(wire1visited).intersection(wire2visited)

        # for x in wire1visited:
        #    for y in wire2visited:
        #        if x == y:
        #           intersections.append((x, y))

        manhattandist = []

        for x in intersections:
            manhattandist.append((abs(x[0] - 40000) + abs(x[1] - 40000)))

        print(min(manhattandist))

def main2():
    with open('input.txt') as f:
        list = f.read().splitlines()
        wire1 = list[0].split(",")
        wire2 = list[1].split(",")

        wire1visited = []
        wire2visited = []

        s1a = 0
        s1b = 0
        s1c = 0
        s1d = 0
        s2a = 0
        s2b = 0
        s2c = 0
        s2d = 0

        allsteps = []
        steps = 0
        steps2 = 0

        wire1X = 40000
        wire1Y = 40000
        wire2X = 40000
        wire2Y = 40000

        for x,y in enumerate(wire1):
            direction = y[:1]
            len = int(y[1:])
            if direction == "R":
                for i in range(len):
                    wire1X = wire1X +1
                    wire1visited.append((wire1X, wire1Y))
                    steps2 = steps2 +1
                    if wire1X == 40768 and wire1Y == 39601:
                        s1a = steps2
                    if wire1X == 40768 and wire1Y == 40000:
                        s1b = steps2
                    if wire1X == 41126 and wire1Y == 39601:
                        s1c = steps2
                    if wire1X == 40994 and wire1Y == 40166:
                        s1d = steps2
            elif direction == "L":
                for i in range(len):
                    wire1X = wire1X - 1
                    wire1visited.append((wire1X, wire1Y))
                    steps2 = steps2 + 1
                    if wire1X == 40768 and wire1Y == 39601:
                        s1a = steps2
                    if wire1X == 40768 and wire1Y == 40000:
                        s1b = steps2
                    if wire1X == 41126 and wire1Y == 39601:
                        s1c = steps2
                    if wire1X == 40994 and wire1Y == 40166:
                        s1d = steps2
            elif direction == "U":
                for i in range(len):
                    wire1Y = wire1Y + 1
                    wire1visited.append((wire1X, wire1Y))
                    steps2 = steps2 + 1
                    if wire1X == 40768 and wire1Y == 39601:
                        s1a = steps2
                    if wire1X == 40768 and wire1Y == 40000:
                        s1b = steps2
                    if wire1X == 41126 and wire1Y == 39601:
                        s1c = steps2
                    if wire1X == 40994 and wire1Y == 40166:
                        s1d = steps2

            elif direction == "D":
                for i in range(len):
                    wire1Y = wire1Y - 1
                    wire1visited.append((wire1X, wire1Y))
                    steps2 = steps2 + 1
                    if wire1X == 40768 and wire1Y == 39601:
                        s1a = steps2
                    if wire1X == 40768 and wire1Y == 40000:
                        s1b = steps2
                    if wire1X == 41126 and wire1Y == 39601:
                        s1c = steps2
                    if wire1X == 40994 and wire1Y == 40166:
                        s1d = steps2


        for x, y in enumerate(wire2):
            direction = y[:1]
            len = int(y[1:])
            if direction == "R":
                for i in range(len):
                    wire2X = wire2X + 1
                    wire2visited.append((wire2X, wire2Y))
                    steps = steps + 1
                    if wire2X == 40768 and wire2Y == 39601:
                        s2a = steps
                    if wire2X == 40768 and wire2Y == 40000:
                        s2b = steps
                    if wire2X == 41126 and wire2Y == 39601:
                        s2c = steps
                    if wire2X == 40994 and wire2Y == 40166:
                        s2d = steps
            elif direction == "L":
                for i in range(len):
                    wire2X = wire2X - 1
                    wire2visited.append((wire2X, wire2Y))
                    steps = steps +1
                    if wire2X == 40768 and wire2Y == 39601:
                        s2a = steps
                    if wire2X == 40768 and wire2Y == 40000:
                        s2b = steps
                    if wire2X == 41126 and wire2Y == 39601:
                        s2c = steps
                    if wire2X == 40994 and wire2Y == 40166:
                        s2d = steps
            elif direction == "U":
                for i in range(len):
                    wire2Y = wire2Y + 1
                    wire2visited.append((wire2X, wire2Y))
                    steps = steps + 1
                    if wire2X == 40768 and wire2Y == 39601:
                        s2a = steps
                    if wire2X == 40768 and wire2Y == 40000:
                        s2b = steps
                    if wire2X == 41126 and wire2Y == 39601:
                        s2c = steps
                    if wire2X == 40994 and wire2Y == 40166:
                        s2d = steps

            elif direction == "D":
                for i in range(len):
                    wire2Y = wire2Y - 1
                    wire2visited.append((wire2X, wire2Y))
                    steps = steps + 1
                    if wire2X == 40768 and wire2Y == 39601:
                        s2a = steps
                    if wire2X == 40768 and wire2Y == 40000:
                        s2b = steps
                    if wire2X == 41126 and wire2Y == 39601:
                        s2c = steps
                    if wire2X == 40994 and wire2Y == 40166:
                        s2d = steps


        allsteps = [s1a + s2a, s1b + s2b, s1c + s2c, s1d + s2d]
        print(min(allsteps))


        #intersections = set(wire1visited).intersection(wire2visited)

        #print(intersections)




if __name__ == '__main__':
    #main1()
    main2()