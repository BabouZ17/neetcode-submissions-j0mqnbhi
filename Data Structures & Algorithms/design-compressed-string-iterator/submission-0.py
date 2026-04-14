class StringIterator:

    def __init__(self, compressedString: str):
        self.string = compressedString
        self.ptr = 0
        self.num = 0
        self.char = ""

    def next(self) -> str:
        if not self.hasNext():
            return " "

        if self.num == 0:
            self.char = self.string[self.ptr]
            self.ptr += 1
            while (self.ptr < len(self.string) and
                self.string[self.ptr].isdigit()):
                self.num = self.num * 10 + int(self.string[self.ptr])
                self.ptr += 1
        self.num -= 1
        return self.char
        

    def hasNext(self) -> bool:
        return self.ptr != len(self.string) or self.num != 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
