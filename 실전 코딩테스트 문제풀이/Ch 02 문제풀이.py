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

def BackJoon17269():
    n, m = map(int, input().split())
    name1, name2 = input().split()

    array = []
    data = { 'A' : 3, 'B' : 2, 'C' : 1, 'D' : 2, 'E' : 4, 'F' : 3, 'G' : 1, 'H' : 3, 'I' : 1, 'J' : 1, 'K' : 3, 'L' : 1, 'M' : 3, 'N' : 2, 'O' : 1, 'P' : 2, 'Q' : 2, 'R' : 2, 'S' : 1, 'T' : 2, 'U' : 1, 'V' : 1, 'W' : 1, 'X' : 2, 'Y' : 2, 'Z' : 1 }

    for i in range(max(len(name1), len(name2))):
        if i < len(name1):
            array.append(name1[i])
        if i < len(name2):
            array.append(name2[i])

    result = []
            
    for i in range(len(array)):
        if array[i] in data:
            result.append(data[array[i]])

    result_len = len(result)
    for i in range(1, result_len - 1):
        result2 = []
        for j in range(len(result) - 1):
            result2.append((result[j] + result[j + 1]) % 10)
        result = result2

    if result[0] == 0:
        print("%d%%" % (result[1]))
    else:
        print("%d%d%%" % (result[0], result[1]))

def BackJoon17389():
    n = int(input())
    s = list(input())

    result = 0
    bonus = 0
    for i in range(n):
        if s[i] == 'O':
            result += (i + 1 + bonus)
            bonus += 1
        else:
            bonus = 0
            
    print(result)

if __name__ == "__main__":
    BackJoon17389()