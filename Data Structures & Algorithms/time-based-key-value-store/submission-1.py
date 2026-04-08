class TimeMap:

    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.values.get(key) is not None:
            self.values[key].append((value, timestamp))
        else:
            self.values[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if self.values.get(key) is None:
            return ""
        
        values = self.values[key]
        print(values)
        for value in reversed(values):
            print(value)
            if value[1] <= timestamp:
                return value[0]
        return ""