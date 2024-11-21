print()
# 튜플은 값이 추가가 안된다는 특징이 있다.
# 리스트랑 동일한 구조(값의 추가, 수정, 삭제 불가능)
tuple1 = ()
tuple1 = tuple()

tuple1 = (1, 2, 3)
print(tuple1[1:]) # 인덱스와 슬라이스 가능

tuple1 = tuple1 * 3 # 추가가 아닌 새로운 튜플을 만든거다 
print(tuple1)

# tuple1.append(10) 
# print(tuple1) # 에러 발생

tuple2 = (10,)# 튜플은 하를 기입해도 쉼표를 사용한다.
tuple3 = 1, 2, 3 # 괄호를 생략한다.

# void add() {
  
# }

# function add() {

# }

def add(n1, n2, n3): # def 정의한다. ":"으로 하위를 정의한다.
  return n1 + n2, n2 + n3, n1 + n3

print(add(10, 20, 30))