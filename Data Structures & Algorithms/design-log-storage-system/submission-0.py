class LogSystem:

    def __init__(self):
        self.logs = []

    def to_epoch(self, timestamp: str) -> int:
        year, month, day, hour, minute, second = timestamp.split(":")
        year = int(year) - 2000
        res = (
            year * 365 * 86_400 +
            int(month) * 30 * 86_400 +
            int(day) * 86_400 +
            int(hour) * 3600 +
            int(minute) * 60 +
            int(second)
        )
        return res

    def put(self, id: int, timestamp: str) -> None:
        epoch = self.to_epoch(timestamp)
        self.logs.append((id, epoch))

    def apply_granularity(self, timestamp: str, granularity: str, is_start: bool):
        if granularity == "Year":
            if is_start:
                res = timestamp.split(":")[0] + ":01:01:00:00:00"
            else:
                res = timestamp.split(":")[0] + ":12:31:23:59:59"
        elif granularity == "Month":
            if is_start:
                res = ":".join(timestamp.split(":")[:2]) + ":01:00:00:00"
            else:
                res = ":".join(timestamp.split(":")[:2]) + ":31:23:59:59"
        elif granularity == "Day":
            if is_start:
                res = ":".join(timestamp.split(":")[:3]) + ":00:00:00"
            else:
                res = ":".join(timestamp.split(":")[:3]) + ":23:59:59"
        elif granularity == "Hour":
            if is_start:
                res = ":".join(timestamp.split(":")[:4]) + ":00:00"
            else:
                res = ":".join(timestamp.split(":")[:4]) + ":59:59"
        elif granularity == "Minute":
            if is_start:
                res = ":".join(timestamp.split(":")[:5]) + ":00"
            else:
                res = ":".join(timestamp.split(":")[:5]) + ":59"
        else:
            res = timestamp
        return res

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        res = []

        start = self.to_epoch(self.apply_granularity(start, granularity, True))
        end = self.to_epoch(self.apply_granularity(end, granularity, False))

        for id, time in self.logs:
            if (start <= time <= end):
                res.append(id)
        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
