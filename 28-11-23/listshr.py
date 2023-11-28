if __name__ == '__main__':
    N = int(input())
    l = []

    for i in range(N):
        op = input().split()

        if op[0] == 'insert':
            i = int(op[1])
            x = int(op[2])
            l.insert(i, x)
        elif op[0] == 'print':
            print(l)
        elif op[0] == 'remove':
            x = int(op[1])
            l.remove(x)
        elif op[0] == 'append':
            x = int(op[1])
            l.append(x)
        elif op[0] == 'sort':
            l.sort()
        elif op[0] == 'pop':
            l.pop()
        elif op[0] == 'reverse':
            l.reverse()
