def rever(block):
    plug = ''
    buffer = ''
    for symbol in block:
        if symbol.isalpha():
            buffer = symbol + buffer
        elif not symbol.isalpha():
            buffer = buffer + symbol
            plug += buffer
            buffer = ''
    plug += buffer

    return plug


text = input('Сообщение: ').split()
print(text)

text_rever = [rever(block) for block in text]
print(*text_rever)
