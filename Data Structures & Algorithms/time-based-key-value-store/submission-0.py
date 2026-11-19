class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        entries = self.store[key]
        left = 0
        right = len(entries) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            entry_ts = entries[mid][0]
            entry_val = entries[mid][1]

            if entry_ts <= timestamp:
                result = entry_val
                left = mid + 1
            else:
                right = mid - 1

        return result