def caesar(stroka, move, abc_low, abc_up):
    caesar = ''
    for sym in stroka:
        if sym.islower():
            caesar += abc_low[(abc_low.index(sym) + move) % len(abc_low)]
        elif sym.isupper():
            caesar += abc_up[(abc_up.index(sym) + move) % len(abc_up)]
        else:
            if sym == '/':
                sym = '.'
            elif sym == '.':
                sym = '-'
            elif sym == '(':
                sym = '`'
            caesar += sym
    return caesar


text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

alphabet_low = 'abcdefghijklmnopqrstuvwxyz'
alphabet_UP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = -1  # int(input('Введите сдвиг: '))

decode = caesar(text, shift, alphabet_low, alphabet_UP)
print(f'Зашифрованное сообщение, но ещё со сдвигом: {decode}')

slices = decode.split()
block_temp = []
block_list = []
for block in slices:
    block_temp.append(block)
    if '.' in block:
        block_list.append(block_temp)
        block_temp = []

new_list = []
sdvig = 3
for i in range(len(block_list)):
    for part in block_list[i]:
        sdvig_p = sdvig % len(part)
        part_new = part[-sdvig_p::] + part[:-sdvig_p:]
        new_list.append(part_new)
    sdvig += 1

print(' '.join(new_list))
