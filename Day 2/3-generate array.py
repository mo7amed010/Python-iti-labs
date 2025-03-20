start = int(input("Enter the start of the range: "))
length = int(input("Enter the length of the array: "))


# def generate(length,start):
#   if length == 0:
#     return []
#   else:
#     arr = []
#     for i in range(start,start + length):
#       arr.append(i)
#     return arr

def generate(length, start):
  return list(range(start,start+length)) if length > 0 else []

arr = generate(length,start)
print(arr)


