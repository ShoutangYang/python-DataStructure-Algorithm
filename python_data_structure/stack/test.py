from stack import Stack


if __name__ == '__main__':
    S =Stack()
    print( S.isEmpty())
    S.push('1')
    print(S.size)
    S.push(True)
    print(S.isEmpty())

    print(S.peek)

    print(S.size())
    for item in S.items:
        print(item)


