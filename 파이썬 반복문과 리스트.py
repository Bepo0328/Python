# Exercise 31. 반복문
# 1 ~ 10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하세요.
def Excercis_31():
    result = 0
    for i in range(10):
        result += (i + 1)

    print(result)

# Exercise 32. 반복문
# 사용자로부터 2 ~ 9 사이의 숫자를 입력 받은 후, 해당 숫자에 대한 구구단을 출력하세요.
def Excercis_32():
    inputNumber = int(input("숫자를 입력해주세요: "))
    for i in range(9):
        print("{0} x {1} = {2}".format(inputNumber, (i + 1), inputNumber * (i + 1)))

# Exercise 33. 반복문과 문자열 다루기 (split)
# 사용자로부터 , 로 구분된 여러 이름을 입력받아서, 한 줄에 하나씩 이름을 출력하세요
# 사용자 입력: Dave,David,Andy,Arthor
# 출력 예:
# Dave
# David
# Andy
# Arthor
def Excercis_33():
    strings = input("입력해주세요: ")
    for string in strings.split(","):
        print (string)

# Exercise 34. 반복문과 문자열 다루기 (split)
# 사용자로부터 [이름1],[이름2],[이름3] 과 같은 형식으로 데이터를 입력받아서, 한 줄에 하나씩 이름을 출력하세요
# 사용자 입력: [Dave],[David],[Andy],[Arthor]
# 출력 예:
# Dave
# David
# Andy
# Arthor
def Excercis_34():
    strings = input("입력해주세요: ")
    for string in strings.split(","):
        print (string.strip("[]"))

# Exercise 35. 반복문과 조건문
# 1부터 30까지의 숫자 중 3의 배수만 출력하세요.
def Excercis_35():
    for i in range(1, 30):
        if (i % 3 == 0):
            print(i)

# Exercise 36. 반복문 (while)
# 1부터 100까지 숫자를 모두 더한 값을 출력하세요.
# 단 while 구문을 사용해서 작성하세요.
def Excercis_36():
    result, num = 0, 1
    while num <= 100:
        result += num
        num += 1

    print(result)

# Exercise 37. 반복문 (while)
# 사용자로부터 4자리의 숫자로 구성된 데이터를 입력받아서
# 비밀번호와 같으면 '비밀번호가 맞습니다.'를 출력하고 종료하세요.
# 비밀번호와 다르면 '비밀번호가 틀렸습니다.'를 출력하고 다시 사용자로부터 데이터를 입력받으세요.
# 비밀번호는 4312 입니다.
def Excercis_37():
    inpuNum = 0
    while inpuNum != 4321:
        inpuNum = int(input("숫자를 입력해주세요: "))
        if inpuNum == 4321:
            print("비밀번호가 맞습니다.")
            break
        else:
            print("비밀번호가 다릅니다.")

# Exercise 38. 데이터 구조와 반복문 (리스트)
# 다음 리스트 변수에서 음수 데이터를 삭제하고, 양수만 가진 리스트 변수로 만들고, 해당 변수를 출력하세요.
# num_list = [0, -11, 31, 22, -11, 33, -44, -55]
def Excercis_38():
    num_list = [0, -11, 31, 22, -11, 33, -44, -55]
    num_list2 = list()

    for num in num_list:
        if num >= 0:
            num_list2.append(num)

    print(num_list2)

# Exercise 39. 데이터 구조와 반복문 (리스트)
# 다음 리스트에 있는 데이터의 길이를 한 라인에 하나씩 출력하세요.
# list_data = ["fun-coding", "Dave", "Linux", "Python", "javascript", "front-end", "back-end", "dataengineering"]
# 출력 예:
# "fun-coding"'s length is 10
# "Dave"'s length is 4
# "Linux"'s length is 5
# "Python"'s length is 6
# "javascript"'s length is 10
# "front-end"'s length is 9
# "back-end"'s length is 8
# "dataengineering"'s length is 15
def Excercis_39():
    list_data = ["fun-coding", "Dave", "Linux", "Python", "javascript", "front-end", "back-end", "dataengineering"]
    for string in list_data:
        print("\"{0}\"\'s length is {1}".format(string, len(string)))

# Exercise 40. 데이터 구조와 반복문 (리스트)
# 다음 리스트에 있는 숫자를 역 방향으로 출력하세요.
# 단, 리스트에 있는 숫자들은 한 라인에 하나씩 출력하세요.
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
def Excercis_40():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data.reverse()
    for num in data:
        print(num)

# Exercise 41. 데이터 구조 (리스트), 반복문, 문자열 다루기
# 다음과 같이 파일 이름(확장자 포함) 저장하고 있는 리스트가 있을 때 확장자를 제거하고 파일 이름만 출력하세요.
# filelist = ['exercise01.docx', 'exercise02.docx', 'exercise03.docx', 'exercise04.docx', 'exercise05.docx']
def Excercis_41():
    filelist = ['exercise01.docx', 'exercise02.docx', 'exercise03.docx', 'exercise04.docx', 'exercise05.docx']
    for file in filelist:
        print(file.split(".")[0])

# Exercise 42. 데이터 구조 (리스트), 반복문, 조건문, 문자열 다루기
# 파일 이름이 다음과 같은 리스트에 저장되어 있을 때 확장자가 .txt 인 파일에 대한 리스트를 출력하라
# filelist = ['exercise01.docx', 'exercise02.csv', 'exercise03.txt', 'exercise04.hwp']
def Excercis_42():
    filelist = ['exercise01.docx', 'exercise02.csv', 'exercise03.txt', 'exercise04.hwp']
    for file in filelist:
        if file.split(".")[1] == "txt":
            print(file)

