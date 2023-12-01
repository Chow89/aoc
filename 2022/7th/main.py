def findDir(dir, currentDir):
    for element in currentDir.get('content'):
        if element.get('name') == dir:
            return element
    return None


def dirSize(dir):
    size = 0
    for element in dir.get('content'):
        if element.get('size'):
            size += int(element.get('size'))
        else:
            size += dirSize(element)
    return size


def flatten(dir):
    list = [dir]   # dir.get('content')
    for elem in dir.get('content'):
        if elem.get('size'):    # it is a file
            pass
        else:
            list.extend(flatten(elem))
    return list


def main():
    with open('2022/7th/inputs.txt') as file:
        lines = file.readlines()
        filesystem = {
            'name': '/',
            'content': [],
            'parent': None
        }
        currentDir = filesystem
        for line in lines:
            if line.startswith('$ cd'): # go to dir
                dirName = line.split(' ')[-1].strip()
                if dirName == '..':
                    currentDir = currentDir.get('parent')
                else:
                    dir = findDir(dirName, currentDir)
                    if dir:
                        currentDir = dir
            elif line.startswith('$ ls'): # list content
                pass
            elif line.startswith('dir'):    # directory name
                currentDir.get('content').append({
                    'name': line.split(' ')[-1].strip(),
                    'content': [],
                    'parent': currentDir
                })
            else:   # filename with size
                [size, name] = line.split(' ')
                currentDir.get('content').append({
                    'name': name.strip(),
                    'size': size.strip()
                })

        dirs = flatten(filesystem)
        sum = 0
        for dir in dirs:
            if dirSize(dir) <= 100000:
                sum += dirSize(dir)
        print(sum)
        toBeDeletedSpace = dirSize(filesystem) - 70000000 + 30000000
        tooBigDirs = list(filter(lambda x: dirSize(x) >= toBeDeletedSpace, dirs))
        toBeDeletedDir = sorted(tooBigDirs, key=lambda x: dirSize(x))[0]
        print(dirSize(toBeDeletedDir))


main()
