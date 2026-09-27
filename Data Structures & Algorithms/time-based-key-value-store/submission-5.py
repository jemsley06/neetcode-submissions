class TimeMap:

    def __init__(self):
        self.items = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.items.get(key, 0) == 0:
            self.items[key] = []
        self.items[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        options = self.items.get(key, None)
        if options == None:
            return ""
        l, r = 0, len(options) - 1
        m = 0
        while l <= r:
            m = (l + r) // 2
            if options[m][1] == timestamp:
                return options[m][0]
            elif options[m][1] > timestamp:
                r = m - 1
            else:
                l = m + 1
        if options[m][1] <= timestamp:
            return options[m][0]
        else:
            while m >= 0 and options[m][1] > timestamp:
                m-=1
            if m < 0:
                return ""
            else:
                return options[m][0]
