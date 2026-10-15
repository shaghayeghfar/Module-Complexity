
def count_letters(s: str) -> int:
    """
    Count uppercase letters that never appear in lowercase.
    """
    lowercase_letters = set()
    uppercase_letters = set()

    for letter in s:
        if letter.islower():
            lowercase_letters.add(letter)
        elif letter.isupper():
            uppercase_letters.add(letter)

    return sum(
        1 for letter in uppercase_letters
        if letter.lower() not in lowercase_letters
    )
