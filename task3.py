def are_brackets_balanced(sequence: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    opening_brackets = bracket_map.values()

    for char in sequence:
        if char in opening_brackets:
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False

    return not stack


def main() -> None:
    test_sequences = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }"
    ]

    for seq in test_sequences:
        if are_brackets_balanced(seq):
            print(f"{seq}: Симетрично")
        else:
            print(f"{seq}: Несиметрично")

if __name__ == "__main__":
    main()
