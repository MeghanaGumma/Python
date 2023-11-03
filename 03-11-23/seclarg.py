if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s=set(arr)
    arr=list(s)
    arr.sort()
    print(arr[-2])
