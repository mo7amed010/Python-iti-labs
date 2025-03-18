sentence = "hi this is me and i don't know what should i write"
new = ""
for char in sentence:
  if char != "a" and char != "i" and char != "e" and char != "o" and char != "u":
    new +=  char
print(new)