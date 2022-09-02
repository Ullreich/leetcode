def selfdiving(number):
    intset = set([int(i) for i in str(number)])
    if 0 in intset:
        return False
    return sum([number%i for i in intset])==0

print([i for i in range(22) if selfdiving(i)])

# nicer
# return [x for x in range(left, right+1) if all((i and (x % i==0) for i in map(int, str(x))))]