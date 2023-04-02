import family


def rand_children_list() -> [family.Child, ...]:
    child_qty = 3
    children = list()
    for i_child in range(1, child_qty + 1):
        child = family.Child(f'Child {i_child}',
                             i_child + 5)
        children.append(child)
    return children
