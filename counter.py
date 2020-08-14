file=open('data.txt')
for line in file:
    words=line.split()
    for word in words:
        print(word)
