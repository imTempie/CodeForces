number = int(input())
for i in range(0, number):
    word = str(input())
    chars = len(word)
    if chars > 10:
        print(str(word[0]) + str(chars-2) + str(word[chars-1]))
    else:
        print(word)
