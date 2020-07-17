from typing import List
from collections import Counter
from operator import itemgetter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(map(itemgetter(0), Counter(nums).most_common(k)))
