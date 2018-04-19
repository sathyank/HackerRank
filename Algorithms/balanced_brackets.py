def is_matched(expression):
    dict = {'{' : '}', '[' : ']', '(' : ')'}
    stack = []
    for char in expression:
        if char in dict:
            stack.append(dict[char])
        elif stack and char == stack[-1]:
                stack.pop()
        else: return False
    return not stack

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
