class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Build tree
root = Node(10)
root.left = Node(7)
root.right = Node(12)
root.left.left = Node(55)
root.left.right = Node(9)
root.right.left = Node(4)
root.right.left.right = Node(8)
root.right.left.right.left = Node(2)

# Corrected Functions:

def depth(root, value, l=1):
    if root is None:
        return None
    if root.value == value:
        return l
    return depth(root.left, value, l+1) or depth(root.right, value, l+1)

def min_depth(root):
    if root is None:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))

def left_view(root, left_list, level=0):
    if root is None:
        return
    if level == len(left_list):  # fixed typo
        left_list.append(root.value)
    left_view(root.left, left_list, level + 1)
    left_view(root.right, left_list, level + 1)

def max_sum(root):
    if root is None:
        return 0
    return root.value + max(max_sum(root.left), max_sum(root.right))

# New: Check if tree is balanced
def is_balanced(root):
    def height_and_balanced(node):
        if node is None:
            return (0, True)
        lh, left_balanced = height_and_balanced(node.left)
        rh, right_balanced = height_and_balanced(node.right)
        balanced = abs(lh - rh) <= 1 and left_balanced and right_balanced
        return (1 + max(lh, rh), balanced)
    _, balanced = height_and_balanced(root)
    return balanced


print("Depth of 8:", depth(root, 8))             # should return level
print("Minimum depth:", min_depth(root))         # minimum depth
left_result = []
left_view(root, left_result)
print("Left view:", left_result)
print("Max sum path:", max_sum(root))
print("Is balanced?:", is_balanced(root))
