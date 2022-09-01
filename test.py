zahlen = input()
_return = ""
for i in range(0, len(zahlen), 1):
    if i == 0:
        if zahlen[i] == "-":
            print(zahlen[0])
        else:
            print(f"Error! Please write your prefix from '{zahlen[0]}' to '-'")
    else:
        _return = _return + str(zahlen[i])
print(_return)