sentence = "hi this is me and i don't know what should i write"
count = 0
for char in sentence:
  if char == "a" or char == "i" or char == "e" or char == "o" or char == "u":
    count += 1
print(count)