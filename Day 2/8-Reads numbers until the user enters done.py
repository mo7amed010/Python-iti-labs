flag = True
sum = 0
count = 0

while flag:
  try:
    num = input("Enate a number: ")
    if num == "done":
      flag = False
    else:
      num = int(num)
      sum += num
      count += 1
    
  except:
    print("Invalid numbmer ):")

print("Sum:", sum)
print("count:", count)
print("Average:", sum/count)
