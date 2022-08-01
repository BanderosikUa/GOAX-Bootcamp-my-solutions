s = "Python Bootcamp"


def hash_function(string: str) -> int:
    return sum(
        ind * ord(char) for ind, char in enumerate(string)
    )


print(hash_function(s))