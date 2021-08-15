def slice_less(my_list, lesser):
    q = []
    for i in sorted(my_list):
        if i > lesser: q.append(i)
    q.reverse()
    return q
