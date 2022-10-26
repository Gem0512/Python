text = ""
while True:
    try:
        str = input()
        text += str + " "
    except EOFError:
        break
print(text)
