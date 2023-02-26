# imo the elegant solution
'''
def permutate(arr: list[list[int]]) -> list[list[int]]:
    if len(arr) == 1:
        return [arr]
    else:
        ret = list()
        for a in permutate(arr[1:]):
            for l in range(len(a)):
                ret.append((a[:l] + [arr[0]] + a[l:]))
            ret.append(a+[arr[0]])
        return ret
def poweroftwo(number: int) -> bool:
    while number%2==0:
        number = number/2
    return number==1
def convert_list_to_str(arr: list[int]) -> int:
    ret = [str(a) for a in arr]
    ret = "".join(ret)
    return int(ret)
def putittogether(n: int) -> bool:
    n_arr = [int(i) for i in str(n)]

    #get list of all permutations
    perms = permutate(n_arr)
    for per in perms:
        if per[0] != 0:
            int_per = convert_list_to_str(per)
            if poweroftwo(int_per):
                return True
    return False


print(putittogether(411228773))
'''

# fast solution
def fast(n: int) -> bool:
    as_str = str(n)
    #list_of_digits = [str(i) for i in range(10)]


    #make a list of possible powers of 2
    list_of_pows = ["1"]
    i = 1
    while len(str(2**i))  <= len(as_str):
        if len(str(2**i)) == len(as_str):
            list_of_pows.append(str(2**i))
        i += 1

    #count digits
    list_of_dicts = [{a: l.count(a) for a in set(l)} for l in list_of_pows]

    dict_of_n = {a: as_str.count(a) for a in set(as_str)}

    return dict_of_n in list_of_dicts


print(fast(203))