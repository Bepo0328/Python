# Exercise 49. 데이터 구조 (튜플)
# a, b, c, d, e를 저장하는 튜플을 만들고 첫 번째 튜플값과 마지막 번째 튜플값을 출력하세요.
def Excercis_49():
    tupleData = ("a", "b", "c", "d", "e")
    print(tupleData[0], tupleData[4])

# Exercise 50. 데이터 구조 (튜플)
# 다음 코드를 작성해서 실행해보고 에러가 나는 이유를 설명하세요.

# 실행코드
# tupledata = ('dave', 'fun-coding', 'endless')
# tupledata[0] = 'david'
# 에러

# TypeError                                 Traceback (most recent call last)
# <ipython-input-2-db4a259aad24> in <module>()
#       1 tupledata = ('dave', 'fun-coding', 'endless')
# ----> 2 tupledata[0] = 'david'

# TypeError: 'tuple' object does not support item assignment
def Excercis_50():
    tupledata = ('dave', 'fun-coding', 'endless')
    tupledata[0] = 'david'
    # 튜플은 값을 변경할수 없음.

# Exercise 51. 데이터 구조 (튜플)
# 다음 코드를 읽고, 최종적으로 var1과 var2의 값이 어떤 값이될지 확인해보고, 왜 이렇게 동작하는지 튜플을 기반으로 설명하세요.
# 실행코드
# var1, var2 = 1, 2
# var1, var2 = var2, var1
def Excercis_51():

    print()

# Exercise 52. 데이터 구조 (튜플)
# 다음 코드에서 두번째 데이터부터 마지막 데이터를 다음과 같이 출력하세요
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')
# 출력:
# ('fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')
def Excercis_52():
    print()

if __name__ == '__main__':
    Excercis_50()