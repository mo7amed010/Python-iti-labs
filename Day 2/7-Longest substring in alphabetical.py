name = input("Enter any string: ")

def longest(name):
  longest_word = ""
  current_word = name[0] if name else ""

  for i in range(1, len(name)):
    if name[i] >= name[i-1]:
      current_word += name[i]
    else:
      if len(current_word) > len(longest_word):
        longest_word = current_word
      current_word = name[i]

  if len(current_word) > len(longest_word):
    longest_word = current_word

  return longest_word

print(longest(name))
