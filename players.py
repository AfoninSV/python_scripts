players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

def tpl_split(p_dict):
    p_list = []
    for key, value in p_dict.items():
        p_list.append(key + value)
    return p_list


print(tpl_split(players))