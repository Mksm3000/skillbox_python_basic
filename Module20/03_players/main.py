players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

remix = list()
for index, value in players.items():
    stamp = index + value
    remix.append(stamp)
print(remix)