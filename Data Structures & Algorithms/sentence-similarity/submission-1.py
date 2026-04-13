class Solution:
    @staticmethod
    def compute_key(a: str, b: str) -> tuple[str]:
        return f"{a}-{b}"

    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        similarity_keys = set()
        for keys in similarPairs:
            similarity_keys.add(self.compute_key(keys[0], keys[1]))

        print(similarity_keys)

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or (
                len(similarPairs) > 0 and
                self.compute_key(sentence1[i], sentence2[i]) in similarity_keys or
                self.compute_key(sentence2[i], sentence1[i]) in similarity_keys
            ):
                continue
            else:
                return False
        return True