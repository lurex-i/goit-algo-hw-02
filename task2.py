from collections import deque
import sys

def is_palindrome(text: str):
    deq = deque("".join(ch.lower() for ch in text if ch.isalpha()))
    while len(deq):
        beg_c = deq.popleft()
        if len(deq):
            end_c = deq.pop()
            if beg_c != end_c:
                return False
        else:
            # We have even symbols, so we checked them all
            return True
    # We checked all odd symbols and didn't find differencies
    return True


def main():
    if len(sys.argv) < 2:
        print("Call the application with potential palindrome string")
    else:
        text = " ".join(sys.argv[1:])
        print(f"We'll analyze '{text}' as palindrome.")
        result = is_palindrome(text)
        if result:
            print("Yes, it is a palindrome.")
        else:
            print("No, it is just a common text.")

if __name__ == "__main__":
    main()