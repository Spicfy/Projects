def power_set(L):
    '''(list of int) --> 2D list
>>> power_set([1, 2])
[ [], [1], [2], [1,2] ]
    '''
    if len(L) == 0:
        return [ [] ]#returns the emtpy set because this is obvious
    if len(L) ==1:
        return [[], [L[0]] ]
    pps = power_set(L[1: ])
    fps = pps[:] #aliasing
    for item in pps:
        fps.append(item + [L[0]])
    return fps
