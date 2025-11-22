from collections import deque


def is_palindrome(string: str) -> bool:
    cleaned = ''.join(c.lower() for c in string if c.isalnum())
    queue = deque(cleaned)

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False

    return True


try:
    while True:
        user_input = input("Enter a string to check for palindrome (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("See you later!")
            break
        if is_palindrome(user_input):
            print(f'"{user_input}" is a palindrome.')
        else:
            print(f'"{user_input}" is not a palindrome.')

except KeyboardInterrupt:
    print("\nProgram terminated by user.")
