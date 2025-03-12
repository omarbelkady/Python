def find_max_pair(mytup):
    if len(mytup) < 2:
        raise ValueError("Tuple must have at least two elements")
    new_list = list(mytup)
    new_list.sort()
    last_element = new_list[-1]
    penultimate_element = new_list[-2]
    return last_element * penultimate_element
def rotate_by_n_steps(mylist, steps):
    print("You decided to move the list by:", steps, "steps")
    steps = steps % len(mylist)
    rotated_list = mylist[-steps:] + mylist[:-steps]
    return rotated_list
def remove_duplicates(mylist):
    present = set()
    unique_elems = []
    for i in mylist:
        if i not in present:
            present.add(i)
            unique_elems.append(i)
    return unique_elems

def is_magic(the_list):
    length = len(the_list)

    # Ensure the matrix is square
    if any(len(row) != length for row in the_list):
        return False

    magic_sum = sum(the_list[0])  # Reference sum

    # Check sum of each row
    for row in the_list:
        if sum(row) != magic_sum:
            return False
    for col in range(length):
        if sum(the_list[i][col] for i in range(length)) != magic_sum:
            return False

    if sum(the_list[i][i] for i in range(length)) != magic_sum:
        return False

    if sum(the_list[i][length-1-i] for i in range(length)) != magic_sum:
        return False

    return True
