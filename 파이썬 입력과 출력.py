# Excercise 1. 문자열 출력하기
# 화면에 "Hello World"를 출력하라.
def Excercis_01():
    print("Hello World")

# Excercise 2. 문자열 출력하기
# 화면에 "Mary's cosmetics"를 출력하라.(중간에 '가 있음에 주의)

def Excercis_02():
    print("Mary\'s cosmetics")

# Excercise 3. 포맷 연산자
# print 함수를 사용하여 3.141592의 값을 출력하라. 단, 출력된 값이 소수점 아래로 두 자리 숫자 까지만 표시되도록 하라.
# 실행 예: 3.14

def Excercis_03():
    digit = 3.141592
    print("%.2f" % digit)

# Excercise 4. 사용자 입력
# 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값을 출력하는 프로그램을 작성하라.
# 실행 예: first: 3 second: 4 합: 7

def Excercis_04():
    first = int(input("first: "))
    second = int(input("second: "))
    result = first + second
    print("합: %d" % result)

# Excercise 5. 사용자 입력(반복문을 배우는 이유)
# 사용자로부터 출력하고자 하는 문자열과 반복 횟수를 4로 입력받았다고 가정하기, 문자열을 반복 횟수(4번)만큼 출력하는 프로그램을 작성하라.
# 실행 예: 문자열: hello 반복횟수: 4 "hellohellohellohello"

def Excercis_05():
    str = input("문자열: ")
    forNumber = int(input("반복횟수: "))
    
    for i in range(forNumber):
        print(str, end='')

# Exercise 6. 형 변환
# 문자열 '720'를 정수형으로 변환하라. 정수 100을 문자열 '100'으로 변환하라.
def Excercis_06():
    string = "720"
    number = 100
    print(int(string), type(string), type(int(string)))
    print(str(number), type(number), type(str(number)))

# Exercise 7. 사칙 연산
# 사용자로부터 두 개의 숫자를 입력 받은 후 두 숫자의 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/) 결괏값을 출력하라.
def Excercis_07():
    num1 = int(input("number1: "))
    num2 = int(input("number2: "))
    print("add: %d" % (num1 + num2))
    print("min: %d" % (num1 - num2))
    print("mul: %d" % (num1 * num2))
    print("div: %d" % (num1 / num2))

# Exercise 8. 거듭제곱
# 사용자로부터 밑과 지수를 입력 받은 후 거듭제곱 값을 출력하라.
# 실행 예: 밑: 3 지수: 2 3^2 = 9
def Excercis_08():
    baseNumber = int(input("밑: "))
    exponentNumber = int(input("지수: "))
    result = baseNumber ** exponentNumber
    print("%d^%d = %d" % (baseNumber, exponentNumber, result))

# Exercise 9. 입력과 출력
# 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값, 곱한 값, 나눈 값, 나눈 몫, 나머지 값을 각각 출력하는 프로그램을 작성하세요.
# Example
# INPUT: 4 and 4
# OUTPUT:
# 8
# 16
# 1.0
# 1
# 0
def Excercis_09():
    num1 = int(input("number1: "))
    num2 = int(input("number2: "))
    
    print("add: %d" % (num1 + num2))
    print("min: %d" % (num1 * num2))
    print("mul: %d" % (num1 / num2))
    print("div: %.1f" % (num1 // num2))
    print("remain: %d" % (num1 % num2))

# Exercise 10. 입력과 출력
# 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값, 곱한 값, 나눈 값, 나눈 몫, 나머지 값을 각각 다음과 같이 출력하는 프로그램을 작성하세요.
# Example
# INPUT: 4 and 4
# OUTPUT:
# 4 + 4 = 8
# 4 * 4 = 16
# 4 / 4 = 1
# 4 // 4 = 1
# 4 % 4 = 0
def Excercis_10():
    num1 = int(input("number1: "))
    num2 = int(input("number2: "))
    
    print("{0} + {1} = {2}".format(num1, num2, num1 + num2))
    print("{0} * {1} = {2}".format(num1, num2, num1 * num2))
    print("{0} / {1} = {2:.0f}".format(num1, num2, num1 / num2))
    print("{0} // {1} = {2}".format(num1, num2, num1 // num2))
    print("{0} % {1} = {2}".format(num1, num2, num1 % num2))

# Exercise 11. 입력과 출력
# 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 나눈 값을 다음 조건에 맞추어 출력하는 프로그램을 작성하세요.
# format() 함수를 사용해서 출력하세요
# 단, 나눈 값은 소숫점 첫번째 자리까지만 출력하세요.
# Example
# INPUT: 5 and 4
# OUTPUT:
# 5 / 4 = 1.2
def Excercis_11():
    num1 = int(input("number1: "))
    num2 = int(input("number2: "))
    print("{0} / {1} = {2:0.1f}".format(num1, num2, num1 / num2))

if __name__ == '__main__':
    Excercis_11()