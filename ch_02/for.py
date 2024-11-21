nums = [10, 20, 30, 40]

for num in nums:
  print(num)

nums = range(10)
print(list(nums)) 

for i in range(10):
  print(i)

nums = range(10, 20, 2) # step은 건너띄기 range(start, stop, step)
print(list(nums))


for i in range(10):
  for j in range(5):
    print(f'i: {i}, j: {j}')



for i in range(5):
  print((i+1) * "*")

print("=" * 10)

for i in range(5):
  # print((i+1) * "*", end="\t\t\t")
  # print("*" * (5-1))
  print(f'{"*" * (i+1)}\t\t\t{(5-i) * "*" }')

for i in range(5):
  print((5-i) * "*" )

print("=" * 10)


for i in range(5):
  print((i+1) * "*", (5-i) * " ", (5-i) * "*")
for i in range(5):
  print((i+1) * "*", 0 * " ", (5-i) * "*")





