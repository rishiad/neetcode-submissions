class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []


    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
        if self.large and self.small[0] > self.large[0]:
            tmp = heapq.heappop_max(self.small)
            heapq.heappush(self.large, tmp)

        if len(self.small) > len(self.large) + 1:
            tmp = heapq.heappop_max(self.small)
            heapq.heappush(self.large, tmp)
        if len(self.large) > len(self.small) + 1:
            tmp = heapq.heappop(self.large)
            heapq.heappush_max(self.small, tmp)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (self.large[0] + self.small[0]) / 2 