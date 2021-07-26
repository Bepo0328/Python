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

if __name__ == '__main__':
    Excercis_40()