def BackJoon15969():
    n = int(input())
    array = list(map(int, input().split()))

    result = max(array) - min(array)
    print(result)

def BackJoon10539():
    n, b = int(input()), list(map(int, input().split()))
    a = [0] * n
    a[0] = b[0]
    for i in range(1, n):
        a[i] = b[i] * (i + 1) - sum(a[:i])
    
    for i in a:
        print(i, end=' ')

if __name__ == "__main__":
    BackJoon10539()