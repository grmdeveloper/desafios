string = input('Validação para pares de brackets: ')
size = len(string)

openers = [
    '[', '(', '{'
]

closers = [
    ']', ')', '}'
]

status = True
cpointer = 1
for v in string:

    pointer = string.index(v)

    if size % 2 != 0:
        status = False
        break

    if pointer < (size / 2) and status:
        if v in openers:
            pointer += 1
        else:
            status = False
            break

    elif pointer < size and status:
        if v in closers:

            x = string[string.index(v)-cpointer]
            if x in openers:
                oindex = openers.index(x)
            if v in closers:
                cindex = closers.index(v)

            if oindex != cindex:
                status = False

            pointer += 1
            cpointer += 2

        else:
            status = False
            break

if status:
    print('SIM')
else:
    print('NÃO')
