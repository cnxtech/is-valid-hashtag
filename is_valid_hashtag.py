"""is_valid_hashtag

2018 Caleb Ely
<https://github.com/le717/is-valid-hashtag>

The Unlicense
<http://unlicense.org/>

"""


import re


__all__ = ["is_valid_hashtag"]


def is_valid_hashtag(hashtag: str) -> bool:
    """Check if a hashtag is valid.

    Args:
        hashtag (str): The text to check.

    Returns:
        bool: True for valid hashtag, False otherwise.
    """
    pattern = re.compile("#(?:[a-z]|(?:\d|_)[a-z])\w+",
                         re.IGNORECASE | re.ASCII)
    result = pattern.fullmatch(hashtag)
    return result is not None
