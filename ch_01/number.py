num1 = 10
num2 = 20
num3 = num1 + num2
num4 = num1 / 3 # 그냥 나누기 소수점까지 나온다
num5 = num1 // 3 # 몫을 구하는 방법
num6 = num1 ** 2 # 제곱(자바에서는 지원하지 않는데 파이썬은 가능하다.)

# Literal: 변하지 않는 고정값

print(num1 == 10) #Literal 주소가 같다는 의미

print(id(11))
print(id(num1))
print(num4)
print(num5)
print(num6)

# ctrl + f5 = 디버거로 실행

# print(num1++) - 증감 연산자 지원하지 않는다. 하려면 num += 1을 사용한다.