def generate_dict(word):
    dict = {}

    for letter in word:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1

    return dict


def is_anagram(first_string, second_string):
    if (
        not isinstance(first_string, str)
        or first_string == ""
        or not isinstance(second_string, str)
        or second_string == ""
    ):
        return False

    # lower() method
    # https://www.w3schools.com/python/ref_string_lower.asp
    first_dict = generate_dict(first_string.lower())
    second_dict = generate_dict(second_string.lower())

    return first_dict == second_dict


# print(is_anagram("Paula", "Carlos"))
# print(is_anagram("amor", "roma"))
