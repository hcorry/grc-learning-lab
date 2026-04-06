"""
rate_limiter.py

Simple in-memory fixed-window rate limiter for the grade endpoint.
Max 10 requests per 60-second window. Single-user local tool — no
persistence needed.
"""

import time
from collections import deque

# Configuration
MAX_REQUESTS = 10
WINDOW_SECONDS = 60

# Timestamps of recent grade requests
_request_times = deque()


def check_rate_limit():
    """
    Call before processing a grade request.

    Returns (allowed: bool, retry_after: int)
      - allowed=True means the request can proceed
      - allowed=False means the limit is hit; retry_after is seconds to wait
    """
    now = time.time()
    window_start = now - WINDOW_SECONDS

    # Drop timestamps outside the current window
    while _request_times and _request_times[0] < window_start:
        _request_times.popleft()

    if len(_request_times) >= MAX_REQUESTS:
        # Oldest request in the window determines when the slot opens
        oldest = _request_times[0]
        retry_after = int(oldest + WINDOW_SECONDS - now) + 1
        return False, retry_after

    # Record this request
    _request_times.append(now)
    return True, 0
