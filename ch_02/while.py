print("\n")
isClose = False

while not isClose:
  print("반복 실행!!")
  flag = input("멈추겠습니까?(Y/N) ") # pass 비워저있다는 의미
  if flag in ['y', 'n']:
    isClose = True