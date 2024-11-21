# num1 = int(input("숫자1: "))
# num2 = int(input("숫자2: "))

# 10, 20
# 10 20
num1Andnum2Input = input("숫자1, 숫자2: ").replace(",", "").split(" ")
# num1Andnum2 = list(map(int, num1Andnum2Input))
# num1Andnum2 = map(int, num1Andnum2Input)
print(num1Andnum2)
# num1Andnum2 = input("숫자1, 숫자2: ").replace(",", "").split(" ")
# input("숫자1, 숫자2: ") - 이렇게 하면 문자열로 나온 출력이되서 나오기에 숫자로 사용할수 가없다
# int(input("숫자1, 숫자2: ")) - int를 붙이면 숫자 타입으로 만들 수 있지만 두개의 숫자를 받아오는 지문이기에 10, 20 / 10 20 이런식으로 받아오면 사용할 수 없다.
# int(input("숫자1, 숫자2: ").split(","))) - .split을 바로 사용하면 두숫자가 ,를 중심으로 배열로 나눠진다 하지만 ['10', ' 20'] 이렇게 나올 수 있다. 입력 조건을 안지키고 입력했을 때를 생각해야한다. 그래서 replace를 사용해서 ","를 ""으로 변경한다. 그런다음에 .split(" ")을 해서 빈칸을 중심으로 해서 숫자를 나눈다.
# map을 사용해서 int 타입으로 반환을 할 것이다. 
# num1Andnum2 = map(int, input("숫자1, 숫자2: ").replace(",", "").split(" ")m1Andnum2Input) -> map으로 반환을 하면 리스트 형식으로 출려되지 않음으로 list타입을 변환을 시켜준다.
# list(map(int, input("숫자1, 숫자2: ").replace(",", "").split(" ")))

num1, num2 = num1Andnum2
print(num1)
print(num2)

# nums = ['1', '2', '3', '4']
# nums2 = list(map(int, nums))
# print(nums2)

# def parseInt(strNum):
#   return int(strNum)

# nums3 = list(map(parseInt, nums2)) #nums.map(strNum => int(strNum))
# print(nums3)

# nums4 = list(map(lambda strNum: int(strNum), nums))
# print(nums4)
