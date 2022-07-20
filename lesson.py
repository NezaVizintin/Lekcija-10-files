text1 = open("text1.txt", "r")

contents1 = text1.read()
print(contents1)

text1.close()

print()

#recomended approach - the connection is automatically closed once you go out of the with clause
with open("text2.txt", "r") as text2:
    contents2 = text2.read()
    print(contents2)

print()

#Reading a file line-by-line (using a for loop)
with open("text3.txt", "r") as text3:
    lines = text3.read().splitlines()

    for line in lines:
        print(line)

with open("text4.txt", "w") as text4:
    text4.write("this text was written by the program")

print()

with open("text4.txt", "r") as text4r:
    content4 = text4r.read()
    print(content4)