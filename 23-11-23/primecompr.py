def prime(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False

n = int(input())
l = [i for i in range(2, n + 1) if prime(i)]
for i in l:
    print(i, end=' ')
