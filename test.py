def get_input():
    _get = int(input())
    try:
        return _get
    except ValueError:
        print("Please try again!")

def square_root(_input):
    count = 1
    for i in range(_input):
        count += 2
        if count >= _input:
            if count > _input:
                i -= 1
                print(i)
                break
            if count == _input:
                print(i)
                break

if __name__ == "__main__":
    _input = get_input()
    square_root(_input)