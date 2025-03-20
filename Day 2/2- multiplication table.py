num = int(input("Enter a number: "))

if num == 0:
  print("[zero]")
else:
  final = []
  for i in range(1,num+1):
    arr = []
    for j in range(1,i+1):
      arr.append(i*j)
    final.append(arr)
print(final)