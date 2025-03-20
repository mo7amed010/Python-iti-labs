numbers = []

while len(numbers) < 5:
  num = input("Enter a number: ")
  try:
    num = int(num)
    numbers.append(num)
  except:
    print("Invalid num")

# numbers.sort()
# print("sorting:",numbers)
# numbers.reverse()
# print("sorting reverse:",numbers)

# sort manually
def swap(x,y):
  return y,x


def sortingASC(arr):
  n = len(arr)
  for i in range(n):
    for num in range(n-1):
      if arr[num] > arr[num+1]:
        arr[num] , arr[num+1] = swap(arr[num] , arr[num+1])
  return arr

def sortingDesc(arr):
  n = len(arr)
  for i in range(n):
    for num in range(n-1):
      if arr[num] < arr[num+1]:
        arr[num] , arr[num+1] = swap(arr[num] , arr[num+1])
  return arr


print(sortingASC(numbers))
print(sortingDesc(numbers))


