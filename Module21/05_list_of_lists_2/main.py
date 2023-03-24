def rect(leest):
    rect_list = []
    for i_element in leest:
        if isinstance(i_element, list):
            temp = rect(i_element)
            for temp_elem in temp:
                rect_list.append(temp_elem)
        elif isinstance(i_element, int):
            rect_list.append(i_element)
    return rect_list




nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(rect(nice_list))

# TODO здесь писать код
