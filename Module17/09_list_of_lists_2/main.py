nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# new_list = [nice_list.append(x) for x in range(0, len(nice_list))]

new_list = [item for sublist in nice_list for item in sublist]
new_list = [item for sublist in new_list for item in sublist]

# for sublist in nice_list:
#     for item in sublist:
#         new_list.append(item)

# for sublist in new_list:
#     for item in sublist:
#         new_list.append(item)

print(new_list)
