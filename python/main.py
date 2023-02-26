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


# output 25
# expected 51

n = 6
speed = [10,5,1,7,4,2]
efficiency = [2,1,1,1,7,3]
k = 6

n = 5
speed = [10,6,6,5,8]
efficiency = [8,2,8,10,6]
k = 3

# output 174
# expected 168

print(find_best_list(n, speed, efficiency, k))
