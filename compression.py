
def compact(lst):
    return list(filter(None, lst))
 
compact([0, 1, False, None, 2, '', 3, 'a', 's', 34])
>>> [1, 2, 3, 'a', 's', 34]
