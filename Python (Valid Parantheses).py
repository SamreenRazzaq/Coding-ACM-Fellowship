# Valid Parantheses:

def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False
    return not stack
#Examples:
print(is_valid_parentheses("()"))           # Output: True
print(is_valid_parentheses("()[]{}"))       # Output: True
print(is_valid_parentheses("(]"))           # Output: False
