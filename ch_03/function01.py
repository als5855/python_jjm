def fx01():
  pass 

def fx02():
  print("fx02 호출")

fx02()

class A:
  pass



def fx03(a, b, c):
  print(a)
  print(b)
  print(c)

def fx03(a: int, b:A | None=A(), c=None): # b:A객체 | None=A()A생성자 b이거나 None이거나
  print(a)
  print(b)
  print(c)

fx03(10, A()) # 오버로딩이 안된다. 인터프리터여서 그렇다.
fx03(1, "문자열", [])

def fx04(*args): # -- *tuple
  print(args)

fx04(1, 2, 3, 4, 5) # 괄호가 생략된 튜플

def requestGet(
    url:str |None="http://localhost", 
    port:int | None=8080, 
    params:dict| None=dict()): #dict key: value값으로 받아야 하니까.
  print(url)
  print(port)
  print(params)
  return "Response"

responseData = requestGet("https://localhost", None, {"name": "장지민", "age" : 29})
requestGet(url="https://localhost", params={"name": "장지민", "age" : 29})

req = lambda url, port, params: {"usl":url, "port":port, "params":params} #람다는 간단한 수식을 위해 사용한다. 파이썬에서는 타입지정을 못한다.
req = lambda url="http://localhost", port=8080, params={"name": "장지민", "age" : 29}: {"usl":url, "port":port, "params":params} #람다는 간단한 수식을 위해 사용한다. 파이썬에서는 타입지정을 못한다.

print(req("http://localhost", 8080, {"name":"장지민", "age": 31}))

