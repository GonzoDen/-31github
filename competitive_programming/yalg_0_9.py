def is_valid_sequence(s):
    stack = []

    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for bracket in s:
        if bracket in bracket_pairs.values():
            stack.append(bracket)
        elif bracket in bracket_pairs.keys():
            if not stack or stack.pop() != bracket_pairs[bracket]:
                return "no"
        else:
            pass

    return "yes" if not stack else "no"

input_sequence = input()

print(is_valid_sequence(input_sequence))
