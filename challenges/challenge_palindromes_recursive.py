def is_palindrome_recursive(word, low_index, high_index):
    if not isinstance(word, str) or word == "":
        return False

    if low_index > high_index:
        return True

    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return False


# print(is_palindrome_recursive("PAULA", 0, 4))
# print(is_palindrome_recursive("ANA", 0, 2))
# print(is_palindrome_recursive("SOCOS", 0, 4))
# print(is_palindrome_recursive("COXINHA", 0, 6))
