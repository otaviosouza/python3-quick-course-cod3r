#!python3

module = __name__


def greeting(name='World'):
    print(f'Hello, {name}!')


def greeting_2():
    if module != '__main__':
        return
    print('greeting_2 calls gretting')
    greeting()


def sum_tim(a, b, c):
    return (a + b) * c


if module == '__main__':
    greeting_2()
