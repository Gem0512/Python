from itertools import permutations


def perm_str(x):
    lst_perm = permutations(x)
    for i in (lst_perm):
        print(''. join(i))

for i in range(int(input())):
    input_str = input()
    perm_str(input_str)