# Exercise 43. 문자열 다루기와 조건문
# prices 변수에 입력된 값을 원 화로 바꿔서 계산하세요.
# prices = '100 달러'
# 환율은 다음과 같음
# 통화단위	원화 환율
# 달러	1112
# 출력:
# 111200 원
def Excercis_43():
    prices = '100 달러'
    print("{0} 원".format(int(prices.split()[0]) * 1112))

# Exercise 44. 문자열 다루기와 조건문
# 사용자로부터 달러 또는 위안 금액을 입력받은 후 이를 원으로 바꿔서 계산하세요.
# 사용자는 100 달러, 100 위안 과 같이 금액과 통화명 사이에 공백을 넣어 입력하기로 합니다.
# 각 통화별 환율은 다음과 같습니다.
# 통화단위	원화 환율
# 달러	1112
# 위안	171
# 출력:
# 111200 원
def Excercis_44():
    prices  = input("금액을 입력해주세요: ")
    price = prices.split()
    if price[1] == "달러":
        print("{0} 원".format(int(price[0]) * 1112))
    elif price[1] == "위안":
        print("{0} 원".format(int(price[0]) * 171))
    else:
        print(price)


# Exercise 45. 문자열 다루기, 조건문, 데이터 구조 (dictionary)
# 다음 통화별 환율을 통화단위와 원화 환율을 가진 딕셔너리로 만들고 사용자로부터 달러, 엔, 또는 위안 금액을 입력받은 후 이를 원으로 바꿔서 계산하세요.
# 사용자는 100 달러, 100 위안 과 같이 금액과 통화명 사이에 공백을 넣어 입력하기로 합니다.
# 통화단위	원화 환율
# 달러	1112
# 위안	171
# 엔	1010
def Excercis_45():
    exchange  = {"달러" : 1112, "위안" : 171, "엔" : 1010 }

    prices  = input("금액을 입력해주세요: ")
    price = prices.split()

    if price[1] == "달러" or price[1] == "위안" or price[1] == "엔":
        print("{0} 원".format(int(price[0]) * exchange[price[1]]))

# Exercise 46. 이중 반복문
# 구구단을 2단부터 9단까지 다음과 같이 출력하세요
# 출력 예
# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# 2 X 4 = 8
# 2 X 5 = 10
# 2 X 6 = 12
# 2 X 7 = 14
# 2 X 8 = 16
# 2 X 9 = 18
# 3 X 1 = 3
# 3 X 2 = 6
# .
# .
# .
# 9 X 7 = 63
# 9 X 8 = 72
# 9 X 9 = 81
def Excercis_46():
    for i in range(2, 10):
        for j in range(1, 10):
            print("{0} x {1} = {2}".format(i, j, i * j))
        print()

# Exercise 47. 이중 반복문과 조건문
# 구구단을 2단부터 9단까지 출력하되, 계산 값이 짝수인 경우에만 출력하세요
# 예: 3 X 3 = 9 에서 9는 홀수이므로 출력하지 않는다.
# 예: 2 X 4 = 8 에서 8은 짝수이므로 출력한다.
# 최종 출력 예
# 2 X 2 = 4
# 2 X 3 = 6
# 2 X 4 = 8
# 2 X 5 = 10
# 2 X 6 = 12
# 2 X 7 = 14
# 2 X 8 = 16
# 2 X 9 = 18
# 3 X 2 = 6
# 3 X 4 = 12
# 3 X 6 = 18
# 3 X 8 = 24
# 4 X 2 = 8
# 4 X 3 = 12
# 4 X 4 = 16
# 4 X 5 = 20
# 4 X 6 = 24
# 4 X 7 = 28
# 4 X 8 = 32
# 4 X 9 = 36
# 5 X 2 = 10
# 5 X 4 = 20
# 5 X 6 = 30
# 5 X 8 = 40
# 6 X 2 = 12
# 6 X 3 = 18
# 6 X 4 = 24
# 6 X 5 = 30
# 6 X 6 = 36
# 6 X 7 = 42
# 6 X 8 = 48
# 6 X 9 = 54
# 7 X 2 = 14
# 7 X 4 = 28
# 7 X 6 = 42
# 7 X 8 = 56
# 8 X 2 = 16
# 8 X 3 = 24
# 8 X 4 = 32
# 8 X 5 = 40
# 8 X 6 = 48
# 8 X 7 = 56
# 8 X 8 = 64
# 8 X 9 = 72
# 9 X 2 = 18
# 9 X 4 = 36
# 9 X 6 = 54
# 9 X 8 = 72
def Excercis_47():
    for i in range(2, 10):
        for j in range(1, 10):
            if (i * j) % 2 == 0:
                print("{0} x {1} = {2}".format(i, j, i * j))
        print()

# Exercise 48. 이중 반복문과 데이터 구조 (리스트)
# 아파트 동호수를 다음과 같은 두 리스트 변수를 활용해서 출력하세요.
# 단, 각 동과 동 사이에는 구분이 되도록 한 라인씩 띄워서 출력하세요
# dongs = ["6209동", "6208동", "6207동"]
# hos = ["101호", "102호", "103호", "104호"]
# 출력 예:
# 6209동 101호
# 6209동 102호
# 6209동 103호
# 6209동 104호
# 6208동 101호
# 6208동 102호
# 6208동 103호
# 6208동 104호
# 6207동 101호
# 6207동 102호
# 6207동 103호
# 6207동 104호
def Excercis_48():
    dongs = ["6209동", "6208동", "6207동"]
    hos = ["101호", "102호", "103호", "104호"]
    for dong in dongs:
        for ho in hos:
            print("{0} {1}".format(dong, ho))

if __name__ == '__main__':
    Excercis_48()