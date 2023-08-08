#Length of last word:

def length_of_last_word(s):
    words = s.strip().split()
    return len(words[-1]) if words else 0
#Examples:
print(length_of_last_word("Hello World"))            # Output: 5
print(length_of_last_word("fly me to the moon"))     # Output: 4
print(length_of_last_word("luffy is still joyboy"))    # Output: 6
