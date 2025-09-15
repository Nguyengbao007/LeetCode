# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

# Example 1:

# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
from collections import deque
class RecentCounter:
    def __init__(self):
        # Initialize a double-ended queue to keep track of ping times
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Add the new ping time to the queue
        self.queue.append(t)

        # Remove ping times that are older than 3000ms from the current time
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        # Return the number of pings within the last 3000ms
        return len(self.queue), self.queue
obj = RecentCounter()
# param_1 = obj.ping(1)
print(obj.ping(1))
#param_1 = obj.ping(100)
print(obj.ping(100))
#param_1 = obj.ping(3001)
print(obj.ping(3001))
#param_1 = obj.ping(3002)
print(obj.ping(3002))
#param_1 = obj.ping(8000)
print(obj.ping(8000))
# Example usage:
# recent_counter = RecentCounter()
# count = recent_counter.ping(1)  # Assuming 't' is a timestamp in milliseconds