def special(word):
    symbol = "(.,:;!_№@^*-+()\|/#%&)"
    for i, char in enumerate(word):
        if char in symbol:
            # print('длина блока', len(word))
            # print('индекс:', i)
            return i
    else:
        pass


def rev(block):
    index = special(block)
    if index is None:
        plug = ''.join(list(block)[::-1])
    #       plug = plug[::-1]
    #       plug = ''.join(plug)
    else:
        # print(block[:index:-1])
        # print(block[index])
        # print(block[index - 1::-1])
        plug = block[index-1::-1] + block[index] + block[:index:-1]
    return plug


text = input('Сообщение: ').split()
text_rev = [rev(block) for block in text]

print(*text_rev)
