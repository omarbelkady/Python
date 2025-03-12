def is_valid(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


# Example:
print(is_valid("()[]{}"))  # Output: True
print(is_valid("(]"))  # Output: False
x