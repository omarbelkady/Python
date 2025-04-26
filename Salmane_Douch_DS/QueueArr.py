from Bin_Search_Algo import sequence_Nelan


def permutation(mylist: list)->list:
    if len(sequence) <= 1:
        return [sequence]
    permutations=[]
    seen = set()
    for i in range(len(sequence)):
        current=sequence[i]
        if current in seen:
            continue
        seen.add(current)
        remaining = sequence[:i]+sequence[i+1:]
        for j in permutation(remaining):
            if isinstance(sequence,arr):
                permutations.appen''''''