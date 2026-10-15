
from typing import List


def find_longest_common_prefix(strings: List[str]) -> str:
    """
    Return the longest prefix shared by any two strings.
    Return an empty string if fewer than two strings are provided.
    """
    if len(strings) < 2:
        return ""

    prefix_counts = {}

    for string in strings:
        for i in range(1, len(string) + 1):
            prefix = string[:i]
            prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1

    longest = ""

    for prefix, count in prefix_counts.items():
        if count >= 2 and len(prefix) > len(longest):
            longest = prefix

    return longest
