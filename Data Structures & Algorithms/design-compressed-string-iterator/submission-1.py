class StringIterator:

    def __init__(self, compressedString: str):
        self.compressed_str = compressedString
        self.ptr = 0
        self.char = ""
        self.num = 0

    def next(self) -> str:
        if not self.hasNext():
            return ""
        
        if self.num == 0:
            # look for next
            self.char = self.compressed_str[self.ptr]
            self.ptr += 1

            while (
                self.ptr < len(self.compressed_str) and 
                self.compressed_str[self.ptr].isdigit()
            ):
                self.num = 10 * self.num + int(self.compressed_str[self.ptr])
                self.ptr += 1
        
        self.num -= 1
        return self.char
 

    def hasNext(self) -> bool:
        return self.ptr != len(self.compressed_str) - 1


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
