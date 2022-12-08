def main():
    with open('8th/inputs.txt') as file:
        lines = file.readlines()
        forest = []
        for line in lines:
            forest.append(list(line.strip()))
        visibleCount = 0
        for i in range(0, len(forest)):
            for j in range(0, len(forest[0])):
                visible = False
                # check to the left
                for k in range(0, j):
                    if forest[i][k] >= forest[i][j]:
                        break
                else:
                    visible = True
                # check to the top
                if not visible:
                    for k in range(0, i):
                        if forest[k][j] >= forest[i][j]:
                            break
                    else:
                        visible = True

                    # check to the right
                    if not visible:
                        for k in range(j + 1, len(forest[0])):
                            if forest[i][k] >= forest[i][j]:
                                break
                        else:
                            visible = True

                        # check to the bottom
                        if not visible:
                            for k in range(i + 1, len(forest)):
                                if forest[k][j] >= forest[i][j]:
                                    break
                            else:
                                visible = True
                if visible:
                    visibleCount += 1
        print(visibleCount)


def main2():
    with open('8th/inputs.txt') as file:
        lines = file.readlines()
        forest = []
        for line in lines:
            forest.append(list(line.strip()))
        results = []
        for i in range(0, len(forest)):
            for j in range(0, len(forest[0])):
                ## counting left
                leftCount = 0
                for k in reversed(range(0, j)):
                    leftCount += 1
                    if forest[i][j] <= forest[i][k]:
                        break
                ## counting top
                topCount = 0
                for k in reversed(range(0, i)):
                    topCount += 1
                    if forest[i][j] <= forest[k][j]:
                        break
                ## counting right
                rightCount = 0
                for k in range(j + 1, len(forest[0])):
                    rightCount += 1
                    if forest[i][j] <= forest[i][k]:
                        break
                ## counting bottom
                bottomCount = 0
                for k in range(i + 1, len(forest)):
                    bottomCount += 1
                    if forest[i][j] <= forest[k][j]:
                        break
                results.append(leftCount * topCount * rightCount * bottomCount)
        results.sort(reverse=True)
        print(results[0])


main()
main2()