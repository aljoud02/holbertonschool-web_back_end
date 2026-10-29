#!/usr/bin/env python3
"""
This module contains a basic asynchronous coroutine that demonstrates
how to utilize the asyncio and random modules to simulate unexpected delays
in network requests or Input/Output Operations.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay seconds
    (inclusive, floating-point value) and eventually returns the delay.

    Args:
        max_delay (int): The upper limit of the random delay time.

    Returns:
        float: The amount of time in seconds that the coroutine slept.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
