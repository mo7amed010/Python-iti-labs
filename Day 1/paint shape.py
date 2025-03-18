stars = int(input("Enter the height of the shape : "))
space = " "
s = "*"

for star in range(0,stars):
  print(space* (stars-star+1) + s*(star+1))
