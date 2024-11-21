# Map 자료형
# key, vlaue
# key 중복X, 순서X

dict1 = dict()
dict1 = {
  "name": "장지민",
  "age": 29,
  "height": 160
}

print(dict1)

list1 = ['a', 'b', 'c'] # key는 인덱스
tuple1 = 'a', 'b', 'c' # key는 인덱스
dict1 = {'10':'a', '20':'b', '30':'c'} # key:value

print(list1[0])
print(tuple1[0])
print(dict1['10'])

dict1['40'] = 'd' # 추가 방법
print(dict1)
dict1.update({'40':'e', '50': 'f'})
print(dict1)

# value 조회
print(dict1.get('20'))
print(dict1['20'])

# 쌍 삭제
print(dict1.pop('30')) # 30을 추출 한다.
print(dict1) # 30이 사라진다.

print(dict1.items()) # 리스트안에 튜플 단위로 출력된다. items로 엔트리를 추출한다.

for item in dict1.items():
  print(item[0]) # key값 뽑는 방법
  # print(item[1]) # value값 뽑는 방법

for key in dict1.keys():
  print(key)

for value in dict1.values():
  print(value)

keys1 = dict1.keys() #  내장함수 사용 불가능
# print(keys1.) 내장함수 쓸 수 있는게 없다

keys1 = list(dict1.keys()) # 형변환 내장함수 사용 가능
print(keys1) 


