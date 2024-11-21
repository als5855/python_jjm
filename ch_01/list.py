# 선언 및 초기화 방법
list1 = [1, 3, 5, 4]
# list2 = list()

print(list1[0])
print(list1[0:2])

print(list1.index(3))


list2 = list1[:] # 슬라이싱 하면 새로운 배열에 담는 것이다. (깊은 복사)
list2.sort()
list2.reverse()
print("========")
print(list2.pop(2))
print(list2)
# print(list2.remove(4)) #리턴은 반환이 없어서 안된다.
list2.remove(4)

print(list2)
print(list1)

list1.insert(1, 10) #1번 위치에 10이 들어간다.
print(list1)

list3 = list1.copy()
print(list3)
list1.extend(list3)
print(list1)

print(list3 + [1, 2, 3, 4]) # list3에 직접적인 영향을 주진 않는다
print(list3 * 3) # list3에 직접적인 영향을 주진 않는다

list4 = [1, "장지민", [10, 20], 3.14, [30, 40]]
print(list4)


print(list4[2::2])


list5 = list4[2:]
list5.remove(3.14)
print(list5)

print(list5[2:])

