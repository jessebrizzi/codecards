from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low = []
        self.high = []
        

    def addNum(self, num: int) -> None:
        if not self.low or num < -self.low[0]:
            heappush(self.low, -num)
        else:
            heappush(self.high, num)
        if len(self.high) > len(self.low):
            heappush(self.low, -heappop(self.high))
        if len(self.low) > 1 + len(self.high):
            heappush(self.high, -heappop(self.low))
        

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2