name = '장지민'

print(name)

# 문자열 사이에 문자역 추가(join)
print(",".join(name))

#문자열 f포맷, 표현식
print(f"{name}입니다.") # 장지민입니다.

#문자열 안에서 찾고자하는 문자여의 위치 반환
print(name.find('민')) # 2
print(name.rfind('장')) # 
print(name.index('민')) # 2
print(name.find('김')) # -1
# print(name.index('김')) # error - 가급적 예외처리를 선택한다.

# 문자열 안에서 찾고자하는 문자역의 개수 반환
print(name.count('지'))

#문자열 길이
print(name.__len__)
print(len(name))

# 문자열 양끝이 공백제거
print(" 이름 ".strip()) # 양쪽 공백 제거
print(" 이름 ".lstrip()) # 왼쪽 공백 제거
print(" 이름 ".rstrip()) # 오른쪽 공백 제거

# 문자열 특정 부분 변경
print("010-1234/5678".replace("-", "").replace("/", ""))

# 토큰으로 문자역 리스트화 하기
print("장지민, 장지은, 장지호".split(",")) #['장지민', ' 장지은', ' 장지호']

address = "부산광역시 동래구 사직동 아파트 2동 207호"
addressList = address.split(" ")
address1 = addressList[0]
address2 = addressList[1] # 
address3 = " ".join(addressList[2:]) # 사지동 아차트 2동 207호

print(f"주소1: {address1}, 주소2: {address2}, 주소3: {address3}") # 띄어쓰기
print(f"주소1: {address1}\n주소2: {address2}\n주소3: {address3}") # 줄바꾸기
print(f"""주소1: {address1}
주소2: {address2}
주소3: {address3}""") # 

# 인덱싱, 슬라이싱
print(address[0]) 
print(address[0:3]) # 0~2까지 출력된다. : 부산광
print(address[:3]) # 0~2까지 출력된다. : 부산광
print(address[4:]) # 4부터 끝까지 출력된다. :시 동래구 사직동  
print(address[-1:]) # 뒤에서 부터 끝까지 출력된다. : 동
print(address[-3:]) # 뒤에서 3번째 부터 끝까지 출력된다. : 사직
print(address[-3:-1]) # 시 동래구
print(address[4:-3]) # 사직 

print(address[:address.find("시") + 1])

print(address[address.find("시") + 2:address.find("사") - 1])
print(address[6:-4])

print("*" * 20)
print("1. 회원가입")
print("2. 로그인")
print("*" * 20)



