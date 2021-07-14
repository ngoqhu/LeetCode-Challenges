class Solution:
    def customSortString(self, order: str, str: str) -> str:
        mapping = defaultdict(lambda: 26)
        for i, v in enumerate(order):
            mapping[v] = i
        return "".join(sorted(list(str), key=mapping.__getitem__)) 
