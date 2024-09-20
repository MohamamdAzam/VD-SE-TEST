import time
import threading
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, max_requests=5, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.user_requests = defaultdict(deque)
        self.lock = threading.Lock()

    def allow_request(self, user_id):
        current_time = time.time()
        with self.lock:
            requests = self.user_requests[user_id]

            while requests and requests[0] <= current_time - self.time_window:
                requests.popleft()

            if len(requests) < self.max_requests:
                requests.append(current_time)
                return True
            else:
                return False

# Example :
rate_limiter = RateLimiter()

def simulate_request(user_id):
    if rate_limiter.allow_request(user_id):
        print(f"Request allowed for user {user_id}")
    else:
        print(f"Request denied for user {user_id}")


if __name__ == "__main__":
    user_id = 'user1'
    
    for _ in range(7):
        simulate_request(user_id)
        time.sleep(10)
