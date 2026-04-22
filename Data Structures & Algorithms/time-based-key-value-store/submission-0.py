class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            res = ""
            inside = self.map[key]
            l,r = 0, len(inside) - 1

            while l <= r:
                m = (l + r) // 2
                check = inside[m]
                if check[1] <= timestamp:
                    res = check[0]
                    l = m + 1
                else:
                    r = m - 1
            return res
        else:
            return ""
            
        
