from sys import prefix
from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix