_command = "-"
_return = ""

if _command.split(' ')[0] == _command.split(' ')[0]:
    for i in range(0, len(_command), 1):
        if i == 0:
            if _command[0] == "-":
                print(True)
            else:
                print(f"Error! Please write your prefix from '{_command[0]}' to '-'")
        else:
            _return = _return + str(_command[i])
else:
    print(False)
print(_return.split(' ')[0])

#if _command.split(' ') == [(_command[0] if _command[0] == "-" else _command[0]) for i in range(0, len(_command), 1)]: