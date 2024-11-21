# 변수, 메서드

class User:
  username="aaaa"
  password="1234"
  name="장지민"
  email="wlals@naver.com"

  def getUserInfo(self, address): #self는 자바에서는 this이다. 
    return f'''
username: {self.username}
password: {self.password}
name: {self.name}
email: {self.email}
address: {address}
'''
user1 = User()
print(user1.getUserInfo("부산")) # 무조거 self가 매개변수 첫번째로 들어가도록 설계???

'''
클래스*(틀) = 참조자료형 = 객체
int, double = 일반자료형

'''