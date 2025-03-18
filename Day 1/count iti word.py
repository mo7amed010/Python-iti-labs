sentence = "ititi"
# print(sentence.count("iti"))
index=0
count=0

while index < len(sentence):
    if sentence[index:index+3]=="iti":
        count+=1
        index+=1
    else:
        index+=1

print("nums of iti is  ",count)