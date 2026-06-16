class Solution: 
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_ = {order[i]: i for i in range(len(order))}
        sorted_words = sorted(words, key=lambda x: [order_[c] for c in x])
        return sorted_words == words