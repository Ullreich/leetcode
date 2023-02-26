def find_best_list(n, speed, efficiency, k):
    # make a list of sorted tuples
    sort_list = sorted(zip(speed, efficiency), key=lambda x: -x[1])

    # find the best engineer and their index
    m = max(sort_list, key=lambda x: x[0]*x[1])
    i = sort_list.index(m)

    # check if list is empty
    try:
        s_front, e_front = zip(*sorted(sort_list[:i], key=lambda x: -x[0]))
    except ValueError:
        s_front, e_front = [], []
    try:
        s_back, e_back = zip(*sorted(sort_list[i+1:], key=lambda x: -x[1]))
    except ValueError:
        return ((sum(s_front[:k-1])+m[0]) * m[1])%(10**9+7)
    # return stuff based on cases
    if k-1 <= i:
        return ((sum(s_front[:k-1])+m[0]) * m[1])%(10**9+7)
    # check if adding stuff in blocks of efficiency increases value
    else:
        sum_front = sum(s_front[:i])+m[0]
        m = m[1]

        maxmann = sum_front*m


        for s_i, s_val  in enumerate(s_back[:k-i-1]):
            #print(sum_front*m)
            if i+s_i+1 >= k-1 or (e_back[s_i] != e_back[s_i+1]):
                if (sum_front+sum(s_back[:s_i+1]))*e_back[s_i] > maxmann:

                    m = e_back[s_i]
                    maxmann = (sum_front + sum(s_back[:s_i + 1]))*m
        return maxmann%(10**9+7)


####
# the following is garbadge
















def find_best_list(n, speed, efficiency, k):
    # make a list of sorted tuples
    sort_list = sorted(zip(speed, efficiency), key=lambda x: -x[1])

    # find the best engineer and their index
    m = max(sort_list, key=lambda x: x[0]*x[1])
    i = sort_list.index(m)

    # check if list is empty
    try:
        s_front, e_front = zip(*sorted(sort_list[:i], key=lambda x: -x[0]))
    except ValueError:
        s_front, e_front = [], []
    try:
        s_back, e_back = zip(*sorted(sort_list[i+1:], key=lambda x: -x[1]))
    except ValueError:
        return (sum(s_front[:k-1])+m[0]) * m[1]
    # return stuff based on cases
    if k-1 <= i:
        return (sum(s_front[:k-1])+m[0]) * m[1]
    # check if adding stuff in blocks of efficiency increases value
    else:
        sum_front = sum(s_front[:i])+m[0]
        m = m[1]

        maxmann = sum_front*m

        #print(sort_list)
        #print(s_back[:-1])
        #print(e_back)

        for s_i, s_val  in enumerate(s_back[:-1]):
            #print(sum_front*m)
            if (e_back[s_i] != e_back[s_i+1]) or s_i+1==k:
                if (sum_front+sum(s_back[:s_i+1]))*e_back[s_i] > maxmann:

                    m = e_back[s_i]
                    maxmann = (sum_front + sum(s_back[:s_i + 1]))*m
                else:
                    return maxmann
        return maxmann

    """
    else:
        s_sum_rec, m_rec = find_best_list(n, s_back, e_back, k-(i+1))
        s_sum = (sum(s_front[:i]))+m[0]
        print("m0", m[0])

        print("S", s_sum)
        print("m", m[1])
        print(s_sum * m[1], (s_sum + s_sum_rec) * m_rec)
        if s_sum*m[1] >= (s_sum+s_sum_rec)*m_rec:
            return s_sum, m[1]
        else:
            return s_sum+s_sum_rec, m_rec
    """

def helpis(s_back, e_back):
    pass












n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2

#n = 4
#speed = [8,9,5,9]
#efficiency = [1,2,6,9]
#k = 2

n = 7
speed = [1,4,1,9,4,4,4]
efficiency = [8,2,1,7,1,8,4]
k = 6

# result 119
# expected 98

n = 4
speed = [8,9,5,9]
efficiency = [1,2,6,9]
k = 2

# output 81
# expected 84

n = 6
speed = [8,7,5,9,1,3]
efficiency = [1,7,5,10,1,3]
k = 4

# output = 105
# expected = 112

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2

#print(find_best_list(n, speed, efficiency, k))
print(find_best_list(n, speed, efficiency, k))


"""
def find_best_list(n, speed, efficiency, k):
    # make a list of sorted tuples
    sort_list = sorted(zip(speed, efficiency), key=lambda x: -x[1])

    # find the best engineer and their index
    m = max(sort_list, key=lambda x: x[0]*x[1])
    i = sort_list.index(m)

    # check if list is empty
    if not sort_list[:i]:
        return m[0]*m[1]

    # explanation of what this does:
    # v = sorted(sort_list[:i], key=lambda x: -x[0])        sort the list of s,e (ordered by descending e && up to i) by descending s
    # w = list(zip(*v))                                     unzip into s, e and turn into list
    # s = w[0][min(i, k-1)]                                 we only need the s row and only the first i or k-1
    # (sum(s)+m[0])*m[1]                                    sum up (fastes e + m_s) * m_e

    # return (sum(list(zip(*sorted(sort_list[:i], key=lambda x: -x[0])))[0][:min(i, k-1)])+m[0])*m[1]

    if k-1 == min(i, k-1):
        return (sum(list(zip(*sorted(sort_list[:i], key=lambda x: -x[0])))[0][:k-1])+m[0])*m[1]
    else:
"""



"""
def find_best_list(n, speed, efficiency, k):
    # make a list of sorted tuples
    sort_list = sorted(zip(speed, efficiency), key=lambda x: -x[1])

    # find the best engineer and their index
    m = max(sort_list, key=lambda x: x[0]*x[1])
    i = sort_list.index(m)

    # check if list is empty
    try:
        s_front, e_front = zip(*sorted(sort_list[:i], key=lambda x: -x[0]))
    except ValueError:
        s_front, e_front = [], []
    print(s_front)
    try:
        s_back, e_back = zip(*sorted(sort_list[i+1:min(k-i+1, len(sort_list))], key=lambda x: -x[1]))
    except ValueError:
        return sum(s_front[:k-1])+m[0] * m[1]
    print(s_front)
    print(s_back)
    # return stuff based on cases
    if k-1 <= i:
        return sum(s_front[:k-1])+m[0] * m[1]
    # check if adding stuff in blocks of efficiency increases value
    else:
        sum_front = sum(s_front[:i])+m[0]
        m = m[1]

        maxmann = sum_front*m

        #print(sort_list)
        #print(s_back[:-1])
        #print(e_back)

        for s_i, s_val  in enumerate(s_back[:-1]):
            #print(sum_front*m)
            if (e_back[s_i] != e_back[s_i+1]) or s_i+1==len(s_back[:-1]):
                if (sum_front+sum(s_back[:s_i+1]))*e_back[s_i] > maxmann:

                    m = e_back[s_i]
                    maxmann = (sum_front + sum(s_back[:s_i + 1]))*m
                else:
                    return maxmann
        return maxmann

    """
