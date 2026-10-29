#!/usr/bin/env python3

"""
This module contains an asynchronous routine that spawns multiple coroutines
concurrently using asyncio tasks. It gathers the results as they complete
to maintain an ordered list of delays without using built-in sort functions.

"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns the wait_random coroutine n times concurrently with a specified
    maximum delay, and collects the resulting delays in ascending order.

    Args:
        n (int): The total number of times to spawn the coroutine.
        max_delay (int): The maximum delay value for each coroutine.

    Returns:
        List[float]: A list containing all the generated float delays
        arranged in ascending order based on execution completion.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
        
    return delays
